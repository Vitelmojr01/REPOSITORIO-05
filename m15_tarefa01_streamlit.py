import streamlit as st
import pandas as pd
import numpy as np
import time

# Título
st.title("Módulo 15 - Tarefa 01")
st.header("Aplicação Streamlit")
st.subheader("Exemplos de comandos")

# Texto
st.write("Primeira aplicação Streamlit")
st.text("Texto simples")

# Markdown
st.markdown("**Texto em negrito**")
st.markdown("_Texto em itálico_")
st.markdown("### Texto em markdown")
st.markdown("---")

# Link
st.markdown("Acesse o [Google](https://google.com)")

# Emoji
st.markdown("Streamlit é incrível 😎")

# Dataframe
df = pd.DataFrame(
    np.random.randn(10,3),
    columns=['Coluna A','Coluna B','Coluna C']
)

st.dataframe(df)

# Tabela
st.table(df)

# Slider
numero = st.slider("Escolha um número",0,100)

st.write("Número escolhido:",numero)

# Botão
if st.button("Clique aqui"):
    st.write("Botão pressionado!")

# Checkbox
if st.checkbox("Mostrar dataframe"):
    st.write(df)

# Selectbox
opcao = st.selectbox(
    "Escolha uma opção",
    ("Python","Streamlit","EBAC")
)

st.write("Você escolheu:",opcao)

# Multiselect
opcoes = st.multiselect(
    "Escolha linguagens",
    ["Python","R","SQL","Java"]
)

st.write(opcoes)

# Progress bar
st.write("Barra de progresso")

bar = st.progress(0)

for i in range(100):
    bar.progress(i + 1)
    time.sleep(0.01)

# Gráfico linha
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)

st.line_chart(chart_data)

# Mapa
map_data = pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[-23.55,-46.63],
    columns=['lat','lon']
)

st.map(map_data)

# Métrica
st.metric("Temperatura","30 °C","+2 °C")

# Colunas
col1, col2 = st.columns(2)

col1.write("Coluna 1")
col2.write("Coluna 2")

# Mensagens
st.success("Sucesso!")
st.warning("Atenção!")
st.error("Erro!")
st.info("Informação")

# Spinner
with st.spinner("Carregando..."):
    time.sleep(2)

st.success("Carregado!")