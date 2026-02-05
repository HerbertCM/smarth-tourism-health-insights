from dataframes import df_weather, df_weather_tourism, df_tourism_event
import plotly.express as px
import plotly.graph_objects as go

def graphics_line(df, ax_x, ax_y, tx):
    grp_line = px.line(
        df, 
        x= ax_x, 
        y= ax_y,
        markers=True,
        title= tx
    )
    grp_line.update_xaxes(title_text="")
    grp_line.update_yaxes(title_text="")
    return grp_line

def graphics_bar(df, ax_x, ax_y, tx, clr=None, clr_map=None):
    grp_bar = px.bar(
        df,
        x=ax_x,
        y=ax_y,
        color=clr,
        color_discrete_map=clr_map,
        title=tx
    )
    grp_bar.update_xaxes(title_text="")
    grp_bar.update_yaxes(title_text="")
    return grp_bar

def graphics_pie(df, value, name, tx):
    grp_pie = px.pie(
        df, 
        values=value, 
        names=name, 
        title=tx
    )
    return grp_pie

## Criar Gráfico de clima, turismo e mes
grp_weather_tourism = go.Figure() #Cria a figura
grp_weather_tourism.add_trace( #Cria o gráfico na figura
    go.Bar(
        x=df_weather_tourism["Month_name"],
        y=df_weather_tourism["Tourism"],
        name="Turistas",
        yaxis="y1" #Coloca o eixo y na esquerda
    )
)

# Linha - Temperatura
grp_weather_tourism.add_trace(
    go.Scatter( #Cria mais um gráfico na figura
        x=df_weather_tourism["Month_name"],
        y=df_weather_tourism["TEMPERATURA MEDIA, DIARIA (AUT)(°C)"],
        name="Temperatura Média (°C)",
        mode="lines+markers", #Adiciona linhas e marcadores
        yaxis="y2" #Coloca o eixo y na direita
    )
)

grp_weather_tourism.update_layout( #Upgrade nos gráficos
    title="Turismo x Temperatura por Mês",
    xaxis=dict(title="Mês"), #Titulo do eixo x
    yaxis=dict(
        title="Quantidade de Turistas", #Titulo do eixo y
        side="left" #Titulo á esquerda
    ),
    yaxis2=dict(
        title="Temperatura (°C)", 
        overlaying="y", #Informa que o eixo y vai compartilhar o eixo x
        side="right" 
    ),
    legend=dict(x=0.01, y=0.99), #posição da legenda
    template="plotly_white" #Limpo, fundo branco
)

## Criar gráfico de mes, turismo e evento

df_event_yes = df_tourism_event[df_tourism_event["Event"] == 1]
grp_turism_event = go.Figure()
grp_turism_event.add_trace(
    go.Scatter(
        x=df_tourism_event["Month_name"],
        y=df_tourism_event["Tourism"],
        name="Turistas",
        mode="lines+markers",
        yaxis="y1"
    )
)

grp_turism_event.add_trace(
    go.Scatter(
        x=df_event_yes["Month_name"],
        y=df_event_yes["Tourism"],
        name="Eventos",
        mode="markers",
        marker=dict(
            size=14,
            symbol="star"
        )
    )
)

grp_turism_event.update_layout(
    title="Turismo x Eventos",
    xaxis=dict(title="Mês"),
    yaxis=dict(
        title="Quantidade de Turistas",
        side="left"
    ),
    legend=dict(x=0.01, y=0.99),
    template="plotly_white"
)