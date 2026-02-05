import pandas as pd
import streamlit as st
from dataframes import df_month_tourism, df_state_tourism, df_weather, df_restaurant, df_event_gramado, df_foods
from functions import choose_dataframe, filter_dataframe

st.title("Vizualização dos DataFrames")
st.markdown("'Transparência sobre origem, estrutura e distribuição dos dados utilizados no projeto.'")
st.set_page_config(layout="wide")

choice_DataFrame = ["Turismo Mensal", "Turismo por Estado", "Análise de Restaurantes", "Clima", "Eventos em Gramado", "Pratos"]

option = st.selectbox("Escolha o DataFrame para a Visualização", choice_DataFrame)
df_choice = choose_dataframe(option)


## Filtar dataframes com função ##
if option == "Turismo Mensal":
    df_filter = filter_dataframe(df_month_tourism)

elif option == "Turismo por Estado":
    df_filter = filter_dataframe(df_state_tourism)

elif option == "Análise de Restaurantes":
    df_filter = filter_dataframe(df_restaurant)

elif option == "Clima":
    df_filter = filter_dataframe(df_weather)

elif option == "Eventos em Gramado":
    df_filter = filter_dataframe(df_event_gramado)
elif option == "Pratos":
    df_filter = filter_dataframe(df_foods)

st.dataframe(df_filter)