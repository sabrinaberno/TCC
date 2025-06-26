import pandas as pd
import numpy as np

file_path = "geral.xlsx"

data = pd.read_excel(file_path)

# Substituindo os valores da coluna 'Ploidia' de 'euploide' e 'aneuploide' para 1 e 0
data['Ploidia'] = data['Ploidia'].replace({'Euplóide': 1, 'Aneuplóide': 0})

# Removendo a letra D da coluna Estágio para ficar somente números representado o dia
data['Estágio'] = data['Estágio'].str.replace("D", "", regex=False)
data['Estágio'] = pd.to_numeric(data['Estágio'], errors='coerce')

# Substituindo a classificação Morfo pelo seu grupo de 1 a 4
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

# Aplicar a função diretamente na coluna 'Morfo'
data['Morfo'] = data['Morfo'].apply(classificar_morfo)

# Selecionando apenas as colunas numéricas
numeric_columns = data.select_dtypes(include=[np.number])

# Salvando em uma nova planilha
output_file = "PlanilhaNumerica.xlsx"
numeric_columns.to_excel(output_file, index=False)

print(f"Planilha somente com dados numéricos salva como: {output_file}")
