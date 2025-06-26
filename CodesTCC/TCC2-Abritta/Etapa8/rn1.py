import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

ARQUIVO_ENTRADA = "PlanilhaNumerica.xlsx"
ARQUIVO_SAIDA = "Planilha_Com_Classe_Probabilidade.xlsx"

print(f"Lendo arquivo para predição: {ARQUIVO_ENTRADA}...")
df = pd.read_excel(ARQUIVO_ENTRADA)

# Carregar modelo e scaler salvos
mlp = joblib.load("mlp_model.pkl")  
scaler = joblib.load("scaler.pkl")

# Verificar se tem coluna Ploidia
tem_rotulo = "Ploidia" in df.columns

# Separar X e y se possível
if tem_rotulo:
    X = df.drop(columns=["Ploidia"])
    y_true = df["Ploidia"].values
else:
    X = df.copy()
    y_true = None

# Aplicar scaler
X_scaled = scaler.transform(X)

# Prever classes e probabilidades
classes_pred = mlp.predict(X_scaled)
probs = mlp.predict_proba(X_scaled)[:, 1]

# Inserir resultados na planilha
df["Classe_Prevista"] = classes_pred
df["Prob_Euploidia_%"] = np.round(probs * 100, 2)

# Exibir métricas, se possível
if tem_rotulo:
    print("\n✅ Avaliação da predição:")
    acc = accuracy_score(y_true, classes_pred)
    print(f"Accuracy: {acc:.3f}")
    print("\nClassification Report:")
    print(classification_report(y_true, classes_pred))
    auc = roc_auc_score(y_true, probs)
    print(f"AUC: {auc:.3f}")
else:
    print("⚠️ Coluna 'Ploidia' não encontrada — apenas predição realizada.")

# Salvar planilha com resultados
df.to_excel(ARQUIVO_SAIDA, index=False)
print(f"\n📄 Arquivo salvo como: {ARQUIVO_SAIDA}")
print("✅ Predição concluída com sucesso!")