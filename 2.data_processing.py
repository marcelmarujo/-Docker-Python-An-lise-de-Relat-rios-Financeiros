import pandas as pd

def processar_dados(caminho_arquivo):
    """Processa os dados e salva a saída."""
    dados = pd.read_csv(caminho_arquivo)
    dados_processados = dados.dropna()  # Exemplo de processamento
    dados_processados.to_csv("/Users/Marcel/Projetos/finance-analysis/dados/processados/transacoes_processadas.csv", index=False)

if __name__ == "__main__":
    caminho_arquivo = "/Users/Marcel/Projetos/finance-analysis/dados/brutos/transacoes_ficticias.csv"
    processar_dados(caminho_arquivo)
