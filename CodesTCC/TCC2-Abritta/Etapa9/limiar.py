import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split

# === Carregar os dados e modelo ===
df = pd.read_excel("PlanilhaNumerica.xlsx")
X = df.drop(columns=["Ploidia"])
y = df["Ploidia"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

modelo = joblib.load("melhor_modelo_mlp_20250610_113659.pkl")
scaler = joblib.load("scaler_mlp_20250610_113659.pkl")

X_test_scaled = scaler.transform(X_test)
y_proba = modelo.predict_proba(X_test_scaled)[:, 1]

# === Testar vários limiares e calcular métricas ===
limiares = [0.3, 0.4, 0.5, 0.6, 0.7]

print("Limiar\tAcurácia\tRecall (Euploide)\tRecall (Aneuploide)\tAUC")
for limiar in limiares:
    y_pred_limiar = (y_proba >= limiar).astype(int)
    
    acc = accuracy_score(y_test, y_pred_limiar)
    recall_euploide = recall_score(y_test, y_pred_limiar, pos_label=1)
    recall_aneuploide = recall_score(y_test, y_pred_limiar, pos_label=0)
    auc = roc_auc_score(y_test, y_proba)
    
    print(f"{limiar:.1f}\t{acc:.3f}\t\t{recall_euploide:.3f}\t\t\t{recall_aneuploide:.3f}\t\t\t{auc:.3f}")