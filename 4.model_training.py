import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def treinar_modelo(caminho_arquivo):
    """Treina um modelo de machine learning."""
    dados = pd.read_csv(caminho_arquivo)
    X = dados[['nova_feature']]
    y = dados['classe']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)
    return modelo

if __name__ == "__main__":
    caminho_arquivo = "/Users/Marcel/Projetos/finance-analysis/dados/features/transacoes_features.csv"
    modelo = treinar_modelo(caminho_arquivo)
    print("Modelo treinado com sucesso!")
