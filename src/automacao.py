import schedule
import time
from src.coleta import coletar_dados
from src.tratamento import tratar_dados
from src.banco import salvar_dados

def job():
    print("🚀 Executando pipeline automático...")

    dados = coletar_dados()
    print(f"📥 Dados coletados: {len(dados)}")

    df = tratar_dados(dados)
    print(f"🧹 Dados tratados: {df.shape}")

    salvar_dados(df)
    print("💾 Dados salvos no banco!\n")

# ⏱️ Intervalo curto para demonstração
schedule.every(10).seconds.do(job)

print("⏳ Automação iniciada... (Ctrl+C para parar)")

while True:
    schedule.run_pending()
    time.sleep(1)