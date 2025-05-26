
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import joblib

# 1. Carregar os dados
df = pd.read_excel("dados_treinamento_aumentado.xlsx")
coluna_alvo = "Ploidia"

# 2. Separar variáveis independentes (X) e variável dependente (y)
X = df.drop(columns=[coluna_alvo])
y = df[coluna_alvo]
colunas_usadas = X.columns.tolist()

# 3. Dividir dados em treino (80%) e validação (20%)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Critérios de qualidade exigidos
criterios = {
    "r2": 0.7,        # ≥ 0.7 (bom), ≥ 0.9 (excelente)
    "mae": 10,        # ≤ 10
    "rmse": 10,       # ≤ 10
    "mse": 100        # ≤ 100
}

# 5. Treinar modelo com ajuste inteligente de hiperparâmetros
melhor_modelo = None
tentativas = 0
max_tentativas = 20

while tentativas < max_tentativas:
    tentativas += 1
    modelo = GradientBoostingRegressor(
        n_estimators=100 + tentativas * 10,
        max_depth=3 + (tentativas % 4),
        learning_rate=0.05 + (tentativas * 0.005),
        random_state=42
    )
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_val)

    r2 = r2_score(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_val, y_pred)

    print(f"Tentativa {tentativas} ➤ R²: {r2:.4f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}, MAE: {mae:.2f}")

    if r2 >= criterios["r2"] and mse <= criterios["mse"] and rmse <= criterios["rmse"] and mae <= criterios["mae"]:
        melhor_modelo = modelo
        break

# 6. Salvar modelo final e colunas se aprovado
if melhor_modelo:
    joblib.dump(melhor_modelo, "modelo_gb_euploidia.pkl")
    joblib.dump(colunas_usadas, "features_gb_modelo.pkl")
    print("✅ Modelo Gradient Boosting treinado e salvo com sucesso!")
else:
    print("❌ Nenhum modelo atingiu os critérios definidos.")
