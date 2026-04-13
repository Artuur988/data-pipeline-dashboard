import pandas as pd

def tratar_dados(dados):
    df = pd.DataFrame(dados)

    df = df[['title', 'price', 'category', 'rating']]
    df['rating'] = df['rating'].apply(lambda x: x['rate'])

    df.dropna(inplace=True)

    return df