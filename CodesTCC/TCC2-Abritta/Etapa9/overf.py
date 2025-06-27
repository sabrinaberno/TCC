import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score

# === CARREGAR OS DADOS ===
df = pd.read_excel("PlanilhaNumerica.xlsx")
X = df.drop(columns=["Ploidia"])
y = df["Ploidia"]

# === SPLIT EM TREINO E TESTE IGUAL AO USADO ANTES ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# === CARREGAR MODELO E SCALER ===
modelo = joblib.load("mlp_model.pkl")
scaler = joblib.load("scaler.pkl")

# === ESCALONAR OS DADOS ===
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# === PREVISÕES ===
y_train_pred = modelo.predict(X_train_scaled)
y_train_proba = modelo.predict_proba(X_train_scaled)[:, 1]
y_test_pred = modelo.predict(X_test_scaled)
y_test_proba = modelo.predict_proba(X_test_scaled)[:, 1]

# === MÉTRICAS TREINO ===
acc_train = accuracy_score(y_train, y_train_pred)
recall_train_euploide = recall_score(y_train, y_train_pred, pos_label=1)
recall_train_aneuploide = recall_score(y_train, y_train_pred, pos_label=0)
auc_train = roc_auc_score(y_train, y_train_proba)

# === MÉTRICAS TESTE ===
acc_test = accuracy_score(y_test, y_test_pred)
recall_test_euploide = recall_score(y_test, y_test_pred, pos_label=1)
recall_test_aneuploide = recall_score(y_test, y_test_pred, pos_label=0)
auc_test = roc_auc_score(y_test, y_test_proba)

# === EXIBIR RESULTADOS ===
print("DESEMPENHO NO TREINO:")
print(f"  Acurácia: {acc_train:.3f}")
print(f"  Recall Euploide: {recall_train_euploide:.3f}")
print(f"  Recall Aneuploide: {recall_train_aneuploide:.3f}")
print(f"  AUC: {auc_train:.3f}\n")

print("DESEMPENHO NO TESTE:")
print(f"  Acurácia: {acc_test:.3f}")
print(f"  Recall Euploide: {recall_test_euploide:.3f}")
print(f"  Recall Aneuploide: {recall_test_aneuploide:.3f}")
print(f"  AUC: {auc_test:.3f}")