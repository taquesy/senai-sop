
# 📊 Dashboard Financeiro com Streamlit

Este projeto é uma aplicação web simples construída com [Streamlit](https://streamlit.io/) para visualização de dados financeiros a partir de um arquivo CSV real. Ideal para quem deseja praticar análise de dados e construção de dashboards com Python.

---

## 🧾 Funcionalidades

- Leitura de dados financeiros a partir de um arquivo `.csv`
- Limpeza e tratamento de dados monetários
- Visualização da tabela de dados
- Gráfico de barras horizontal com receita total por segmento

---

## 📁 Estrutura do Projeto

```
meu_dashboard_financeiro/
│
├── app.py                    # Código principal da aplicação
├── ms-financial-sample.csv  # Arquivo com os dados financeiros
└── README.md                 # Instruções e documentação
```

---

## ⚙️ Pré-requisitos

Antes de começar, instale:

- [Python 3.10+](https://www.python.org/)
- `pip` (gerenciador de pacotes do Python)

---

## 🧪 Instalação

1. Clone este repositório ou baixe os arquivos para sua máquina.
2. Instale as dependências:

```bash
pip install streamlit pandas matplotlib
```

---

## 📂 Como usar

1. Certifique-se de que o arquivo `ms-financial-sample.csv` está na mesma pasta do `app.py`.

2. Execute o aplicativo com o comando abaixo:

```bash
streamlit run app.py
```

3. O Streamlit abrirá automaticamente no navegador (geralmente em [http://localhost:8501](http://localhost:8501)).

---

## 📄 Estrutura Esperada do CSV

- O arquivo deve estar separado por **ponto e vírgula (`;`)**.
- Deve conter as colunas: `Segment` e `Sales`.
- Exemplo de conteúdo:
```
Segment;Sales
Government;$1.234,56
Midmarket;$3.456,78
Channel Partners;$7.890,00
```

---

## 💻 Código Principal (app.py)

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Financeiro", layout="centered")
st.title("📊 Análise Financeira com Streamlit")
st.write("Aplicação simples com visualização de dados financeiros usando um CSV real.")

df = pd.read_csv("ms-financial-sample.csv", sep=";", on_bad_lines='skip')
df.columns = [col.strip() for col in df.columns]

if 'Sales' in df.columns:
    df["Sales"] = (
        df["Sales"]
        .astype(str)
        .str.strip()
        .str.replace('$', '', regex=False)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
    )

    try:
        df["Sales"] = df["Sales"].astype(float)
    except ValueError as e:
        st.error(f"Erro ao converter coluna 'Sales' para float: {e}")
        st.stop()

st.subheader("📄 Amostra da Tabela")
st.dataframe(df.head())

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
```

---

## 📌 Dicas

- Use o Excel ou o Google Sheets para editar e exportar seu `.csv` com separador `;`.
- Certifique-se de que os valores numéricos estão formatados como string (com `$`, `.` e `,` se aplicável) para simular dados reais.

---

## 🧠 Melhorias Futuras

- Upload dinâmico de arquivos CSV pela interface
- Filtros por data, região ou produto
- Gráficos interativos com Plotly
- Deploy na nuvem (Streamlit Cloud, Heroku etc.)

---

## 📬 Contato

Projeto feito com fins didáticos por Yasmin.
