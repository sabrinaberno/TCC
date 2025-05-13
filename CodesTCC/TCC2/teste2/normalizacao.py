import pandas as pd
import numpy as np

file_path = "PlanilhaNumerica.xlsx"  
data = pd.read_excel(file_path)

numeric_columns = data.select_dtypes(include=[np.number]).columns

normalized_data = data.copy()

for col in numeric_columns:
    mean = data[col].mean()
    std = data[col].std()
    normalized_data[col] = (data[col] - mean) / std

output_file = "Planilha_normalizada.xlsx"
normalized_data.to_excel(output_file, index=False)

print(f"Normalização concluída. Arquivo salvo como: {output_file}")