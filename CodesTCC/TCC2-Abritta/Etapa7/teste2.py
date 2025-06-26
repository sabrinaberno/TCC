import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# === CONFIGURAÇÕES ===
ARQUIVO_ENTRADA = "PlanilhaNumerica.xlsx"
ARQUIVO_SAIDA = "Planilha_Com_Classe_Probabilidade.xlsx"

print("\n=== CLASSIFICAÇÃO DE EMBRIÕES COM NOVA REDE NEURAL (MLP) ===")

# === CARREGAR PLANILHA ===
print(f"Lendo o arquivo: {ARQUIVO_ENTRADA}...")
df = pd.read_excel(ARQUIVO_ENTRADA)

# === PRÉ-PROCESSAMENTO ===
tem_rotulo = "Ploidia" in df.columns

if tem_rotulo:
    le_ploidia = LabelEncoder()
    df["Ploidia"] = le_ploidia.fit_transform(df["Ploidia"])

X = df.drop(columns=["Ploidia"]) if tem_rotulo else df.copy()
y = df["Ploidia"] if tem_rotulo else None

# Escalar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

if tem_rotulo:
    # Balancear manualmente + jitter
    X_df = pd.DataFrame(X_scaled)
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
    indices = np.random.permutation(len(X_bal))
    X_bal = X_bal.iloc[indices].values
    y_bal = y_bal[indices]

    def augment(X, y, n=3, noise=0.05):
        X_aug = [X]
        y_aug = [y]
        for _ in range(n):
            noise_matrix = np.random.normal(0, noise, X.shape)
            X_aug.append(X + noise_matrix)
            y_aug.append(y)
        return np.vstack(X_aug), np.concatenate(y_aug)

    X_aug, y_aug = augment(X_bal, y_bal)

    print("Treinando nova Rede Neural MLP...")
    mlp = MLPClassifier(hidden_layer_sizes=(128, 64, 32),
                        activation='relu',
                        max_iter=1000,
                        early_stopping=True,
                        random_state=42)
    mlp.fit(X_aug, y_aug)

    # Salvar modelo e scaler
    joblib.dump(mlp, "mlp_model.pkl")
    joblib.dump(scaler, "scaler.pkl")
    print("Modelo e scaler salvos como 'mlp_model.pkl' e 'scaler.pkl'.")

    classes_pred = mlp.predict(X_scaled)
    probs = mlp.predict_proba(X_scaled)[:, 1]
else:
    print("⚠️ A planilha não contém rótulos (coluna 'Ploidia'), a MLP será apenas simulada.")

df["Classe_Prevista"] = classes_pred
df["Prob_Euploidia_%"] = np.round(probs * 100, 2)

if tem_rotulo:
    acc = accuracy_score(y, classes_pred)
    print(f"\n✅ Acurácia na planilha: {acc:.3f}")
    print("\nRelatório de Classificação:\n")
    print(classification_report(y, classes_pred))
    print(f"AUC: {roc_auc_score(y, probs):.3f}")

df.to_excel(ARQUIVO_SAIDA, index=False)
print(f"\nArquivo salvo como: {ARQUIVO_SAIDA}")
print("✅ Classificação concluída com sucesso!")