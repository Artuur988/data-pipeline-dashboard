import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

# ===== CONFIG PAGE =====
st.set_page_config(page_title="Dashboard de Produtos", layout="wide")

# ===== LOAD DATA =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "data", "dados.db")
engine = create_engine(f"sqlite:///{db_path}")

df = pd.read_sql("SELECT * FROM produtos", engine)

# ===== TRADUÇÃO (TEM QUE VIR ANTES DE USAR) =====
mapa_categorias = {
    "men's clothing": "Roupas Masculinas",
    "women's clothing": "Roupas Femininas",
    "jewelery": "Joias",
    "electronics": "Eletrônicos"
}

df['categoria_pt'] = df['category'].map(mapa_categorias).fillna(df['category'])

# ===== SIDEBAR FILTROS =====
st.sidebar.header("Filtros")

categorias = st.sidebar.multiselect(
    "Categoria",
    options=df['categoria_pt'].unique(),
    default=df['categoria_pt'].unique()
)

preco_min, preco_max = st.sidebar.slider(
    "Faixa de preço",
    float(df['price'].min()),
    float(df['price'].max()),
    (float(df['price'].min()), float(df['price'].max()))
)

# ===== FILTRAGEM =====
df_filtrado = df[
    (df['categoria_pt'].isin(categorias)) &
    (df['price'] >= preco_min) &
    (df['price'] <= preco_max)
]

# ===== HEADER =====
st.title("📊 Dashboard de Análise de Produtos")
st.markdown("Análise interativa de preços e categorias")

# ===== KPIs =====
col1, col2, col3 = st.columns(3)

col1.metric("Preço médio", f"{df_filtrado['price'].mean():.2f}")
col2.metric("Total de produtos", df_filtrado.shape[0])
col3.metric("Preço máximo", f"{df_filtrado['price'].max():.2f}")

# ===== GRÁFICOS =====
col4, col5 = st.columns(2)

with col4:
    st.subheader("Preço médio por categoria")
    st.bar_chart(df_filtrado.groupby('categoria_pt')['price'].mean())

with col5:
    st.subheader("Distribuição de preços")
    st.line_chart(df_filtrado['price'])

# ===== TABELA =====
st.subheader("Produtos")
st.dataframe(df_filtrado.sort_values(by='price', ascending=False))

# ===== MÉTRICAS EXTRAS =====
st.subheader("Estoque médio")
st.write(df_filtrado['estoque'].mean())

st.subheader("Desconto médio")
st.write(df_filtrado['desconto'].mean())