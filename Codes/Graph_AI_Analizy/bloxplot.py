# Box Plots in Python 
# Documentação: https://plotly.com/python/box-plots/

# Importando a biblioteca Plotly Express para criar gráficos interativos
import plotly.express as px 
# Carregando um conjunto de dados de exemplo sobre gorjetas em restaurantes
dados_gorjetas = px.data.tips()
# Criando um box plot para visualizar a distribuição das gorjetas (total_bill)
grafico_bloxplot = px.box(dados_gorjetas, y="tip")
# Exibindo o gráfico interativo
grafico_bloxplot.show()