# 🦟 Dashboard de Monitoramento da Dengue — Petrolina/PE (v10)

**Projeto PIBIC Jr — IFSertãoPE Campus Petrolina**

Dashboard interativo para análise exploratória avançada e monitoramento
epidemiológico da dengue em Petrolina-PE (2010–2025), integrando dados do
InfoDengue/SINAN, INMET e NOAA (ENSO/ONI).

---

## 🚀 Como executar

```bash
# 1. Clone ou copie o projeto
cd dashboard_v10

# 2. Crie um ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Coloque o dataset na pasta data/
mkdir -p data
cp /caminho/para/dataset_semanal_petrolina.xlsx data/

# 5. Execute
streamlit run app.py
```

---

## 📁 Estrutura do Projeto

```
dashboard_v10/
├── app.py                        # Orquestrador — 5 abas + educacional
├── config.py                     # Constantes, ONI, parâmetros de análise
├── requirements.txt              # Dependências Python
├── data/
│   └── dataset_semanal_petrolina.xlsx
├── utils/
│   ├── __init__.py
│   ├── data_loader.py            # Carga, merge ONI, feature engineering
│   ├── eda_avancada.py           # STL, ADF/KPSS, CCF bootstrap, Granger FDR,
│   │                             # VIF, corr parcial, MI, Rolling Spearman
│   ├── metricas.py               # KPIs, tendências, comparativos
│   └── export.py                 # Exportação Excel/relatórios
├── components/
│   ├── __init__.py
│   ├── charts.py                 # Gráficos Plotly (STL, CCF, Granger, ENSO…)
│   └── layout.py                 # CSS, sidebar, KPI cards
└── pages/
    ├── __init__.py
    ├── situacao_atual.py          # Painel de situação (landing)
    ├── panorama_historico.py      # Evolução temporal + STL
    ├── clima_dengue.py            # CCF bootstrap, Granger, VIF, MI, corr parcial
    ├── enso_dengue.py             # ONI, boxplots, Kruskal-Wallis, estratificação
    ├── analise_estatistica.py     # Rolling Spearman, estacionariedade, outliers
    └── educacional_exportacao.py  # Tutorial, quiz, glossário, exportação
```

---

## 📊 Funcionalidades

### 🏠 Situação Atual
KPIs, gauge de P(Rt>1), tendência 4 semanas, comparativo anual, sparklines, heatmap 52 semanas.

### 📈 Panorama Histórico
Série temporal, evolução anual, **decomposição STL** (tendência + sazonalidade + resíduo),
heatmap meses × anos, comparação entre anos.

### 🌡️ Clima × Dengue
- **CCF Bootstrap** (1.000 permutações): lag ótimo com IC 95%
- **Causalidade de Granger** (seleção BIC + FDR Benjamini-Hochberg)
- **VIF**: diagnóstico de colinearidade
- **Correlação parcial**: efeitos independentes
- **Informação Mútua**: dependências não-lineares

### 🌊 ENSO e Dengue
- Timeline ONI (NOAA/CPC ERSSTv5)
- Boxplots por fase e intensidade ENSO
- Kruskal-Wallis + Mann-Whitney par-a-par
- Correlações estratificadas por fase ENSO (heatmap)
- Perfil sazonal por fase ENSO

### 📊 Análise Estatística
- **Rolling Spearman** (janela 52 semanas)
- Testes ADF + KPSS com conclusão automática
- Matriz de correlação
- Detecção de outliers (IQR, Z-Score, Percentil)
- Estatísticas descritivas com CV
- Indicador de completude

### 🎓 Educacional
Tutorial com 8 métodos, quiz de 5 perguntas, glossário técnico, exportação CSV/Excel/JSON/relatório.

---

## 🔄 Changelog v9 → v10

### Removido
- **Modelagem ML**: Regressão Linear, Polinomial, Random Forest
- Validação cruzada temporal (TimeSeriesSplit)
- Baseline ingênuo, diagnóstico de resíduos

### Adicionado
- Decomposição STL (period=52)
- CCF com IC bootstrap (1.000 permutações circulares)
- Causalidade de Granger (FDR-BH) com diferenciação automática
- VIF entre variáveis climáticas
- Correlação parcial (Chuva controlando Temp e vice-versa)
- Informação Mútua (sklearn)
- Rolling Spearman (janela 52 semanas)
- Aba ENSO completa (ONI, boxplots, Kruskal-Wallis, Mann-Whitney, estratificação)
- Testes de estacionariedade (ADF + KPSS) combinados
- Tutorial e quiz atualizados com novos métodos

### Justificativa
A modelagem preditiva (Random Forest etc.) foi substituída por EDA avançada
porque: (a) o R² com apenas variáveis climáticas seria baixo e pouco
publicável; (b) o ferramental de ML exigiria discussão de hiperparâmetros
que extrapola o escopo do PIBIC Jr; (c) a EDA avançada (Granger, STL,
ENSO) produz achados publicáveis em periódicos B1/B2 brasileiros.

---

## 📚 Referências

- InfoDengue: https://info.dengue.mat.br
- INMET: https://portal.inmet.gov.br
- NOAA/CPC ONI: https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php
- Granger, C.W.J. (1969). Investigating causal relations by econometric models
- Cleveland et al. (1990). STL: A seasonal-trend decomposition procedure
- Benjamini, Y. & Hochberg, Y. (1995). Controlling the false discovery rate

---

## 📄 Licença

Projeto acadêmico — PIBIC Jr, IFSertãoPE Campus Petrolina.

**ODS 3** (Saúde e Bem-estar) · **ODS 4** (Educação de Qualidade) ·
**ODS 9** (Inovação e Infraestrutura)
