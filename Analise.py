import streamlit as st
import pandas as pd
import plotly.express as px

# ⚙️ Configuração opcional da página para usar todo o espaço da tela
st.set_page_config(page_title="Dashboard de Notebooks", layout="wide")

# Carregando os dados
# Usamos o @st.cache_data para não precisar recarregar o Excel toda vez que clicamos em um filtro
@st.cache_data
def carregar_dados():
    return pd.read_excel("Dados.xlsx")

dados = carregar_dados()

# --- CABEÇALHO ---
st.title("📊 Análise de Dados - Dashboard")

st.subheader("Comparativo dos principais notebooks vendidos no Mercado Livre")

st.write("Quantidade de empresas analisadas:", dados["FABRICANTE"].nunique())


# --- SIDEBAR (MENU LATERAL) ---
st.sidebar.title("🔍 Filtros")

# Filtro 1: Empresas (O que você já tinha feito)
fabricantes = st.sidebar.multiselect(
    "Empresas",
    dados["FABRICANTE"].unique()
)

# Filtro 2: Controle deslizante (Slider) para Quantidade
min_qtd = int(dados["QUANTIDADE"].min())
max_qtd = int(dados["QUANTIDADE"].max())

faixa_qtd = st.sidebar.slider(
    "📦 Filtrar por Quantidade Vendida",
    min_value=min_qtd,
    max_value=max_qtd,
    value=(min_qtd, max_qtd)
)

# Aplicando os filtros aos dados
dados_filtrados = dados.copy()

if fabricantes:
    dados_filtrados = dados_filtrados[dados_filtrados["FABRICANTE"].isin(fabricantes)]

dados_filtrados = dados_filtrados[
    dados_filtrados["QUANTIDADE"].between(faixa_qtd[0], faixa_qtd[1])
]

# Botão de Download na Sidebar
@st.cache_data
def converter_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = converter_df(dados_filtrados)
st.sidebar.markdown("---") # Linha divisória
st.sidebar.download_button(
    label="📥 Baixar Dados Filtrados (CSV)",
    data=csv,
    file_name='dados_notebooks.csv',
    mime='text/csv',
)


# --- MÉTRICAS (Lado a Lado em Colunas) ---
col1, col2, col3 = st.columns(3)

col1.metric(
    "TOTAL RECEITA BRUTA",
    f"R$ {dados_filtrados['TOTAL'].sum():,.2f}"
)

col2.metric(
    "MÉDIA RECEITA BRUTA",
    f"R$ {dados_filtrados['TOTAL'].mean():,.2f}"
)

if not dados_filtrados.empty:
    mais_vendido = dados_filtrados.loc[dados_filtrados["QUANTIDADE"].idxmax()]
    col3.metric("🏆 Produto Mais Vendido", str(mais_vendido["PRODUTO"]))
else:
    col3.warning("Nenhum produto no filtro.")


st.markdown("---") # Linha divisória para separar as métricas do resto


# --- ABAS DE ORGANIZAÇÃO (Tabs) ---
aba_graficos, aba_dados = st.tabs(["📈 Gráficos Interativos", "📋 Tabela de Dados e Ranking"])

# ABA 1: GRÁFICOS
with aba_graficos:
    if not dados_filtrados.empty:
        st.subheader("💰 Receita por Fabricante")
        
        # Gráfico de barras com Plotly
        df_agrupado_soma = dados_filtrados.groupby("FABRICANTE", as_index=False)["TOTAL"].sum()
        fig_receita = px.bar(
            df_agrupado_soma,
            x="FABRICANTE", 
            y="TOTAL", 
            color="FABRICANTE",
            text_auto='.2s',
            labels={"TOTAL": "Receita Total (R$)", "FABRICANTE": "Fabricante"}
        )
        st.plotly_chart(fig_receita, use_container_width=True)

        st.subheader("📈 Média de Receita por Fabricante")
        
        # Gráfico de linhas com Plotly
        df_agrupado_media = dados_filtrados.groupby("FABRICANTE", as_index=False)["TOTAL"].mean()
        fig_media = px.line(
            df_agrupado_media,
            x="FABRICANTE",
            y="TOTAL",
            markers=True,
            labels={"TOTAL": "Média de Receita (R$)", "FABRICANTE": "Fabricante"}
        )
        st.plotly_chart(fig_media, use_container_width=True)
    else:
        st.info("Ajuste os filtros para visualizar os gráficos.")

# ABA 2: DADOS
with aba_dados:
    st.subheader("🥇 Ranking das Empresas TOP ONE (Por Receita)")
    
    if not dados_filtrados.empty:
        # Reset_index() deixa a visualização mais bonita no dataframe do Streamlit
        ranking = (
            dados_filtrados
            .groupby("FABRICANTE")["TOTAL"]
            .sum()
            .sort_values(ascending=False)
            .reset_index() 
        )
        st.dataframe(ranking, use_container_width=True)
        
        # Bônus: Mostrar a tabela completa filtrada caso o usuário queira investigar
        st.subheader("🔍 Tabela de Dados Completa (Filtrada)")
        st.dataframe(dados_filtrados, use_container_width=True)
    else:
        st.warning("Nenhum dado encontrado com os filtros atuais.")