def load_data(df, csv_path, json_path):
    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", indent=4)
    print("[LOAD] Dados carregados com sucesso!")
