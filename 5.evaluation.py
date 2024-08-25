import pandas as pd
from sklearn.metrics import accuracy_score

def avaliar_modelo(modelo, caminho_arquivo):
    """Avalia o modelo treinado."""
    dados = pd.read_csv(caminho_arquivo)
    X = dados[['nova_feature']]
    y = dados['classe']
    previsoes = modelo.predict(X)
    acuracia = accuracy_score(y, previsoes)
    print(f"Acurácia do modelo: {acuracia}")

if __name__ == "__main__":
    from model_training import treinar_modelo
    
    caminho_arquivo = "/Users/Marcel/Projetos/finance-analysis/dados/features/transacoes_features.csv"
    modelo = treinar_modelo(caminho_arquivo)
    avaliar_modelo(modelo, caminho_arquivo)
