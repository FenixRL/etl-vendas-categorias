import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print("[TRANSFORM] Iniciando transformação...")

    # Remove valores nulos
    df = df.dropna()

    # Padroniza categorias
    df["categoria"] = df["categoria"].str.lower()

    # Calcula total por categoria
    relatorio = df.groupby("categoria")["valor"].sum().reset_index()

    print("[TRANSFORM] Transformação concluída.")
    return relatorio
