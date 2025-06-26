import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.utils import shuffle

# === CONFIGURAÇÕES ===
ARQUIVO_ENTRADA = "PlanilhaNumerica.xlsx"
MODELO_PKL = "mlp_model.pkl"
SCALER_PKL = "scaler.pkl"

print(f"\n📥 Lendo dados: {ARQUIVO_ENTRADA}")
df = pd.read_excel(ARQUIVO_ENTRADA)

# === PRÉ-CHECAGEM ===
if "Ploidia" not in df.columns:
    raise ValueError("❌ A coluna 'Ploidia' é obrigatória para avaliação.")

# === SEPARAR FEATURES E RÓTULOS ===
X = df.drop(columns=["Ploidia"])
y = df["Ploidia"].values

# === CARREGAR MODELO ANTIGO E AVALIAR ===
print("\n🔍 Avaliando modelo salvo...")
scaler_antigo = joblib.load(SCALER_PKL)
modelo_antigo = joblib.load(MODELO_PKL)
X_scaled_antigo = scaler_antigo.transform(X)
probs_antigo = modelo_antigo.predict_proba(X_scaled_antigo)[:, 1]
auc_antigo = roc_auc_score(y, probs_antigo)
print(f"📊 AUC do modelo antigo: {auc_antigo:.4f}")

# === BALANCEAMENTO MANUAL + JITTER ===
print("\n🧪 Re-treinando nova MLP com dados balanceados...")
scaler_novo = StandardScaler()
X_scaled = scaler_novo.fit_transform(X)
X_df = pd.DataFrame(X_scaled)

# Balanceamento manual
class_0 = X_df[y == 0]
class_1 = X_df[y == 1]

if len(class_0) > len(class_1):
    class_1_up = class_1.sample(len(class_0), replace=True, random_state=42)
    X_bal = pd.concat([class_0, class_1_up])
    y_bal = np.array([0] * len(class_0) + [1] * len(class_1_up))
else:
    class_0_up = class_0.sample(len(class_1), replace=True, random_state=42)
    X_bal = pd.concat([class_0_up, class_1])
    y_bal = np.array([0] * len(class_0_up) + [1] * len(class_1))

X_bal, y_bal = shuffle(X_bal.values, y_bal, random_state=42)

# Aumento de dados com jitter
def augment(X, y, n=3, noise=0.05):
    X_aug = [X]
    y_aug = [y]
    for _ in range(n):
        noise_matrix = np.random.normal(0, noise, X.shape)
        X_aug.append(X + noise_matrix)
        y_aug.append(y)
    return np.vstack(X_aug), np.concatenate(y_aug)

X_aug, y_aug = augment(X_bal, y_bal)

# Treinar nova MLP
mlp_novo = MLPClassifier(hidden_layer_sizes=(128, 64, 32),
                         activation='relu',
                         max_iter=1000,
                         early_stopping=True,
                         random_state=42)
mlp_novo.fit(X_aug, y_aug)

# Avaliar nova MLP
X_scaled_novo = scaler_novo.transform(X)
probs_novo = mlp_novo.predict_proba(X_scaled_novo)[:, 1]
auc_novo = roc_auc_score(y, probs_novo)
print(f"📈 AUC do novo modelo: {auc_novo:.4f}")

# === COMPARAÇÃO E DECISÃO ===
if auc_novo > auc_antigo:
    joblib.dump(mlp_novo, MODELO_PKL)
    joblib.dump(scaler_novo, SCALER_PKL)
    print(f"\n✅ Novo modelo SALVO! AUC melhorou de {auc_antigo:.4f} para {auc_novo:.4f}")
else:
    print(f"\n⚠️ Novo modelo NÃO salvo. AUC não melhorou: {auc_antigo:.4f} ➝ {auc_novo:.4f}")