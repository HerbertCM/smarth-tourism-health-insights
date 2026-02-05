import pandas as pd
import streamlit as st
from dataframes import df_month_tourism, df_state_tourism, df_restaurant, df_weather, df_event_gramado, df_foods

#Função para escolher dataframe para visualização
def choose_dataframe(choice):
    if choice == "Turismo Mensal":
        return df_month_tourism
    elif choice == "Turismo por Estado":
        return df_state_tourism
    elif choice == "Análise de Restaurantes":
        return df_restaurant
    elif choice == "Eventos em Gramado":
        return df_event_gramado
    elif choice == "Pratos":
        return df_foods
    else:
        return df_weather

#Função para filtrar os dataframes
def filter_dataframe(df):
    choice_filter = st.selectbox("Selecione por qual coluna deseja filtrar:", df.columns.to_list())
    choice = st.multiselect(f"Escolha os(as) {choice_filter} para exibir:", df[choice_filter].unique().tolist(), default=df[choice_filter].unique().tolist())
    df_filter = df[df[choice_filter].isin(choice)]

    #Remover coluna
    choice_columns = st.multiselect("Colunas que deseja exibir:", df.columns.tolist(), default=df.columns.tolist())
    df_filter = df_filter[choice_columns]

    return df_filter

def format_num(num):
    format_num = ""
    if num >= 1000000:
        format_num = f"{num/1000000:.2f}" + " Milhão(ões)"
    elif num >= 1000:
        format_num = f"{num/1000:.2f}" + " Mil"
    else:
        format_num = num
    return format_num

def break_items(df, col1, col2, emoji):
    list_col1 = df[col1].tolist()
    list_col2 = df[col2].tolist()
    text = ""
    for x in range(len(list_col1)):
        text += f"{emoji} " + f"{list_col1[x]}" + " - " + f"{list_col2[x]}" + "  \n"
    return text

def list_items(df, col1, col2):
    list_col1 = df[col1].tolist()
    list_col2 = df[col2].tolist()
    text = ""
    cont = 1
    for x in range(len(list_col1)):
        text += f"{cont}° - " + f"{list_col1[x]}" + ": " + f"{format_num(list_col2[x])} Turistas" + "  \n"
        cont += 1
    return text

def plate(caloria):
    calorie_control = {
    "Nome": ["Taxa Metabólica Basal", "Perda em Caminhada (2h)", "Consumo médio Restaurantes Pesquisados", "Teste de Prato"],
    "Caloria": [1600, 400, df_restaurant["Caloria Média dos Pratos"].median(), caloria], #Mediana para tirar valores extremos
    "Representa": ["Perda Calórica", "Perda Calórica", "Ganho Calórico", "Ganho Calórico"]
    }
    df_plate = pd.DataFrame(calorie_control)
    return df_plate

def list_items_br(df, col1, col2):
    list_col1 = df[col1].tolist()
    list_col2 = df[col2].tolist()
    text = ""
    cont = 1
    for x in range(len(list_col1)):
        text += f"{cont}° - " + f"{list_col1[x]}" + ": " + f"{format_num(list_col2[x])} Turistas" + "<br/>"
        cont += 1
    return text