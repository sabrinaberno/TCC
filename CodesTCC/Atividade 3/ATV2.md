# Código da Atividade 2

## Objetivo Geral

O código Python tem como objetivo principal **identificar e analisar os fatores que influenciam a porcentagem de euploidia em embriões**, utilizando o coeficiente de Spearman como ferramenta estatística. Além disso, visa **estabelecer uma relação qualitativa e fundamentada cientificamente entre esses fatores e a ploidia embrionária**.

## Objetivos Específicos

1. **Identificação de relações:**
    - Determinar quais parâmetros apresentam a correlação mais forte (positiva ou negativa) com a porcentagem de euploidia.
    - Avaliar como esses parâmetros se relacionam entre si.
2. **Visualização de dados:**
    - Criar gráficos que evidenciem as variáveis mais influentes.
    - Visualizar padrões que suportem as relações monótonas entre as variáveis.
3. **Análise qualitativa:**
    - Gerar uma lista detalhada dos parâmetros identificados, com todos os gráficos de cada relação.

O código em Python a seguir foi utilizado para realizar a análise descrita:

```python
import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
from docx import Document
from docx.shared import Inches
import os

# Carregar os dados
file_path = "PlanilhaDeDadosDosEmbriões4.xlsx"
data = pd.read_excel(file_path)

# Selecionar apenas colunas numéricas relevantes
numerical_columns = [
    "Idade", "Estágio", "Morfo", "KIDScore", "t2", "t3", "t4", "t5", "t8", "tSC", "tSB", "tB", "cc2 (t3-t2)", 
    "cc3 (t5-t3)", "t5-t2", "s2 (t4-t3)", "s3 (t8-t5)", "tSC-t8", "tB-tSB", "Ploidia"
]

numerical_columns = [col for col in numerical_columns if col in data.columns]

# Lista para armazenar os resultados
generated_pairs = set()
results = []

# Calcular correlações
for col1 in numerical_columns:
    for col2 in numerical_columns:
        if col1 != col2 and (col1, col2) not in generated_pairs and (col2, col1) not in generated_pairs:  
            coef, _ = spearmanr(data[col1], data[col2], nan_policy="omit")
            results.append({"Variable 1": col1, "Variable 2": col2, "Spearman Coefficient": coef})
            generated_pairs.add((col1, col2))

# Salvar os resultados em um arquivo Excel
correlation_df = pd.DataFrame(results)
output_file = "correlation_results.xlsx"
correlation_df.to_excel(output_file, index=False)
print(f"\nResultados salvos no arquivo: {output_file}")

# Criar o documento Word para o relatório
doc = Document()
doc.add_heading('Correlação de Spearman - Embriões', 0)

# Diretório para salvar os gráficos
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Configurar cores dos gráficos
color_var1 = "lightgreen"
color_var2 = "darkblue"

# Gerar gráficos
for index, row in correlation_df.iterrows():
    var1, var2 = row['Variable 1'], row['Variable 2']
    coef = row['Spearman Coefficient']

    # Verificar se as variáveis são válidas para dispersão
    if pd.api.types.is_numeric_dtype(data[var1]) and pd.api.types.is_numeric_dtype(data[var2]):
        plt.figure(figsize=(6, 4))
        plt.scatter(data[var1], data[var2], alpha=0.6, c=color_var1, label=f'{var1}', marker='o')
        plt.scatter(data[var2], data[var1], alpha=0.6, c=color_var2, label=f'{var2}', marker='x')
        plt.title(f"Dispersão entre {var1} e {var2} (Coeficiente de Spearman: {coef:.2f})")
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.legend(title="Variáveis")

        img_path = os.path.join(output_dir, f"grafico_{var1}_{var2}.png")
        plt.savefig(img_path)
        plt.close()

        doc.add_heading(f'Correlação entre {var1} e {var2}', level=1)
        doc.add_paragraph(f'Coeficiente de Spearman: {coef:.2f}')
        doc.add_picture(img_path, width=Inches(5.0))

# Salvar o documento Word
output_word = "relatorio_correlacoes.docx"
doc.save(output_word)

print(f"\nRelatório gerado e salvo em: {output_word}")
```

## Rodar o Código

Instale as dependências, caso necessário:
```python
pip install pandas 
pip install scipy 
pip install pandas scipy  
pip list 
pip install --upgrade pandas # Caso necessário 
pip install matplotlib  
pip install openpyxl 
pip install pandas matplotlib python-docx
```

Por fim, rode o arquvio python com esse comando:
```python
python analise_spearman.py  
```

Voltar aqui