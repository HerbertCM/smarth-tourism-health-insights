import streamlit as st
from graphics import graphics_line, graphics_bar, graphics_pie
from dataframes import df_weather, df_month_tourism, df_state_tourism, df_restaurant, df_event_gramado
from functions import format_num, break_items

st.set_page_config(layout="wide")
st.title("Dados Tratados")
st.markdown("'Visão consolidada dos principais indicadores turísticos e climáticos, indicadores exploratórios de consumo, atividade física e eventos locais.'")

abs1, abs2 = st.tabs(["Clima e Turismo", "Eventos e Saúde"])

with abs1:
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("<br>" * 1, unsafe_allow_html=True)
        st.metric("Total de Turistas que Visitaram Gramado em 2025:", format_num(df_month_tourism["Tourism"].sum()))
        st.markdown("<br>" * 2, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(graphics_line(df_weather, df_weather["Month_name"], df_weather["TEMPERATURA MEDIA, DIARIA (AUT)(°C)"], "Média de Temperatura Mensal em Gramado no ano de 2025"))
        st.markdown("<br>" * 4, unsafe_allow_html=True)
        st.metric("Estado com Maior Origem de Turistas", f"{df_state_tourism[df_state_tourism["Tourism"] == df_state_tourism["Tourism"].max()]["State"].iloc[0]}")
        st.plotly_chart(graphics_bar(df_state_tourism, df_state_tourism["State"], df_state_tourism["Tourism"], "Estado de Origem dos Turistas que Visitam Gramado no ano de 2025"))
    with col2:
        st.plotly_chart(graphics_line(df_month_tourism, df_month_tourism["Month_name"], df_month_tourism["Tourism"], "Fluxo Mensal de Turistas para Gramado no ano de 2025"))
        st.markdown("<br>" * 4, unsafe_allow_html=True)
        st.metric("Estado com Menor Origem de Turistas", f"{df_state_tourism[df_state_tourism["Tourism"] == df_state_tourism["Tourism"].min()]["State"].iloc[0]}")
        st.plotly_chart(graphics_pie(df_state_tourism, df_state_tourism["Tourism"], df_state_tourism["State"], "Porcentagem da Origem dos Turistas que Visitam Gramado no ano de 2025"))

with abs2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3>Quantidade de Avaliaçoes dos Restaurantes Analisados:</h3>", unsafe_allow_html=True)
        st.markdown(break_items(df_restaurant, "Restaurantes", "Avaliações", "⭐"))
        st.markdown("<br>" * 2, unsafe_allow_html=True)
        st.markdown("<h3>Eventos Gramado em 2025:</h3>", unsafe_allow_html=True)
        st.markdown(break_items(df_event_gramado, "Month_name", "Name", "🎉"))
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3>Pratos Principais dos Restaurantes Analisados:</h3>", unsafe_allow_html=True)
        st.markdown(break_items(df_restaurant, "Restaurantes", "Pratos Principais", "🥣"))
        st.markdown("<br>" * 2, unsafe_allow_html=True)
        st.markdown("<h3>Atividade física mais praticada por Turistas em Gramado:</h3>", unsafe_allow_html=True)
        st.markdown("🚶 Caminhada, queima de aproximadamente 400 calorias diária")
    st.markdown("<br>", unsafe_allow_html=True)
    st.plotly_chart(graphics_bar(df_restaurant, df_restaurant["Restaurantes"], df_restaurant["Caloria Média dos Pratos"], "Caloria Média Consumida nos Restaurantes Analisados"))