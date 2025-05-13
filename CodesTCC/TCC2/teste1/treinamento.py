import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Carregar dados de treinamento
df_treino = pd.read_excel("dados_treinamento.xlsx")

# Definir as features
colunas_features = [
    'Idade', 'Estágio', 'Morfo', 'Kidscore', 't2', 't3', 't4', 't5', 't8',
    'tSC', 'tSB', 'tB', 'cc2 (t3-t2)', 'cc3 (t5-t3)', 't5-t2',
    's2 (t4-t3)', 's3 (t8-t5)', 'tSC-t8', 'tB-tSB'
]

# Simular variável alvo (por enquanto)
np.random.seed(42)
df_treino['porcentagem_euploidia'] = np.random.uniform(30, 90, size=len(df_treino))

# Pré-processamento (One-Hot Encoding)
df_encoded = pd.get_dummies(df_treino[colunas_features])
X_treino = df_encoded
y_treino = df_treino['porcentagem_euploidia']
colunas_usadas = X_treino.columns.tolist()

# Treinar o modelo
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

# Salvar modelo e colunas
joblib.dump(modelo, "modelo_euploidia.pkl")
joblib.dump(colunas_usadas, "features_modelo.pkl")

print("Modelo treinado e salvo com sucesso!")