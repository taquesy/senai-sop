import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Dashboard Financeiro", layout="centered")

st.title("📊 Análise Financeira com Streamlit")
st.write("Aplicação simples com visualização de dados financeiros usando um CSV real.")

# Leitura do CSV com separador correto
df = pd.read_csv("ms-financial-sample.csv", sep=";", on_bad_lines='skip')
df.columns = [col.strip() for col in df.columns]  # Remove espaços nos nomes das colunas

# Tratamento da coluna 'Sales' para conversão correta
if 'Sales' in df.columns:
    df["Sales"] = (
        df["Sales"]
        .astype(str)
        .str.strip()
        .str.replace('$', '', regex=False)  # Remove o símbolo $
        .str.replace('.', '', regex=False)  # Remove pontos (milhar)
        .str.replace(',', '.', regex=False)  # Troca vírgula decimal por ponto
    )

    # Tenta converter em float
    try:
        df["Sales"] = df["Sales"].astype(float)
    except ValueError as e:
        st.error(f"Erro ao converter coluna 'Sales' para float: {e}")
        st.stop()

# Visualização da tabela
st.subheader("📄 Amostra da Tabela")
st.dataframe(df.head())

# Agrupamento por segmento e soma das vendas
if 'Segment' in df.columns and 'Sales' in df.columns:
    st.subheader("📈 Receita Total por Segmento")
    revenue_by_segment = df.groupby("Segment")["Sales"].sum().sort_values()

    fig, ax = plt.subplots()
    revenue_by_segment.plot(kind="barh", ax=ax)
    ax.set_xlabel("Receita")
    ax.set_ylabel("Segmento")
    st.pyplot(fig)
else:
    st.warning("As colunas 'Segment' e 'Sales' não foram encontradas.")
