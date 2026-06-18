# app.py
# =============================================================================
# Dashboard de Monitoramento da Dengue — Petrolina/PE (v10)
# PIBIC Jr — IFSertãoPE Campus Petrolina
# =============================================================================
#
# CHANGELOG v9 → v10
# =============================================================================
# [ESTRATÉGICO]   Modelagem ML (Regressão Linear, Polinomial, Random Forest)
#                 REMOVIDA. Substituída por EDA avançada com ferramental de
#                 análise de séries temporais e inferência causal.
#
# [NOVO]          CCF com IC Bootstrap (1000 permutações circulares):
#                 substitui a CCF analítica (±1.96/√n), mais robusta para
#                 séries autocorrelacionadas.
#
# [NOVO]          Causalidade de Granger com seleção de lag por menor p-valor
#                 e correção FDR (Benjamini-Hochberg) para múltiplos testes.
#                 Diferenciação automática conforme ADF/KPSS.
#
# [NOVO]          VIF (Variance Inflation Factor): diagnóstico de
#                 colinearidade entre variáveis climáticas.
#
# [NOVO]          Correlação parcial: efeito independente de Chuva e Temp
#                 controlando mutuamente.
#
# [NOVO]          Informação Mútua (MI): captura dependências não-lineares.
#
# [NOVO]          Rolling Spearman (janela 52 semanas): evolução temporal
#                 da relação clima-dengue ao longo de 15 anos.
#
# [NOVO]          Aba "ENSO e Dengue": integração com ONI (NOAA/CPC),
#                 boxplots por fase/intensidade, Kruskal-Wallis,
#                 Mann-Whitney pairwise, correlações estratificadas,
#                 perfil sazonal por fase ENSO.
#
# [NOVO]          Decomposição STL (Seasonal-Trend using LOESS) com
#                 period=52 na aba Panorama Histórico.
#
# [NOVO]          Testes de estacionariedade (ADF + KPSS) combinados
#                 com conclusão automática.
#
# [NOVO]          Aba "Análise Estatística" substituiu "Modelagem":
#                 Rolling Spearman, estacionariedade, outliers, descritivas.
#
# [NOVO]          Tutorial atualizado com Granger, STL, ENSO, bootstrap.
#
# [MELHORIA]      5 abas (vs 4): Situação Atual, Panorama, Clima×Dengue,
#                 ENSO, Estatística. Educacional como expander.
#
# [MANTIDO]       Situação Atual, Panorama Histórico, exportação, quiz.
# =============================================================================

import streamlit as st

from components.layout import inject_css, render_sidebar
from utils.data_loader import load_data, apply_filters

# ── Configuração da página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard Dengue — Petrolina/PE — PIBIC Jr",
    page_icon="🦟",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

# ── Cabeçalho ────────────────────────────────────────────────────────────────
st.markdown(
    "<h1 style='margin-bottom:0;'>🦟 Dashboard de Monitoramento da Dengue</h1>"
    "<h4 style='margin-top:0; color:#666;'>Petrolina/PE — Projeto PIBIC Jr "
    "| IFSertãoPE</h4>",
    unsafe_allow_html=True,
)

# ── Dados ────────────────────────────────────────────────────────────────────
df = load_data()

# ── Sidebar e filtros ────────────────────────────────────────────────────────
filtros = render_sidebar(df)
df_filtrado = apply_filters(
    df,
    date_range=filtros["date_range"],
    anos=filtros["anos"],
    nivel=filtros["nivel"],
    estacoes=filtros["estacoes"],
)

# ── Abas ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Situação Atual",
    "📈 Panorama Histórico",
    "🌡️ Clima × Dengue",
    "🌊 ENSO e Dengue",
    "📊 Análise Estatística",
])

from pages import (situacao_atual, panorama_historico, clima_dengue,
                    enso_dengue, analise_estatistica)

with tab1:
    situacao_atual.render(df, df_filtrado, filtros)
with tab2:
    panorama_historico.render(df, df_filtrado, filtros)
with tab3:
    clima_dengue.render(df, df_filtrado, filtros)
with tab4:
    enso_dengue.render(df, df_filtrado, filtros)
with tab5:
    analise_estatistica.render(df, df_filtrado, filtros)

# ── Educacional (fora das abas) ──────────────────────────────────────────────
st.markdown("---")
with st.expander("🎓 **Tutorial, Exportação e Documentação** — clique para expandir"):
    from pages import educacional_exportacao
    educacional_exportacao.render(df, df_filtrado, filtros)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    f"""<div style='text-align:center; padding:1rem 0;'>
        <strong>🦟 Projeto PIBIC Jr — Monitoramento da Dengue em Petrolina/PE</strong><br>
        <small>
            IFSertãoPE — Campus Petrolina | Curso Técnico em Informática<br>
            Python · Pandas · Plotly · Streamlit · SciPy · Statsmodels<br>
            Dados até: {df['data_iniSE'].max().strftime('%d/%m/%Y')} | Versão 10.0<br>
            ODS 3 (Saúde e Bem-estar) · ODS 4 (Educação de Qualidade) ·
            ODS 9 (Inovação e Infraestrutura)
        </small>
    </div>""",
    unsafe_allow_html=True,
)
