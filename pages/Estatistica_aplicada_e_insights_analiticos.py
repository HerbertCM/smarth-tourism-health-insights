import streamlit as st
from graphics import grp_weather_tourism, grp_turism_event, graphics_bar
from dataframes import df_month_tourism, df_tourism_event, df_calorie_control, df_foods
from functions import format_num, list_items, plate

st.set_page_config(layout="wide")
st.title("Estatística Inteligênte")
st.markdown("'Testes estatísticos e hipóteses avaliadas, ferramenta interativa para análise de cenários e comparação de consumo.'")
st.markdown("<br>" * 2, unsafe_allow_html=True)

abs1, abs2 = st.tabs(["Turismo, Clima e Eventos", "Alimentação e Saúde"])

with abs1:
    ## Criando Título
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("<h2>❄️Turismo e Clima</h2>", unsafe_allow_html=True)
    st.markdown("<br>" * 2, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    #Pegar mês com maior fluxo turistico
    with col1:
        st.markdown("<h3>Mês com Maior Fluxo Turístico:</h3>", unsafe_allow_html=True)
        st.markdown(f"<h5>✈️ {df_month_tourism[df_month_tourism["Tourism"] == df_month_tourism["Tourism"].max()]["Month_name"].iloc[0]}: aproximadamente {format_num(df_month_tourism["Tourism"].max())} Turistas</h5>", unsafe_allow_html=True)
    #Pegar mês com menor fluxo turístico
    with col2:
        st.markdown("<h3>Mês com Menor Fluxo Turístico:</h3>", unsafe_allow_html=True)
        st.markdown(f"<h5>✈️ {df_month_tourism[df_month_tourism["Tourism"] == df_month_tourism["Tourism"].min()]["Month_name"].iloc[0]}: aproximadamente {format_num(df_month_tourism["Tourism"].min())} Turistas</h5>", unsafe_allow_html=True)
    #Colocar gréfico e espaçamento
    st.markdown("<br>", unsafe_allow_html=True)
    st.plotly_chart(grp_weather_tourism)

    col1, col2 = st.columns(2)
    #Criar um top 5 com meses com mais e menos turistas
    with col1:
        st.markdown("<h3>Top 5 Meses com maior Fluxo Turístico:</h3>", unsafe_allow_html=True)
        st.markdown(f"{list_items(df_month_tourism.sort_values("Tourism", ascending=False).head(5), "Month_name", "Tourism")}")
    with col2:
        st.markdown("<h3>Top 5 Meses com menor Fluxo Turístico:</h3>", unsafe_allow_html=True)
        st.markdown(f"{list_items(df_month_tourism.sort_values("Tourism", ascending=True).head(5), "Month_name", "Tourism")}")
    #Criar um título, com espaçamentos
    st.markdown("<br>" * 2, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("<h2>🥳Turismo e Eventos</h2>", unsafe_allow_html=True)
    st.markdown("<br>" * 2, unsafe_allow_html=True)
    #Criar eventos com mais e menos fluxo turístico
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3>Evento com maior Fluxo Turístico:</h3>", unsafe_allow_html=True)
        st.markdown(f"<h5>🎉 {df_tourism_event.groupby("Name", as_index=False)["Tourism"].sum().sort_values("Tourism", ascending=False).iloc[0]["Name"]}", unsafe_allow_html=True)
    with col2:
        st.markdown("<h3>Evento com menor Fluxo Turístico:</h3>", unsafe_allow_html=True)
        st.markdown(f"<h5>🎉 {df_tourism_event.groupby("Name", as_index=False)["Tourism"].sum().sort_values("Tourism", ascending=True).iloc[0]["Name"]}", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.plotly_chart(grp_turism_event)
    #Criar um top 5 de eventos que mais movimentam a cidade
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3>Top 3 Eventos que mais Atraem Turistas:</h3>", unsafe_allow_html=True)
        st.markdown(f"{list_items(df_tourism_event.groupby("Name", as_index=False)["Tourism"].sum().sort_values("Tourism", ascending=False).head(3), "Name", "Tourism")}")
    with col2:
        st.markdown("<h3>Top 3 Eventos que menos Atraem Turistas:</h3>", unsafe_allow_html=True)
        st.markdown(f"{list_items(df_tourism_event.groupby("Name", as_index=True)["Tourism"].sum().sort_values(ascending=True).reset_index().head(3), "Name", "Tourism")}")

## Saude e Alimentação ##
with abs2:
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("<h2>🥬 Consumo Calórico</h2>", unsafe_allow_html=True)
        st.markdown("<br>" * 2, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3>Insights Calorias:</h3>", unsafe_allow_html=True)
        st.markdown(
        f"🫕 Consumo médio Calórico (Restaurantes Analisados): "
        f"{df_calorie_control[df_calorie_control['Representa'] == 'Ganho Calórico']['Caloria'].sum()} Calorias<br>"
        f"🥵 Perda Calórica: "
        f"{df_calorie_control[df_calorie_control['Representa'] == 'Perda Calórica']['Caloria'].sum()} Calorias<br>"
        f"🥗 Consumo Calórico Recomendado (Resto do dia): "
        f"{df_calorie_control[df_calorie_control['Representa'] == 'Perda Calórica']['Caloria'].sum()
        - df_calorie_control[df_calorie_control['Representa'] == 'Ganho Calórico']['Caloria'].sum()} Calorias",
        unsafe_allow_html=True)
    st.plotly_chart(graphics_bar(df_calorie_control, "Nome", "Caloria" , "Ganho e Perda Calórica", "Representa", {"Ganho Calórico": "#d44444", "Perda Calórica": "#4168db"}))

    st.markdown("<br>" * 2, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("<h2>💡 Testando Pratos</h2>", unsafe_allow_html=True)
    st.markdown("<br>" * 2, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3>Teste de Pratos:</h3>", unsafe_allow_html=True)
        refeicao = st.selectbox("Selecione a Refeição:", df_foods["Refeição"].to_list())
        sobremesa = st.selectbox("Selecione a Sobremesa", df_foods["Sobremesas"].to_list())
        soma_caloria = df_foods[df_foods["Refeição"] == refeicao]["Calorias Refeição"].iloc[0] +  df_foods[df_foods["Sobremesas"] == sobremesa]["Calorias Sobremesa"].iloc[0]
        text = "Total de Calorias: "
        if soma_caloria <= 500:
            text += f"<span style='color: green;'>{soma_caloria}</span>"
        elif soma_caloria < 600:
            text += f"<span style='color: yellow;'>{soma_caloria}</span>"
        else:
            text += f"<span style='color: red;'>{soma_caloria}</span>"
        st.markdown(text, unsafe_allow_html=True)
    with col2:
        st.markdown("<h3>Insight Sobre Prato Testado:</h3>", unsafe_allow_html=True)
        caloria_comparacao = (df_calorie_control[df_calorie_control['Representa'] == 'Perda Calórica']['Caloria'].sum() - df_calorie_control[df_calorie_control['Representa'] == 'Ganho Calórico']['Caloria'].sum()) - soma_caloria

        if caloria_comparacao <= -100:
            st.markdown(f"🍔 Consumo calórico de <span style='color: red;'>{caloria_comparacao  * -1}</span> Calorias acima do Recomendado", unsafe_allow_html=True)
        elif caloria_comparacao < 0:
            st.markdown(f"🍗 Consumo calórico de <span style='color: yellow;'>{caloria_comparacao * -1}</span> Calorias acima do Recomendado, porém ainda considerado Saudável", unsafe_allow_html=True)
        else:
            st.markdown(f"🥗 Consumo calórico de <span style='color: green;'>{caloria_comparacao}</span> Calorias abaixo do Recomendado, considerado Saudável", unsafe_allow_html=True)

    st.plotly_chart(graphics_bar(plate(soma_caloria), "Nome", "Caloria" , "Ganho e Perda Calórica", "Representa", {"Ganho Calórico": "#d44444", "Perda Calórica": "#4168db"}))