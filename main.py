from src.coleta import coletar_dados
from src.tratamento import tratar_dados

dados = coletar_dados()
df = tratar_dados(dados)

print(df.head())

