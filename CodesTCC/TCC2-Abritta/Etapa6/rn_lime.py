import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, classification_report, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import lime
import lime.lime_tabular
import numpy as np

df = pd.read_excel("PlanilhaNumerica.xlsx")
modelo = joblib.load("melhor_modelo_mlp_20250610_113659.pkl")
scaler = joblib.load("scaler_mlp_20250610_113659.pkl")

X = df.drop(columns=["Ploidia"], errors="ignore")
y_true = df["Ploidia"]

colunas_treinadas = scaler.feature_names_in_
for col in colunas_treinadas:
    if col not in X.columns:
        X[col] = 0  

X = X[colunas_treinadas]
X_scaled = scaler.transform(X)

classes_preditas = modelo.predict(X_scaled)

explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=X_scaled,
    feature_names=colunas_treinadas,
    mode='classification',
    discretize_continuous=True,
    random_state=42
)

print("Calculando LIME + Probabilidades para cada embrião...")
prob_euploidia = []

for i in range(len(X_scaled)):
    _ = explainer.explain_instance(X_scaled[i], modelo.predict_proba, num_features=len(colunas_treinadas))
    
    prob = modelo.predict_proba(X_scaled[i].reshape(1, -1))[0][1]
    prob_euploidia.append(round(prob * 100, 2))

df["Classe_Prevista"] = classes_preditas
df["Prob_Euploidia_LIME"] = prob_euploidia

prob_raw = modelo.predict_proba(X_scaled)[:, 1]
acc = accuracy_score(y_true, classes_preditas)
auc = roc_auc_score(y_true, prob_raw)

cm = confusion_matrix(y_true, classes_preditas)
tn, fp, fn, tp = cm.ravel()
recall_euploide = tp / (tp + fn) if (tp + fn) > 0 else 0
recall_aneuploide = tn / (tn + fp) if (tn + fp) > 0 else 0

print("\n=== MÉTRICAS DE DESEMPENHO ===")
print(f"Acurácia: {acc:.3f}")
print(f"AUC (baseado na sigmoid): {auc:.3f}")
print(f"Recall Euploide (Sensibilidade): {recall_euploide:.3f}")
print(f"Recall Aneuploide (Especificidade): {recall_aneuploide:.3f}")
print("\n=== Classification Report ===")
print(classification_report(y_true, classes_preditas))

plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Aneuploide (0)", "Euploide (1)"],
            yticklabels=["Aneuploide (0)", "Euploide (1)"])
plt.xlabel("Predito")
plt.ylabel("Real")
plt.title("Matriz de Confusão")
plt.tight_layout()
plt.show()

fpr, tpr, thresholds = roc_curve(y_true, prob_raw)
plt.figure()
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc:.2f})")
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
plt.xlabel("Falso Positivo (1 - Especificidade)")
plt.ylabel("Verdadeiro Positivo (Sensibilidade)")
plt.title("Curva ROC")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df.to_excel("Planilha_Com_LIME_Porcentagem.xlsx", index=False)

print("\n Concluído com sucesso!")
print("Arquivo salvo como: Planilha_Com_LIME_Porcentagem.xlsx")