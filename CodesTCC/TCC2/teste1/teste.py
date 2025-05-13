import pandas as pd
import joblib
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, root_mean_squared_error
import numpy as np

# Carregar modelo e colunas
modelo = joblib.load("modelo_euploidia.pkl")
colunas_usadas = joblib.load("features_modelo.pkl")

# Carregar dados de teste
df_teste = pd.read_excel("dados_teste.xlsx")

# Simular a porcentagem de euploidia (caso ainda não tenha a real)
np.random.seed(42)
df_teste['porcentagem_euploidia'] = np.random.uniform(30, 90, size=len(df_teste))

# Pré-processar
colunas_features = [
    'Idade', 'Estágio', 'Morfo', 'Kidscore', 't2', 't3', 't4', 't5', 't8',
    'tSC', 'tSB', 'tB', 'cc2 (t3-t2)', 'cc3 (t5-t3)', 't5-t2',
    's2 (t4-t3)', 's3 (t8-t5)', 'tSC-t8', 'tB-tSB'
]
df_encoded = pd.get_dummies(df_teste[colunas_features])
df_encoded = df_encoded.reindex(columns=colunas_usadas, fill_value=0)

# Separar X e y
X_teste = df_encoded
y_teste = df_teste['porcentagem_euploidia']

# Predizer e avaliar
y_pred = modelo.predict(X_teste)

# Métricas de regressão ?? ENTENDER MAIS SOBRE ELAS!!!
r2 = r2_score(y_teste, y_pred)
mse = mean_squared_error(y_teste, y_pred)
rmse = root_mean_squared_error(y_teste, y_pred)
mae = mean_absolute_error(y_teste, y_pred)

print("MÉTRICAS DE REGRESSÃO (TESTE):")
print(f"R²: {r2:.4f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")