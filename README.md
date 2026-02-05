# 🚀 Smart Tourism & Health Insights

Projeto de **análise de dados aplicada à tomada de decisão no setor hoteleiro**, integrando informações de **turismo, clima, eventos, alimentação e saúde**.

O objetivo é apoiar decisões estratégicas de redes hoteleiras por meio de **análises estatísticas responsáveis**, **simulações exploratórias** e **relatórios analíticos automatizados**.

---

## 🎯 Objetivo do Projeto

O projeto foi desenvolvido para ir além de visualizações e dashboards, priorizando:

- Clareza analítica  
- Responsabilidade estatística  
- Transparência metodológica  
- Aplicabilidade prática para o negócio  

A proposta central é **testar suposições comuns** sobre o turismo e avaliar quais fatores realmente apresentam relevância quando analisados com dados.

---

## 🔍 Principais Análises Realizadas

- Exploração e estruturação de dados com foco em leitura de padrões  
- Análises descritivas orientadas à tomada de decisão  
- Testes estatísticos para validação (ou refutação) de hipóteses  
- Simulações exploratórias, deixando explícitos os limites de inferência  
- Geração automatizada de relatórios analíticos em PDF  

📊 **Resultado de destaque:**  
No conjunto analisado, o **clima não apresentou relação estatisticamente significativa com o fluxo turístico**, enquanto **fatores estruturais do turismo e eventos** mostraram maior relevância.

---

## 🍽️ Análise de Alimentação (Foco em Hotelaria)

Pensando no setor hoteleiro, o projeto inclui uma análise voltada à **orientação de parcerias e recomendações gastronômicas**, considerando:

- Restaurantes mais visitados  
- Avaliações dos usuários  
- Média calórica dos pratos principais  

Foi utilizado um **modelo energético exploratório simples e interpretável**, baseado em: (TMB + gasto estimado de uma caminhada de 2 horas) − média calórica dos pratos principais
Esse modelo permite comparar **consumo alimentar** e **gasto energético diário** de forma objetiva e orientada à decisão.

⚠️ Importante:  
Essa etapa é tratada explicitamente como **análise exploratória e simulacional**, não como inferência nutricional.

---

## 📄 Relatórios Automáticos

O projeto gera **relatórios analíticos em PDF automaticamente**, reunindo:

- Resultados das análises  
- Gráficos  
- Interpretações orientadas ao negócio  

Essa funcionalidade facilita a comunicação dos insights para gestores e tomadores de decisão.

---

## 🖥️ Aplicação

A aplicação foi desenvolvida com **Streamlit**, permitindo:

- Visualização interativa dos dados  
- Execução das análises  
- Geração automática de relatórios  

👉 **Aplicação em produção:**  
(https://smarth-tourism-health-insights-jynwkdt9ek8wlqkus7mcya.streamlit.app/
)

---

## 🧰 Stack Utilizada

- Python  
- pandas  
- numpy  
- matplotlib  
- plotly  
- scipy  
- statsmodels  
- Streamlit  
- ReportLab (geração de PDFs)  
