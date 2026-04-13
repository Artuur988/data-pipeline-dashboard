import pandas as pd
import random
import datetime

def tratar_dados(dados):
    df = pd.DataFrame(dados)

    # ===== SELEÇÃO E LIMPEZA =====
    df = df[['title', 'price', 'category', 'rating']]
    df['rating'] = df['rating'].apply(lambda x: x['rate'])
    df.dropna(inplace=True)

    # ===== ALEATORIEDADE NA BASE (IMPORTANTE) =====
    df = df.sample(frac=1).reset_index(drop=True)  # embaralha

    # (opcional - mais aleatoriedade ainda)
    df = df.sample(n=min(15, len(df)), replace=True)

    # ===== EXPANSÃO =====
    df_expandido = []

    for _, row in df.iterrows():
        for i in range(random.randint(5, 15)):
            novo = row.copy()

            # ===== VARIAÇÃO DE PREÇO (mais realista) =====
            variacao = random.uniform(0.7, 1.3)
            novo['price'] = round(row['price'] * variacao, 2)

            # ===== VARIAÇÃO DE RATING =====
            novo['rating'] = round(
                min(5, max(1, row['rating'] + random.uniform(-1, 1))), 1
            )

            # ===== VARIAÇÃO DE NOME =====
            novo['title'] = f"{row['title']} v{i}"

            # ===== DADOS SINTÉTICOS =====
            novo['data'] = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))
            novo['estoque'] = random.randint(0, 100)
            novo['desconto'] = random.choice([0, 10, 20, 30])

            df_expandido.append(novo)

    df_final = pd.DataFrame(df_expandido)

    return df_final