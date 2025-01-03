# Código da Atividade 3

## Objetivo Geral

O código tem como objetivo principal normalizar os dados numéricos presentes na planilha de dados dos embriões. A normalização é uma técnica comum em análise de dados que serve para transformar os dados em uma escala comum, facilitando a comparação entre diferentes variáveis e a aplicação de algoritmos de aprendizado de máquina.

## Por que Normalizar os Dados?
* **Comparabilidade**: Permite comparar variáveis com diferentes escalas (por exemplo, idade e t4).
* **Melhora em Algoritmos**: Muitos algoritmos de aprendizado de máquina assumem que os dados estão em uma escala similar.
* **Estabilidade Numérica**: Pode evitar problemas numéricos em alguns algoritmos.

O código em Python a seguir foi utilizado para realizar a análise descrita:
```python
import pandas as pd
import numpy as np

# Carregar a planilha
file_path = "PlanilhaDeDadosDosEmbriões4.xlsx" 
data = pd.read_excel(file_path)

# Identificar colunas numéricas
numeric_columns = data.select_dtypes(include=[np.number]).columns

# Copiar o DataFrame original para manter os dados inalterados
normalized_data = data.copy()

# Normalizar as colunas numéricas utilizando o Z-Score
for col in numeric_columns:
    mean = data[col].mean()
    std = data[col].std()
    normalized_data[col] = (data[col] - mean) / std

# Salvar o DataFrame normalizado em um novo arquivo Excel
output_file = "Planilha_normalizada.xlsx"
normalized_data.to_excel(output_file, index=False)

print(f"Normalização concluída. Arquivo salvo como: {output_file}")
```

## Executar o Código

Instale as dependências, caso necessário:
```python
pip install pandas numpy openpyxl
```

Por fim, rode o arquvio python com esse comando:
```python
python normalizacao_zscore.py
```