# Código da Atividade 4

O código em Python a seguir foi utilizado para realizar a divisão dos dados:
```python
import pandas as pd
import numpy as np

# Carregar os dados da planilha
df = pd.read_excel("sua_planilha.xlsx")

# Embaralhar os dados
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Calcular o número de linhas para cada conjunto
n_total = len(df)
n_train = int(n_total * 0.7)
n_val = int(n_total * 0.15)
n_test = n_total - n_train - n_val  # Garantir que soma seja igual ao total

# Dividir os dados
train_data = df.iloc[:n_train]
val_data = df.iloc[n_train:n_train + n_val]
test_data = df.iloc[n_train + n_val:]

# Salvar os conjuntos em novos arquivos, se necessário
train_data.to_excel("dados_treinamento.xlsx", index=False) # False para evitar que o índice seja salvo no arquivo
val_data.to_excel("dados_validacao.xlsx", index=False)
test_data.to_excel("dados_teste.xlsx", index=False)

print(f"Conjunto de Treinamento: {len(train_data)} linhas")
print(f"Conjunto de Validação: {len(val_data)} linhas")
print(f"Conjunto de Teste: {len(test_data)} linhas")

```

## Explicação do código
Este código tem como objetivo dividir um conjunto de dados em três partes: treinamento, validação e teste. Além disso, ele embaralha os dados antes de fazer a divisão e, por fim, salva esses conjuntos em novos arquivos Excel. A seguir, explicamos cada parte do código com mais detalhes.

### 1. Importação das Bibliotecas

```python
import pandas as pd
import numpy as np
```
* ```pandas```: Biblioteca fundamental para a manipulação e análise de dados estruturados, como tabelas. Ela oferece diversas funções para trabalhar com dados tabulares, incluindo leitura e escrita de arquivos Excel, filtragem de dados, entre outras funcionalidades.
* ```numpy```: Biblioteca utilizada principalmente para operações em arrays multidimensionais e funções matemáticas. Embora esteja importada neste código, ela não é utilizada diretamente, mas pode ser útil para manipulações numéricas no contexto de dados.

### 2. Leitura do Arquivo Excel
```python
df = pd.read_excel("Planilha_normalizada.xlsx")
```
* ```pd.read_excel()```: Esta função lê o arquivo Excel especificado no caminho "Planilha_normalizada.xlsx". Os dados do arquivo são carregados no DataFrame df. O DataFrame é uma estrutura de dados bidimensional, como uma tabela, onde as linhas representam registros e as colunas representam variáveis.

### 3. Embaralhamento dos Dados
```python
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
```
* ```df.sample(frac=1)```: A função ```sample()``` seleciona uma amostra aleatória do DataFrame. O parâmetro frac=1 indica que queremos embaralhar 100% dos dados (ou seja, todas as linhas).
* ```random_state=42```: Este parâmetro define uma "semente" para o gerador de números aleatórios. Isso garante que o embaralhamento seja reprodutível, ou seja, se o código for executado várias vezes com esse valor de random_state, o embaralhamento será o mesmo.
* ```reset_index(drop=True)```: Após o embaralhamento, o índice do DataFrame é redefinido. O parâmetro drop=True evita que o índice antigo seja adicionado como uma nova coluna no DataFrame.

### 4. Cálculo das Proporções para Divisão dos Dados
```python
n_total = len(df)
n_train = int(n_total * 0.7)
n_val = int(n_total * 0.15)
n_test = n_total - n_train - n_val
```
* ```n_total = len(df)```: O comando ```len(df)``` retorna o número total de linhas (instâncias) no DataFrame df, ou seja, a quantidade de dados disponíveis para dividir.
* ```n_train = int(n_total * 0.7)```: A variável ```n_train``` calcula 70% do total de dados para o conjunto de treinamento. ```int()``` é usado para garantir que o valor seja um número inteiro.
* ```n_val = int(n_total * 0.15)```: A variável ```n_val``` calcula 15% do total de dados para o conjunto de validação.
* ```n_test = n_total - n_train - n_val```: O conjunto de teste recebe os dados restantes após a divisão para treinamento e validação, ou seja, os 15% restantes.

### 5. Divisão dos Dados em Conjuntos de Treinamento, Validação e Teste
```python
train_data = df.iloc[:n_train]
val_data = df.iloc[n_train:n_train + n_val]
test_data = df.iloc[n_train + n_val:]
```
* ```train_data = df.iloc[:n_train]```: O DataFrame df é dividido usando o método iloc, que seleciona linhas com base em seus índices. Aqui, ele seleciona as primeiras n_train linhas para o conjunto de treinamento.
* ```val_data = df.iloc[n_train:n_train + n_val]```: O conjunto de validação recebe as próximas ```n_val``` linhas, que vão de ```n_train``` até ```n_train + n_val```.
* ```test_data = df.iloc[n_train + n_val:]```: O conjunto de teste recebe as linhas restantes a partir de ```n_train + n_val``` até o final do DataFrame.

### 6. Salvando os Conjuntos de Dados em Arquivos Excel
```python
train_data.to_excel("dados_treinamento.xlsx", index=False)
val_data.to_excel("dados_validacao.xlsx", index=False)
test_data.to_excel("dados_teste.xlsx", index=False)
```
* ```train_data.to_excel("dados_treinamento.xlsx", index=False)```: O conjunto de dados de treinamento é salvo em um arquivo Excel chamado "dados_treinamento.xlsx". O parâmetro index=False evita que o índice do DataFrame seja incluído como uma coluna adicional no arquivo.
* ```val_data.to_excel("dados_validacao.xlsx", index=False)```: O conjunto de validação é salvo no arquivo "dados_validacao.xlsx".
* ```test_data.to_excel("dados_teste.xlsx", index=False)```: O conjunto de teste é salvo no arquivo "dados_teste.xlsx".

### 7. Exibindo o Número de Linhas de Cada Conjunto
```python
print(f"Conjunto de Treinamento: {len(train_data)} linhas")
print(f"Conjunto de Validação: {len(val_data)} linhas")
print(f"Conjunto de Teste: {len(test_data)} linhas")
```
* ```print(f"Conjunto de Treinamento: {len(train_data)} linhas")```: Exibe o número de linhas do conjunto de treinamento.
* ```print(f"Conjunto de Validação: {len(val_data)} linhas")```: Exibe o número de linhas do conjunto de validação.
* ```print(f"Conjunto de Teste: {len(test_data)} linhas")```: Exibe o número de linhas do conjunto de teste.

## Executar o Código

Instale as dependências, caso necessário:
```python
pip install pandas openpyxl
```

Por fim, rode o arquvio python com esse comando:
```python
python normalizacao_zscore.py
```
---

O código em Python a seguir foi utilizado para realizar o aumento dos dados de treinamento:
```python
import pandas as pd
import numpy as np

# Carregar o conjunto de dados de treinamento
train_data_path = 'dados_treinamento.xlsx'  # Substitua pelo caminho correto
df_train = pd.read_excel(train_data_path)

# Identificar colunas numéricas e categóricas
numerical_columns = df_train.select_dtypes(include=['float64', 'int64']).columns
categorical_columns = df_train.select_dtypes(include=['object']).columns

# Definir o número de amostras adicionais a serem geradas
augmentation_factor = 2  # Cada linha original será replicada com variações
num_new_samples = len(df_train) * augmentation_factor

# Gerar novos dados para as colunas numéricas usando distribuições normais
new_samples = {}
for col in numerical_columns:
    mean = df_train[col].mean()
    std = df_train[col].std()
    new_samples[col] = np.random.normal(loc=mean, scale=std, size=num_new_samples)

# Criar um DataFrame para os novos dados numéricos
df_new_samples = pd.DataFrame(new_samples)

# Adicionar valores para as colunas categóricas, replicando proporcionalmente os existentes
for col in categorical_columns:
    replicated_values = np.random.choice(df_train[col], size=num_new_samples, replace=True)
    df_new_samples[col] = replicated_values

# Concatenar os dados originais e os novos dados
df_augmented = pd.concat([df_train, df_new_samples], ignore_index=True)

# Salvar o conjunto de dados expandido
augmented_data_path = 'dados_treinamento_aumentado.xlsx'
df_augmented.to_excel(augmented_data_path, index=False)

print(f"Conjunto de dados aumentado salvo em: {augmented_data_path}")
```

## Executar o Código

Rode o arquvio python com esse comando:
```python
python data_augmentation.py
```

Voltar aqui
