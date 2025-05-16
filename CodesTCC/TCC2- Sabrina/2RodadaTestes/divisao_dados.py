import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

df = pd.read_excel("Planilha_normalizada.xlsx")

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

coluna_classe = 'Ploidia'  

# Divisão 80/20 com estratificação (preservando proporção das classes)
train_data, val_data = train_test_split(
    df,
    test_size=0.2,
    stratify=df[coluna_classe],
    random_state=42
)

# Quantidade mínima de exemplos na classe menos representada no treino
min_count = train_data[coluna_classe].value_counts().min()

# Lista para armazenar os grupos balanceados e os descartados
balanced_groups = []
discarded_groups = []

# Para cada classe, faz o undersampling e separa os descartados
for classe, group in train_data.groupby(coluna_classe):
    balanced = resample(
        group,
        replace=False,
        n_samples=min_count,
        random_state=42
    )
    balanced_groups.append(balanced)
    
    # Descarta = tudo que não está em balanced
    discarded = group.drop(balanced.index)
    discarded_groups.append(discarded)

# Concatena os grupos balanceados para formar o treino balanceado
balanced_train_data = pd.concat(balanced_groups).sample(frac=1, random_state=42).reset_index(drop=True)

# Concatena os grupos descartados
discarded_data = pd.concat(discarded_groups)

# Adiciona os dados descartados ao conjunto de validacao
val_data_expanded = pd.concat([val_data, discarded_data]).sample(frac=1, random_state=42).reset_index(drop=True)

balanced_train_data.to_excel("dados_treinamento.xlsx", index=False)
val_data_expanded.to_excel("dados_validacao.xlsx", index=False)

print(f"Conjunto de Treinamento Balanceado: {len(balanced_train_data)} linhas")
print(balanced_train_data[coluna_classe].value_counts())
print(f"Conjunto de Validação Expandido (com descartados): {len(val_data_expanded)} linhas")
print(val_data_expanded[coluna_classe].value_counts())
