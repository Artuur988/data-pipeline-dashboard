from sqlalchemy import create_engine

def salvar_dados(df):
    engine = create_engine("sqlite:///dados.db")
    df.to_sql("produtos", engine, if_exists="replace", index=False)

