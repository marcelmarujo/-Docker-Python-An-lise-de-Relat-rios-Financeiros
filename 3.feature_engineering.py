import pandas as pd

def criar_features(caminho_arquivo):
    """Cria novas features a partir dos dados processados."""
    dados = pd.read_csv(caminho_arquivo)
    dados['nova_feature'] = dados['valor'] * 2  # Exemplo de feature
    dados.to_csv("/Users/Marcel/Projetos/finance-analysis/dados/features/transacoes_features.csv", index=False)

if __name__ == "__main__":
    caminho_arquivo = "/Users/Marcel/Projetos/finance-analysis/dados/processados/transacoes_processadas.csv"
    criar_features(caminho_arquivo)
