import pandas as pd
import numpy as np

df = pd.read_excel("Planilha_normalizada.xlsx")

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

n_total = len(df)
n_train = int(n_total * 0.7)
n_val = int(n_total * 0.15)
n_test = n_total - n_train - n_val 

train_data = df.iloc[:n_train]
val_data = df.iloc[n_train:n_train + n_val]
test_data = df.iloc[n_train + n_val:]

train_data.to_excel("dados_treinamento.xlsx", index=False)
val_data.to_excel("dados_validacao.xlsx", index=False)
test_data.to_excel("dados_teste.xlsx", index=False)

print(f"Conjunto de Treinamento: {len(train_data)} linhas")
print(f"Conjunto de Validação: {len(val_data)} linhas")
print(f"Conjunto de Teste: {len(test_data)} linhas")