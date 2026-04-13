from src.coleta import coletar_dados
from src.tratamento import tratar_dados
from src.banco import salvar_dados
from src.analise import gerar_insights

print("🔄 Iniciando pipeline...")

dados = coletar_dados()
print(f"📥 Dados coletados: {len(dados)} registros")

df = tratar_dados(dados)
print(f"🧹 Dados tratados: {df.shape[0]} linhas e {df.shape[1]} colunas")

salvar_dados(df)
print("💾 Dados salvos no banco!")

insights = gerar_insights(df)

print("\n📊 INSIGHTS:")
print(f"💰 Preço médio: {insights['media_preco']:.2f}")
print(f"🏆 Produto mais caro: {insights['produto_mais_caro']}")

print("\n✅ Pipeline finalizado com sucesso!")