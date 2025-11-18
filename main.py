from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    df = extract_data("../data/vendas.csv")
    relatorio = transform_data(df)
    load_data(relatorio, "../output/relatorio_final.csv", "../output/relatorio_final.json")

if __name__ == "__main__":
    main()
