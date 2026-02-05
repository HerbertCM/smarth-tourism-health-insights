from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Image,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from graphics import grp_turism_event, grp_weather_tourism, graphics_line, graphics_bar
from dataframes import df_month_tourism, df_weather, df_state_tourism, df_restaurant, df_event_gramado, df_tourism_event, df_calorie_control, df_weather_tourism
from functions import format_num, break_items, list_items, plate, list_items_br
from pages.Estatistica_aplicada_e_insights_analiticos import caloria_comparacao, soma_caloria, refeicao, sobremesa
import streamlit as st
import time

st.set_page_config(layout="wide")
st.title("Relatório Automático")
st.markdown("<br><h3>Gerar Relatório automático com Dados de Gramado:</h3>", unsafe_allow_html=True)

if st.button("Gerar Relatório"):
    placeholder = st.empty()
    placeholder.info("Aguarde! Gerando Relatório...")

    #Criar pdf
    doc = SimpleDocTemplate(
        "relatorio/Relatorio_Gramado.pdf",
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    #Criar estilo próprio, existe os pré-determinados(Title, Heading1, Heading2, Normal)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Insight",
        fontSize=11,
        textColor=colors.darkgreen,
        spaceAfter=12
    ))

    #Inserir texto, aceita htlm básico se assim quiser
    elements = []
    elements.append(Paragraph(
        "<b>Período analisado:</b> Janeiro a Dezembro de 2025<br/>"
        "<b>Cidade:</b> Gramado – RS",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))

    ##Dados Tratados
    elements.append(Paragraph(
        "Clima e Turismo",
        styles["Title"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Total de Turistas que Visitaram Gramado em 2025</b>: {format_num(df_month_tourism["Tourism"].sum())}",
        styles["Normal"]
    ))
    graphics_line(df_weather, df_weather["Month_name"], df_weather["TEMPERATURA MEDIA, DIARIA (AUT)(°C)"], "Média de Temperatura Mensal em Gramado no ano de 2025").write_image(
        "imagens/grafico_clima.png",
        width=1200,
        height=600
    )
    elements.append(Image(
        "imagens/grafico_clima.png",
        width=400,
        height=250
    ))
    graphics_line(df_month_tourism, df_month_tourism["Month_name"], df_month_tourism["Tourism"], "Fluxo Mensal de Turistas para Gramado no ano de 2025").write_image(
        "imagens/grafico_turismo.png",
        width=1200,
        height=600
    )
    elements.append(Image(
        "imagens/grafico_turismo.png",
        width=400,
        height=250
    ))
    elements.append(Paragraph(
        f"<b>Estado com maior Origem de Turistas</b>: {df_state_tourism[df_state_tourism["Tourism"] == df_state_tourism["Tourism"].max()]["State"].iloc[0]}",
        styles["Normal"]
    ))
    elements.append(Paragraph(
        f"<b>Estado com menor Origem de Turistas</b>: {df_state_tourism[df_state_tourism["Tourism"] == df_state_tourism["Tourism"].min()]["State"].iloc[0]}",
        styles["Normal"]
    ))
    graphics_bar(df_state_tourism, df_state_tourism["State"], df_state_tourism["Tourism"], "Estado de Origem dos Turistas que Visitam Gramado no ano de 2025").write_image(
        "imagens/grafico_estado.png",
        width=1200,
        height=600
    )
    elements.append(Image(
        "imagens/grafico_estado.png",
        width=400,
        height=250
    ))
    elements.append(Spacer(1, 20))

    ##Evento e Saúde
    elements.append(Paragraph(
        "Eventos e Saúde",
        styles["Title"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        "<b>Quantidade de Avaliações dos Restaurantes Analisados</b>:",
        styles["Normal"]
    ))
    elements.append(Paragraph(
        break_items(df_restaurant, "Restaurantes", "Avaliações", "<br/>"),
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        "<b>Pratos principais dos Restaurantes Analisados</b>:",
        styles["Normal"]
    ))
    elements.append(Paragraph(
        break_items(df_restaurant, "Restaurantes", "Pratos Principais", "<br/>"),
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        "<b>Eventos Gramado em 2025</b>:",
        styles["Normal"]
    ))
    elements.append(Paragraph(
        break_items(df_event_gramado, "Month_name", "Name", "<br/>"),
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        "<b>Atividade física mais praticada por Turistas em Gramado</b>:<br/>"
        "Caminhada, queima de aproximadamente 400 calorias diária",
        styles["Normal"]
    ))
    graphics_bar(df_restaurant, df_restaurant["Restaurantes"], df_restaurant["Caloria Média dos Pratos"], "Caloria Média Consumida nos Restaurantes Analisados").write_image(
        "imagens/grafico_restaurante.png",
        width=1200,
        height=600,
        scale=2
    )
    elements.append(Image(
        "imagens/grafico_restaurante.png",
        width=400,
        height=250
    ))
    elements.append(Spacer(1, 20))

    ##Turismo, Clima e Eventos
    elements.append(Paragraph(
        "Relação entre Turismo e Clima.",
        styles["Title"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Mês com maior Fluxo Turístico</b>:<br/>{df_month_tourism[df_month_tourism["Tourism"] == df_month_tourism["Tourism"].max()]["Month_name"].iloc[0]}: aproximadamente {format_num(df_month_tourism["Tourism"].max())} Turistas.",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Mês com menor Fluxo Turístico</b>:<br/>{df_month_tourism[df_month_tourism["Tourism"] == df_month_tourism["Tourism"].min()]["Month_name"].iloc[0]}: aproximadamente {format_num(df_month_tourism["Tourism"].min())} Turistas.",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Top 5 Meses com maior Fluxo Turístico</b>:<br/>{list_items_br(df_month_tourism.sort_values("Tourism", ascending=False).head(5), "Month_name", "Tourism")}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Top 5 Meses com menor Fluxo Turístico</b>:<br/>{list_items_br(df_month_tourism.sort_values("Tourism", ascending=True).head(5), "Month_name", "Tourism")}",
        styles["Normal"]
    ))
    #Pegue o primeiro gráfico e transforme em figura
    grp_weather_tourism.write_image(
        "imagens/grafico_clima_turismo.png",
        width=1200,
        height=600,
        scale=2
    )
    #Inserindo imagem
    elements.append(Image(
        "imagens/grafico_clima_turismo.png",
        width=400,
        height=250
    ))
    pearson = df_weather_tourism["Tourism"].corr(df_weather_tourism["TEMPERATURA MEDIA, DIARIA (AUT)(°C)"], method="pearson")
    spearman = df_weather_tourism["Tourism"].corr(df_weather_tourism["TEMPERATURA MEDIA, DIARIA (AUT)(°C)"], method="spearman")
    elements.append(Paragraph(
        f"<b>Pearsom</b>: {pearson:.2f}<br/>"
        f"<b>Spearman</b>: {spearman:.2f}<br/>"
        f"<b>Análise</b>: A correlação entre temperatura média mensal e fluco de turistas apresentou valores baixos e negativos (Pearson = {pearson:.2f}; Spearman = {spearman:.2f}), indicando que a variável climática, isoladamente, possui pouca influência direta sobre a variação do turismo no período analisado."
    ))
        
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        "Relação entre Turismo e Eventos",
        styles["Title"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Evento com maior Fluxo Turístico</b>:<br/>{df_tourism_event.groupby("Name", as_index=False)["Tourism"].sum().sort_values("Tourism", ascending=False).iloc[0]["Name"]}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Evento com menor Fluxo Turístico</b>:<br/>{df_tourism_event.groupby("Name", as_index=False)["Tourism"].sum().sort_values("Tourism", ascending=True).iloc[0]["Name"]}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Top 3 eventos que mais atraem Turistas</b>:<br/>{list_items_br(df_tourism_event.groupby("Name", as_index=False)["Tourism"].sum().sort_values("Tourism", ascending=False).head(3), "Name", "Tourism")}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"<b>Top 3 eventos que menos atraem Turistas</b>:<br/>{list_items_br(df_tourism_event.groupby("Name", as_index=True)["Tourism"].sum().sort_values(ascending=True).reset_index().head(3), "Name", "Tourism")}",
        styles["Normal"]
    ))
    grp_turism_event.write_image(
        "imagens/grafico_turismo_evento.png",
        width=1200,
        height=600,
        scale=2
    )
    elements.append(Image(
        "imagens/grafico_turismo_evento.png",
        width=400,
        height=250
    ))
    pearson = df_tourism_event["Tourism"].corr(df_tourism_event['Event'], method="pearson")
    spearman = df_tourism_event["Tourism"].corr(df_tourism_event["Event"], method="spearman")
    elements.append(Paragraph(
        f"<b>Pearsom</b>: {pearson:.2f}<br/>"
        f"<b>Spearman</b>: {spearman:.2f}<br/>"
        f"<b>Análise</b>: Enquanto a variável climática apresentou fraca associação com o fluxo turístico, a ocorrência de eventos demonstrou correlação positiva moderada (Pearson = {pearson:.2f}; Spearman = {spearman}), indicando que meses com eventos tendem a registrar maior número de turistas, reforçando o papel da programação de eventos como fator estratégico para o turismo local."
    ))
    elements.append(Spacer(1, 20))

    ##Alimentação e Saúde
    elements.append(Paragraph(
        "Alimentação e Saúde",
        styles["Title"]
    ))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        "<b>Consumo médio Calórico (Restaurantes Analisados)</b>: "
        f"{df_calorie_control[df_calorie_control['Representa'] == 'Ganho Calórico']['Caloria'].sum()} Calorias<br/>"
        "<b>Perda Calórica</b>: "
        f"{df_calorie_control[df_calorie_control['Representa'] == 'Perda Calórica']['Caloria'].sum()} Calorias<br/>"
        "<b>Consumo Calórico Recomendado (Resto do dia)</b>: "
        f"{df_calorie_control[df_calorie_control['Representa'] == 'Perda Calórica']['Caloria'].sum() - df_calorie_control[df_calorie_control['Representa'] == 'Ganho Calórico']['Caloria'].sum()} Calorias."
    ))
    graphics_bar(df_calorie_control, "Nome", "Caloria" , "Ganho e Perda Calórica", "Representa", {"Ganho Calórico": "#d44444", "Perda Calórica": "#4168db"}).write_image(
        "imagens/grafico_calorias.png",
        width=1200,
        height=600,
        scale=2
    )
    elements.append(Image(
        "imagens/grafico_calorias.png",
        width=400,
        height=250
    ))
    elements.append(Paragraph(
        "<b>Combinação de Refeições Recomendadas</b>:<br/>"
        "Macarronada(80) + Carne(100)/ Gelatina(100g): Total de 460 Calorias<br/>"
        "Arroz(80g) + Lentilha(100g) + Omelete(2 ovos)/ Pudim(100g): Total de 570 Calorias<br/>"
        "Arroz(100g) + Feijão(80) + Frango Grelhado(100)/ Sorvete(100g): Total de 610 Calorias<br/>"
        "Legumes Grelhados(200g) + Frango/Carne Magra(100g)/ Pavê(100g): Total de 630 Calorias<br/>",
        styles["Normal"]
    ))

    doc.build(elements)
    placeholder.empty()
    placeholder.success("Relatório Gerado com Sucesso!")
    time.sleep(3)
    placeholder.empty()

    st.markdown("<br><h3>Baixar Relatório Gerado:</h3>", unsafe_allow_html=True)
    with open("relatorio/Relatorio_Gramado.pdf", "rb") as file: #Abre o arquivo em binario rb
        st.download_button(
            label="Baixar Relatório", #Nome do botao
            data=file, #Arquivo
            file_name="Relatorio_Gramado.pdf", #Nome que o usuário verá
            mime="application/pdf" #Informar ao navegador que é pdf
        )