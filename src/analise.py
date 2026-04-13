def gerar_insights(df):
    media_preco = df['price'].mean()
    produto_mais_caro = df.loc[df['price'].idxmax()]

    return {
        "media_preco": media_preco,
        "produto_mais_caro": produto_mais_caro['title']
    }