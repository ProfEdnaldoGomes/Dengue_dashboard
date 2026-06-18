# config.py
# =============================================================================
# Configurações centrais do Dashboard de Dengue — Petrolina/PE (v10)
# =============================================================================

from pathlib import Path

# ── Caminhos ─────────────────────────────────────────────────────────────────
DATA_DIR = Path("data")
DATASET_FILENAME = "dataset_semanal_petrolina.xlsx"
DATASET_PATH = DATA_DIR / DATASET_FILENAME

# ── Mapeamentos PT-BR ────────────────────────────────────────────────────────
MESES_PT = {
    1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr",
    5: "Mai", 6: "Jun", 7: "Jul", 8: "Ago",
    9: "Set", 10: "Out", 11: "Nov", 12: "Dez",
}
MES_ORDEM = list(MESES_PT.values())

MESES_EXTENSO = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro",
}

# ── Níveis de alerta (InfoDengue) ────────────────────────────────────────────
NIVEL_MAPA = {1: "Verde", 2: "Amarelo", 3: "Laranja", 4: "Vermelho"}
NIVEL_INV = {v: k for k, v in NIVEL_MAPA.items()}

CORES_ALERTA = {
    "Verde":    "#2ecc71",
    "Amarelo":  "#f1c40f",
    "Laranja":  "#e67e22",
    "Vermelho": "#e74c3c",
}

CORES_ALERTA_BG = {
    "Verde":    "rgba(46,204,113,0.12)",
    "Amarelo":  "rgba(241,196,15,0.12)",
    "Laranja":  "rgba(230,126,34,0.12)",
    "Vermelho": "rgba(231,76,60,0.12)",
}

# ── Transmissão / Receptividade ──────────────────────────────────────────────
TRANSMISSAO_MAPA = {0: "Nenhuma", 1: "Possível", 2: "Provável", 3: "Altamente Provável"}
RECEPTIVO_MAPA   = {0: "Desfavorável", 1: "Favorável", 2: "Favorável (2 sem.)", 3: "Favorável (3+ sem.)"}

# ── Estações do ano (hemisfério sul) ─────────────────────────────────────────
ESTACOES = {
    "Verão (Jan–Mar)":     [1, 2, 3],
    "Outono (Abr–Jun)":    [4, 5, 6],
    "Inverno (Jul–Set)":   [7, 8, 9],
    "Primavera (Out–Dez)": [10, 11, 12],
}

ESTACAO_POR_MES = {}
for nome, meses in ESTACOES.items():
    for m in meses:
        ESTACAO_POR_MES[m] = nome

# ── Variáveis climáticas disponíveis ─────────────────────────────────────────
VARS_CLIMA = {
    "Temp (C)":                "Temperatura (°C)",
    "Umid (%)":                "Umidade relativa (%)",
    "Chuva (mm)":              "Precipitação (mm)",
    "Vel. Vento (m/s)":        "Vel. do Vento (m/s)",
    "Pressao (hPa)":           "Pressão Atmosférica (hPa)",
    "Nebulosidade (Decimos)":  "Nebulosidade (décimos)",
    "Insolacao (h)":           "Insolação (horas)",
}
VARS_CLIMA_KEYS = list(VARS_CLIMA.keys())

# Variáveis climáticas nucleares (usadas nos testes avançados)
VARS_CLIMA_NUCLEARES = ["Temp (C)", "Umid (%)", "Chuva (mm)", "Pressao (hPa)", "Vel. Vento (m/s)"]

# ── Paleta de cores (ColorBrewer Safe) ───────────────────────────────────────
PALETA = {
    "primaria":   "#1b9e77",
    "secundaria": "#d95f02",
    "terciaria":  "#7570b3",
    "destaque":   "#e7298a",
    "info":       "#66a61e",
    "neutro":     "#666666",
    "fundo":      "#fafafa",
}

# Cores ENSO
COR_NINO = "#FF6F00"
COR_NINA = "#1565C0"
COR_NEUT = "#9E9E9E"

# ── Plotly defaults ──────────────────────────────────────────────────────────
PLOTLY_TEMPLATE = "plotly_white"
PLOTLY_FONT = dict(family="Source Sans Pro, Segoe UI, sans-serif", size=13)
CHART_HEIGHT_SM = 350
CHART_HEIGHT_MD = 480
CHART_HEIGHT_LG = 650

# ── Parâmetros de Análise Avançada ───────────────────────────────────────────
ALPHA = 0.05
MAX_LAG_CCF = 12          # semanas
MAX_LAG_GRANGER = 8       # semanas
N_BOOT_CCF = 1000         # permutações bootstrap para CCF
ROLLING_WINDOW = 52       # semanas (1 ano)
STL_PERIOD = 52           # sazonalidade semanal

# ── Dados ONI (NOAA/CPC ERSSTv5) ────────────────────────────────────────────
# FONTE: NOAA Climate Prediction Center (CPC)
# URL: https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php
# DATASET: ERSSTv5 Oceanic Niño Index (ONI)
# DEFINIÇÃO: Média móvel trimestral das anomalias SST na região Niño 3.4
# DATA DE CONSULTA: 14 de abril de 2026
# NOTA: Cada linha = 1 ano; 12 colunas = estações DJF→NDJ; mês central = Jan→Dez.
ONI_DATA = {
    2010: [ 1.5,  1.2,  0.8,  0.4, -0.2, -0.7, -1.0, -1.3, -1.6, -1.6, -1.6, -1.5],
    2011: [-1.3, -1.0, -0.8, -0.6, -0.5, -0.4, -0.4, -0.6, -0.8, -1.0, -1.0, -0.9],
    2012: [-0.7, -0.6, -0.5, -0.4, -0.2,  0.1,  0.3,  0.4,  0.4,  0.3,  0.1, -0.1],
    2013: [-0.3, -0.3, -0.2, -0.2, -0.3, -0.3, -0.4, -0.3, -0.2, -0.1, -0.1, -0.2],
    2014: [-0.3, -0.3, -0.1,  0.2,  0.3,  0.2,  0.1,  0.1,  0.3,  0.5,  0.7,  0.8],
    2015: [ 0.7,  0.6,  0.7,  0.8,  1.0,  1.3,  1.6,  1.9,  2.2,  2.5,  2.6,  2.8],
    2016: [ 2.6,  2.3,  1.7,  1.0,  0.5,  0.0, -0.3, -0.5, -0.6, -0.6, -0.6, -0.5],
    2017: [-0.2,  0.0,  0.2,  0.3,  0.4,  0.4,  0.2, -0.1, -0.3, -0.6, -0.8, -0.9],
    2018: [-0.8, -0.7, -0.6, -0.4, -0.1,  0.1,  0.1,  0.3,  0.5,  0.8,  1.0,  0.9],
    2019: [ 0.9,  0.9,  0.8,  0.8,  0.6,  0.5,  0.3,  0.2,  0.2,  0.4,  0.6,  0.7],
    2020: [ 0.6,  0.6,  0.5,  0.3,  0.0, -0.2, -0.4, -0.5, -0.8, -1.1, -1.2, -1.1],
    2021: [-0.9, -0.8, -0.7, -0.5, -0.4, -0.3, -0.3, -0.4, -0.6, -0.8, -0.9, -0.9],
    2022: [-0.8, -0.8, -0.9, -1.0, -0.9, -0.8, -0.8, -0.9, -1.0, -0.9, -0.8, -0.7],
    2023: [-0.5, -0.3,  0.0,  0.3,  0.6,  0.8,  1.1,  1.4,  1.6,  1.8,  2.0,  2.1],
    2024: [ 1.9,  1.6,  1.3,  0.8,  0.5,  0.2,  0.1, -0.1, -0.2, -0.2, -0.3, -0.4],
    2025: [-0.5, -0.5, -0.3, -0.2,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    # 2025: valores estimados Jan-Mai; Jun-Dez placeholder neutro
}
