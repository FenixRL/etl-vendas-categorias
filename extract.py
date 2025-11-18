import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        print("[EXTRACT] Dados extraídos com sucesso.")
        return df
    except Exception as e:
        print(f"[ERRO] Falha ao extrair dados: {e}")
        return None
