import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, classification_report, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Planilha_normalizada.xlsx")

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
probabilidades = modelo.predict_proba(X_scaled)[:, 1]
porcentagem_euploidia = (probabilidades * 100).round(2)

df["Classe_Prevista"] = classes_preditas
df["Porcentagem_Euploidia_Preditiva"] = porcentagem_euploidia

acc = accuracy_score(y_true, classes_preditas)
auc = roc_auc_score(y_true, probabilidades)

cm = confusion_matrix(y_true, classes_preditas)
tn, fp, fn, tp = cm.ravel()

recall_euploide = tp / (tp + fn) if (tp + fn) > 0 else 0
recall_aneuploide = tn / (tn + fp) if (tn + fp) > 0 else 0

print("\n=== MÉTRICAS DE DESEMPENHO ===")
print(f"Acurácia: {acc:.3f}")
print(f"AUC: {auc:.3f}")
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

fpr, tpr, thresholds = roc_curve(y_true, probabilidades)
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

df.to_excel("Planilha_Com_Classificacao_e_Porcentagem.xlsx", index=False)

print("\n✅ Concluído com sucesso!")
print("📄 Arquivo salvo como: Planilha_Com_Classificacao_e_Porcentagem.xlsx")