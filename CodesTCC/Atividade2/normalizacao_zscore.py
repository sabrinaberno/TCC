import pandas as pd
import numpy as np

# === LEITURA E PRÉ-PROCESSAMENTO ===
file_path = "teste2.xlsx"  # Altere o nome conforme o arquivo correto

data = pd.read_excel(file_path)

# Substituindo os valores da coluna 'Ploidia' de 'Euploide' e 'Aneuplóide' para 0 e 1
data['Ploidia'] = data['Ploidia'].replace({'Euplóide': 1, 'Aneuplóide': 0})

# Removendo a letra D da coluna Estágio para ficar somente números representando o dia
data['Estágio'] = data['Estágio'].str.replace("D", "", regex=False)
data['Estágio'] = pd.to_numeric(data['Estágio'], errors='coerce')

# Função para classificar Morfo
def classificar_morfo(valor):
    prefixo = valor[0]
    sufixo = valor[1:]

    if sufixo == "AA" and prefixo in "3456":
        return 1  # Excelente
    elif sufixo in ["AB", "BA"] and prefixo in "3456":
        return 2  # Bom
    elif sufixo in ["BB", "AC", "CA"] and prefixo in "3456":
        return 3  # Médio
    else:
        return 4  # Ruim

# Aplicando classificação na coluna Morfo
data['Morfo'] = data['Morfo'].apply(classificar_morfo)

# Selecionando apenas as colunas numéricas
numeric_data = data.select_dtypes(include=[np.number])

# Salvando apenas os dados numéricos em planilha
numeric_file = "PlanilhaNumerica.xlsx"
numeric_data.to_excel(numeric_file, index=False)
print(f"Planilha somente com dados numéricos salva como: {numeric_file}")

# === NORMALIZAÇÃO Z-SCORE ===

# Calculando normalização Z-score para as colunas numéricas
normalized_data = numeric_data.copy()

for col in normalized_data.columns:
    mean = normalized_data[col].mean()
    std = normalized_data[col].std()
    normalized_data[col] = (normalized_data[col] - mean) / std

# Salvando a planilha normalizada
normalized_file = "Planilha_normalizada.xlsx"
normalized_data.to_excel(normalized_file, index=False)
print(f"Normalização concluída. Arquivo salvo como: {normalized_file}")