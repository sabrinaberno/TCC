# Código da Atividade 3

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
import os

# Passo 1: Gerar a planilha de correlações
file_path = "Planilha_normalizada.xlsx"
data = pd.read_excel(file_path)

numerical_columns = [
    "Idade", "Estágio", "Morfo", "KIDScore", "t2", "t3", "t4", "t5", "t8", "tSC", "tSB", "tB", "cc2 (t3-t2)", 
    "cc3 (t5-t3)", "t5-t2", "s2 (t4-t3)", "s3 (t8-t5)", "tSC-t8", "tB-tSB", "Ploidia"
]

numerical_columns = [col for col in numerical_columns if col in data.columns]

generated_pairs = set()
results = []

# Gerar a lista de correlações
for col1 in numerical_columns:
    for col2 in numerical_columns:
        if col1 != col2:  # Não exclui mais a correlação inversa
            coef, _ = spearmanr(data[col1], data[col2], nan_policy="omit")
            results.append({"Variable 1": col1, "Variable 2": col2, "Spearman Coefficient": coef})

# Salvar as correlações em um arquivo Excel
correlation_df = pd.DataFrame(results)
output_file = "correlation_results.xlsx"
correlation_df.to_excel(output_file, index=False)
print(f"\nResultados salvos no arquivo: {output_file}")

# Passo 2: Gerar os gráficos a partir do arquivo de correlação

# Ler o arquivo de correlação gerado
correlation_df = pd.read_excel(output_file)

# Criar diretório para armazenar gráficos, caso não exista
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Criar o documento do Word
doc = Document()
doc.add_heading('Correlação de Spearman - Embriões', 0)

color_var1 = "lightgreen"
color_var2 = "darkblue"

# Para cada linha no dataframe de correlação
for index, row in correlation_df.iterrows():
    var1, var2 = row['Variable 1'], row['Variable 2']
    coef = row['Spearman Coefficient']

    # Gerar gráfico apenas se o coeficiente de correlação não for nulo
    if not pd.isnull(coef):
        plt.figure(figsize=(6, 4))

        # Gerar o gráfico de dispersão
        plt.scatter(data[var1], data[var2], alpha=0.6, c=color_var1, label=f'{var1} vs {var2}', marker='o')
        plt.scatter(data[var2], data[var1], alpha=0.6, c=color_var2, label=f'{var2}', marker='x')
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.legend(title="Variáveis")

        # Nome do arquivo PDF
        sanitized_var1 = var1.replace(" ", "_").replace("/", "-")
        sanitized_var2 = var2.replace(" ", "_").replace("/", "-")
        pdf_filename = f"grafico_{sanitized_var1}_vs_{sanitized_var2}_Spearman_{coef:.2f}.pdf"
        pdf_path = os.path.join(output_dir, pdf_filename)
        plt.savefig(pdf_path, format="pdf")
        plt.close()

        # Adicionar informação ao documento Word
        doc.add_heading(f'Correlação entre {var1} e {var2}', level=1)
        doc.add_paragraph(f'Coeficiente de Spearman: {coef:.2f}')
        doc.add_paragraph(f'O gráfico correspondente foi salvo como: {pdf_filename}')

# Salvar o documento Word
output_word = "relatorio_correlacoes.docx"
doc.save(output_word)

print(f"\nRelatório gerado e salvo em: {output_word}")
```

## Executar o Código "normalizacao_zscore.py"

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

## Explicação Técninca do código 

### Visão Geral do Código
Este código executa três operações principais:
 1. Cálculo da Correlação de Spearman entre variáveis numéricas de um dataset armazenado em um arquivo Excel (.xlsx).
 2. Geração de gráficos de dispersão para cada par de variáveis correlacionadas.
 3. Criação de um relatório em formato .docx, documentando os resultados e referenciando os gráficos gerados.

### 1. **Importação das Bibliotecas**
```python
import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
from docx import Document
import os
```
* ```pandas``` (```pd```): Manipulação e análise de dados, especialmente leitura e escrita de arquivos Excel.
* ```spearmanr``` (de ```scipy.stats```): O spearmanr calcula o coeficiente de correlação de Spearman, que mede a relação monotônica entre duas variáveis. Ele é útil quando você quer entender como duas variáveis estão associadas.
* ```matplotlib.pyplot``` (```plt```): Geração de gráficos de dispersão. O matplotlib é uma biblioteca poderosa para criar visualizações estáticas, interativas e animadas. O módulo pyplot fornece uma interface semelhante ao MATLAB para criar gráficos de forma simples.
* ```Document``` (de ```docx```): Criação e manipulação de documentos Word. A biblioteca python-docx permite criar, ler e manipular documentos do Microsoft Word programaticamente. Assim geramos o relatório automatizado.
* ```os```: Manipulação de diretórios e arquivos do sistema.

### 2. **Leitura dos Dados**
```python
file_path = "Planilha_normalizada.xlsx"
data = pd.read_excel(file_path)
```
* O método ```pd.read_excel(file_path)``` lê o arquivo Excel e converte em um DataFrame do Pandas, que é a estrutura de dados principal utilizada para análise. Ele automaticamente interpreta as planilhas do arquivo Excel, transformando-as em uma tabela estruturada.
* **Considerações**: Este método possui uma grande flexibilidade, sendo capaz de lidar com diferentes tipos de dados, como texto, números, datas e booleanos. 

### 3. **Definição das Colunas Numéricas**
```python
numerical_columns = [
    "Idade", "Estágio", "Morfo", "KIDScore", "t2", "t3", "t4", "t5", "t8", "tSC", "tSB", "tB", "cc2 (t3-t2)", 
    "cc3 (t5-t3)", "t5-t2", "s2 (t4-t3)", "s3 (t8-t5)", "tSC-t8", "tB-tSB", "Ploidia"
]
```
* É uma etapa fundamental para identificar quais colunas de um conjunto de dados serão tratadas como numéricas. Essas colunas são, geralmente, aquelas que contêm valores quantitativos e que podem ser utilizadas em cálculos ou análises estatísticas, como correlação.
* O que é numerical_columns?
    * É uma lista de strings, onde cada string representa o nome de uma coluna do conjunto de dados que contém valores numéricos.
    * Essas colunas serão usadas em etapas da análise de correlação.
```python
numerical_columns = [col for col in numerical_columns if col in data.columns]
```
* Filtramos ```numerical_columns``` para garantir que apenas colunas realmente presentes no DataFrame sejam consideradas.

### 4. **Cálculo da Correlação de Spearman**
```python
generated_pairs = set()
results = []

for col1 in numerical_columns:  # Itera sobre cada coluna como a primeira variável
    for col2 in numerical_columns:  # Itera sobre todas as colunas como a segunda variável
        if col1 != col2:  # Evita correlação de uma variável com ela mesma
            coef, _ = spearmanr(data[col1], data[col2], nan_policy="omit")  # Calcula correlação de Spearman
            results.append({"Variable 1": col1, "Variable 2": col2, "Spearman Coefficient": coef})  # Armazena o resultado
```
#### **1. Variáveis utilizadas**
1. **`generated_pairs = set()`**:
   - Inicialmente definida para evitar pares duplicados (correlação inversa, como `A vs B` e `B vs A`), mas não está sendo usada no trecho atual.

2. **`results = []`**:
   - Lista vazia para armazenar os resultados das correlações, cada um como um dicionário contendo:
     - **`Variable 1`**: Nome da primeira variável (coluna).
     - **`Variable 2`**: Nome da segunda variável (coluna).
     - **`Spearman Coefficient`**: Valor do coeficiente de Spearman entre elas.

#### **2. Funcionamento do loop**
O objetivo principal do loop é calcular as correlações entre todas as combinações de colunas listadas em **`numerical_columns`**, ignorando combinações onde as variáveis sejam iguais (`col1 != col2`).

##### **Detalhes das etapas:**
1. **`col1` e `col2`**:
   - `col1` é a coluna fixa na iteração externa.
   - `col2` varia sobre todas as colunas dentro da iteração interna.
2. **Evitar redundância:**
   - A condição `if col1 != col2` assegura que uma coluna não será comparada consigo mesma.
3. **`spearmanr(data[col1], data[col2], nan_policy="omit")`**:
   - Calcula o coeficiente de correlação de Spearman entre os valores de duas colunas.
   - **`nan_policy="omit"`**: Ignora valores ausentes (NaN) ao calcular a correlação.
4. **Armazenamento dos resultados:**
   - Cada resultado é um dicionário com:
     - **`"Variable 1"`**: Nome da primeira variável.
     - **`"Variable 2"`**: Nome da segunda variável.
     - **`"Spearman Coefficient"`**: Valor do coeficiente de Spearman calculado.

#### **3. Após o loop**
1. **Lista de resultados (`results`)**:
   - Após o loop, os resultados armazenados em `results` são transformados em um **DataFrame**:
   ```python
   correlation_df = pd.DataFrame(results)
   ```
2. **Criação do DataFrame:**
   - Este DataFrame permite salvar os resultados em Excel, processar estatísticas e visualizar os dados.

### 5. Criação do Diretório para Gráficos
```python
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)
```
* Este código cria um diretório chamado **`graficos`** no sistema de arquivos para armazenar os gráficos gerados. Caso o diretório já exista, ele evita erros.

### 6. Geração de Gráficos de Dispersão e Inserção no Documento Word
```python
for index, row in correlation_df.iterrows():
    var1, var2 = row['Variable 1'], row['Variable 2']
    coef = row['Spearman Coefficient']

    if not pd.isnull(coef):
        plt.figure(figsize=(6, 4))

        plt.scatter(data[var1], data[var2], alpha=0.6, c=color_var1, label=f'{var1} vs {var2}', marker='o')
        plt.scatter(data[var2], data[var1], alpha=0.6, c=color_var2, label=f'{var2}', marker='x')
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.legend(title="Variáveis")
```
#### **O que esse código faz?**
Este trecho percorre as linhas de um DataFrame chamado **`correlation_df`**, que contém informações sobre pares de variáveis e seus coeficientes de correlação de Spearman. Para cada linha:
1. Verifica se o coeficiente de correlação não é **NaN**.
2. Gera gráficos de dispersão entre os pares de variáveis presentes na linha.

#### 1. **Iteração sobre as linhas do DataFrame**:
   ```python
   for index, row in correlation_df.iterrows():
   ```
   - **`index`**: Índice da linha atual.
   - **`row`**: Objeto que representa a linha atual do DataFrame.
#### 2. **Acessa os dados da linha**:
   ```python
   var1, var2 = row['Variable 1'], row['Variable 2']
   coef = row['Spearman Coefficient']
   ```
   - **`var1` e `var2`**: Nomes das duas variáveis cujos dados serão plotados.
   - **`coef`**: Valor do coeficiente de correlação entre `var1` e `var2`.
#### 3. **Verifica se o coeficiente é válido**:
   ```python
   if not pd.isnull(coef):
   ```
   - O gráfico só é gerado se o coeficiente não for **NaN**.
#### 4. **Cria uma figura para o gráfico**:
   ```python
   plt.figure(figsize=(6, 4))
   ```
   - Define o tamanho do gráfico como 6 unidades de largura por 4 unidades de altura.
#### 5. **Gera gráficos de dispersão**:
   ```python
   plt.scatter(data[var1], data[var2], alpha=0.6, c=color_var1, label=f'{var1} vs {var2}', marker='o')
   plt.scatter(data[var2], data[var1], alpha=0.6, c=color_var2, label=f'{var2}', marker='x')
   ```
   - **`plt.scatter()`**: Cria gráficos de dispersão para visualizar a relação entre duas variáveis.
   - **Parâmetros principais**:
     - **`data[var1]` e `data[var2]`**: Dados das variáveis que serão plotados.
     - **`alpha=0.6`**: Define a transparência dos pontos no gráfico.
     - **`c`**: Define a cor dos pontos. Utiliza as variáveis `color_var1` e `color_var2`.
     - **`label`**: Rótulo para os pontos no gráfico.
     - **`marker`**: Define o formato dos marcadores (círculo ou "x").
#### 6. **Personaliza o gráfico**:
   ```python
   plt.xlabel(var1)
   plt.ylabel(var2)
   plt.legend(title="Variáveis")
   ```
   - **`plt.xlabel()` e `plt.ylabel()`**: Define os rótulos dos eixos X e Y, respectivamente.
   - **`plt.legend()`**: Adiciona uma legenda ao gráfico para identificar as variáveis.



