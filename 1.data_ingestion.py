import pandas as pd

def extrair_dados(caminho_arquivo):
    """Extrai os dados do arquivo CSV."""
    return pd.read_csv(caminho_arquivo)

if __name__ == "__main__":
    caminho_arquivo = "/Users/Marcel/Projetos/finance-analysis/dados/brutos/transacoes_ficticias.csv"
    dados = extrair_dados(caminho_arquivo)
    print(dados.head())
