import pandas as pd

# Tratando os dados do Clima #
"""df = pd.read_csv(
    "data/clima_canela.csv",
    sep=";",                 # separador correto
    decimal=",",             # vírgula como decimal
)

#Pegando colunas específicas
df_weather = df[['Data Medicao', 'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)', 'TEMPERATURA MEDIA, DIARIA (AUT)(°C)', 'UMIDADE RELATIVA DO AR, MEDIA DIARIA (AUT)(%)', 'VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)']]

#Tranformando a coluna data
df_weather['Data Medicao'] = pd.to_datetime(df_weather['Data Medicao'])

#Pegar colunas importantes e criar a média dos valores nulos
colunas = ['Data Medicao', 'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)', 'TEMPERATURA MEDIA, DIARIA (AUT)(°C)', 'UMIDADE RELATIVA DO AR, MEDIA DIARIA (AUT)(%)', 'VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)']

df_weather[colunas] = df_weather[colunas].fillna(df_weather[colunas].mean())

#Criar a coluna mes, separar a média por mes
df_weather["Mes"] = df_weather["Data Medicao"].dt.to_period("M")
df_weather = df_weather.groupby("Mes").mean()

# Dados do Turismo, criação
dados_turismo_mensal = {
    "Month": ['2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', '2025-05-01', '2025-06-01', '2025-07-01', '2025-08-01', '2025-09-01', '2025-10-01', '2025-11-01', '2025-12-01'],
    "Tourism": [390544, 229895, 249323, 356868, 347200, 343370, 407948, 365790, 314072, 333381, 420734, 473161]

}
df_dados_turismo_mensal = pd.DataFrame(dados_turismo_mensal)
df_dados_turismo_mensal["Month"] = pd.to_datetime(df_dados_turismo_mensal["Month"])
df_dados_turismo_mensal["Month"] = df_dados_turismo_mensal["Month"].dt.to_period("M")
df_dados_turismo_mensal.to_csv("data/monthly_tourism.csv", index=False)

dados_turismo_estado = {
    "State": ['São Paulo', 'Santa Catarina', 'Paraná', 'Rio de Janeiro', 'Minas Gerais', 'Pernambuco', 'Goiás', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Pará', 'Rio Grande do Norte', 'Mato Grosso', 'Paraíba', 'Maranhão', 'Mato Grosso do Sul', 'Amazonas', 'Alagoas', 'Piauí', 'Tocantins', 'Rondônia', 'Sergipe', 'Roraima', 'Acre', 'Amapá'],
    "Tourism": [343667, 333863, 138048, 122433, 96086, 48907, 44565, 42027, 36961, 32437, 25748, 23628, 22529, 21862, 20797, 19797, 16931, 16202, 15337, 10019, 7034, 6910, 5840, 2950, 2309, 1810]
}

df_dados_turismo_estado = pd.DataFrame(dados_turismo_estado)

df_dados_turismo_estado.to_csv("data/state_tourism.csv", index=False)

#Dados de restaurante e caloria
restaurante = {
    "Restaurente": ['Cantina Pastasciutta', 'mlbkRestaurant', 'Vue de La Vallee', 'Kongo Pizzaria Temática', 'St. Gallen Restaurant'],
    "Avaliações": [12737, 7980, 7539, 6412, 4302],
    "Pratos Principais": ['Pratos Italianos', 'Parrilha e Fondue', 'Fondue', 'Pizza (10 fatias)', 'Fondue'],
    "Caloria Média dos Pratos": [500, 1500, 1500, 3500, 1500]
}

df_restaurante = pd.DataFrame(restaurante)

df_restaurante.to_csv("data/restaurant.csv", index=False)

## Criando DataFrame de eventos ##
event_gramado = {
    "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Name": ['s/', 's/', 'Páscoa', 'Páscoa', 'Festa da Colônia', 's/', 'Férias Escolares', 'Festival de Cinema', 's/', 'Natal Luz', 'Natal Luz', 'Natal Luz'],
    "Event": [0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
}

event_gramado = pd.DataFrame(event_gramado)
event_gramado["Date"] = pd.to_datetime(
    '01-' + event_gramado["Month"].astype(str).str.zfill(2) + '-2025',
    format = "%d-%m-%Y"
    )

event_gramado["Month_name"] = event_gramado['Date'].dt.month_name(locale='pt_BR')

##Criando Cardápios##
foods = {
    "Refeição": ["Arroz(100g) + Feijão(80) + Frango Grelhado(100)", "Macarronada(80) + Carne(100)", "Legumes Grelhados(200g) + Frango/Carne Magra(100g)", "Arroz(80g) + Lentilha(100g) + Omelete(2 ovos)"],
    "Calorias Refeição": [360, 400, 300, 370],
    "Sobremesas": ["Pudim(100g)", "Pavê(100g)", "Gelatina(100g)", "Sorvete(100g)"],
    "Calorias Sobremesa": [200, 330, 60, 250]
}

df_foods = pd.DataFrame(foods)
df_foods.to_csv("data/foods.csv", index=False)
"""

df_month_tourism = pd.read_csv("data/monthly_tourism.csv")
df_restaurant = pd.read_csv("data/restaurant.csv")
df_state_tourism = pd.read_csv("data/state_tourism.csv")
df_weather = pd.read_csv("data/weather.csv")
df_event_gramado = pd.read_csv("data/event_gramado.csv")
df_weather_tourism = pd.read_csv("data/weatherAndTourism.csv")
df_tourism_event = pd.read_csv("data/tourismAndEvent.csv")
df_foods = pd.read_csv("data/foods.csv")

#DataFrame com controle de calorias
calorie_control = {
    "Nome": ["Taxa Metabólica Basal", "Perda em Caminhada (2h)", "Consumo médio Restaurantes Pesquisados"],
    "Caloria": [1600, 400, df_restaurant["Caloria Média dos Pratos"].median()], #Mediana para tirar valores extremos
    "Representa": ["Perda Calórica", "Perda Calórica", "Ganho Calórico"]
}
df_calorie_control = pd.DataFrame(calorie_control)

#Pegando como base a TMB e a caminhada diaria de 2h, um turista perde em média 2000 calorias por dia, então o consumo recomendade para não ter alterações no peso seria esse
#Porém, pegando os restaurantes pesquisados e fazendo a média dos pratos, podemos ver que o consumo calórico chega a 1700, sobrando 200 calorias para consumir e não ter variações no peso
#Em geral, esses resturantes são visitados em almoço ou Jantar, o que deixa o perído da manha como oportunidade para criar refeiçoes leves, no máximo 500 calorias para manter a saúde dos turistas
#Próximo passo, mostrar graficamente esse ponto e desenvolver pratos que somados dão menos de 500 calorias.