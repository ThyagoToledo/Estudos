# Box Plots in Python 
# Documentação: https://plotly.com/python/box-plots/

# Importando a biblioteca Plotly Express para criar gráficos interativos
import plotly.express as px 
# Carregando um conjunto de dados de exemplo sobre gorjetas em restaurantes
df = px.data.tips()
# Criando um box plot para visualizar a distribuição das gorjetas (total_bill)
fig = px.box(df, y="total_bill")
# Exibindo o gráfico interativo
fig.show()