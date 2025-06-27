import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

# === CARREGAR OS DADOS E MODELO ===
df = pd.read_excel("PlanilhaNumerica.xlsx")
X = df.drop(columns=["Ploidia"])
y = df["Ploidia"]

modelo = joblib.load("melhor_modelo_mlp_20250610_113659.pkl")
scaler = joblib.load("scaler_mlp_20250610_113659.pkl")

# === SPLIT E ESCALONAMENTO ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
X_test_scaled = scaler.transform(X_test)

# === CALCULA PROBABILIDADES ===
probs = modelo.predict_proba(X_test_scaled)[:, 1]

# === DEFINIR VÁRIOS LIMIARES ===
limiares = [0.3, 0.4, 0.5, 0.6, 0.7]

# === ANALISAR CLASSIFICAÇÕES PARA CADA LIMIAR ===
print("\nAnálise das probabilidades e classificações por limiar:\n")
for i, prob in enumerate(probs):
    print(f"Embrião {i+1}:")
    print(f"  Probabilidade de Euploidia: {prob:.2f}")
    for limiar in limiares:
        classe = 1 if prob >= limiar else 0
        print(f"    → Limiar {limiar:.1f}: Classificado como {'Euploide' if classe == 1 else 'Aneuploide'}")
    print("-" * 40)
