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

## Explicação do código
Este código realiza a ampliação de dados (Data Augmentation) utilizando o método de Simulação de Monte Carlo para gerar novas amostras para o conjunto de dados de treinamento. A técnica de Monte Carlo é aplicada para gerar valores aleatórios com base nas distribuições estatísticas das variáveis numéricas, aumentando a diversidade do conjunto de dados original.

### 1. **Importação das Bibliotecas Necessárias**:
O código começa importando as bibliotecas `pandas` e `numpy`, que são utilizadas para manipulação de dados e geração de números aleatórios, respectivamente.
```python
import pandas as pd
 import numpy as np
```

### 2. **Carregamento do Conjunto de Dados**: 
O conjunto de dados de treinamento é carregado a partir de um arquivo Excel ('dados_treinamento.xlsx') utilizando a função ```pd.read_excel()```. O arquivo contém os dados que serão ampliados.
```python
train_data_path = 'dados_treinamento.xlsx'
df_train = pd.read_excel(train_data_path)
```

### 3. **Identificação das Colunas Numéricas e Categóricas**:
O código identifica as colunas numéricas e categóricas no conjunto de dados original.
```python
numerical_columns = df_train.select_dtypes(include=['float64', 'int64']).columns
categorical_columns = df_train.select_dtypes(include=['object']).columns
```
* O código seleciona as colunas numéricas (tipo ```float64``` e ```int64```) e as colunas categóricas (tipo object) do conjunto de dados.

### 4. **Definição do Fator de Aumento de Dados**:
```python
augmentation_factor = 3
num_new_samples = len(df_train) * augmentation_factor
```
* Aqui, o fator de aumento de dados é definido como 3, o que significa que o conjunto de dados final terá 3 vezes o número de amostras do conjunto original. ```num_new_samples``` calcula quantas novas amostras serão geradas multiplicando o número de linhas do conjunto de dados original pelo fator de aumento.

### 5. **Geração de Novas Amostras para as Colunas Numéricas**
```python
new_samples = {}
for col in numerical_columns:
    mean = df_train[col].mean()
    std = df_train[col].std()
    new_samples[col] = np.random.normal(loc=mean, scale=std, size=num_new_samples)
```
* ```new_samples = {}```: Cria um dicionário vazio para armazenar as novas amostras.
* O loop ```for col in numerical_columns```: percorre cada coluna numérica do conjunto de dados.
    * ```df_train[col].mean()```: Calcula a média da coluna col.
    * ```df_train[col].std()```: Calcula o desvio padrão da coluna col.
    * ```np.random.normal(loc=mean, scale=std, size=num_new_samples)```: Gera novas amostras para essa coluna seguindo uma distribuição normal, com a média e o desvio padrão calculados a partir do conjunto original. O número de amostras geradas será igual a ```num_new_samples```.
 
### 6. **Criação de um DataFrame com as Novas Amostras Numéricas**:
```python
df_new_samples = pd.DataFrame(new_samples)
```
* Aqui, o dicionário ```new_samples``` é convertido em um DataFrame ```df_new_samples```, que contém as novas amostras numéricas geradas.

### 7. ** Geração de Novas Amostras para as Colunas Categóricas**:
```python
for col in categorical_columns:
    replicated_values = np.random.choice(df_train[col], size=num_new_samples, replace=True)
    df_new_samples[col] = replicated_values
```
* O loop ```for col in categorical_columns```: percorre cada coluna categórica.
* ```np.random.choice(df_train[col], size=num_new_samples, replace=True)```: Para cada coluna categórica, essa linha seleciona aleatoriamente valores da coluna original para gerar novas amostras, com reposição (```replace=True```). Ou seja, o mesmo valor pode ser selecionado mais de uma vez.
* As novas amostras são atribuídas ao DataFrame ```df_new_samples``` na coluna correspondente.

### 8. **Combinação dos Dados Originais e Novos**:
```python
df_augmented = pd.concat([df_train, df_new_samples], ignore_index=True)
```
* A função ```pd.concat``` é usada para concatenar o DataFrame original ```df_train``` com as novas amostras ```df_new_samples```. O parâmetro ```ignore_index=True``` garante que o índice do DataFrame seja reajustado para o novo conjunto de dados combinado, sem manter os índices originais.

### 9. **Salvamento do Conjunto de Dados Aumentado**
```python
augmented_data_path = 'dados_treinamento_aumentado.xlsx'
df_augmented.to_excel(augmented_data_path, index=False)
```
* O conjunto de dados aumentado, agora armazenado em ```df_augmented```, é salvo em um novo arquivo Excel chamado ```dados_treinamento_aumentado.xlsx```. O parâmetro ```index=False``` evita que o índice do DataFrame seja incluído no arquivo Excel.

### O que é o Método de Aritmética de Monte Carlo?
* O Monte Carlo é uma técnica matemática que utiliza números aleatórios para simular processos estocásticos. Ele é amplamente utilizado para resolver problemas que envolvem incerteza e variabilidade, especialmente em cenários onde métodos tradicionais de resolução analítica são inviáveis. O MCA permite uma análise mais detalhada, gerando uma gama de resultados possíveis e suas respectivas probabilidades.
* Como o MCA é Aplicado ao Aumento de Dados?
    * **Distribuições Estatísticas**: A partir dos dados originais, são calculadas as distribuições de cada variável numérica. Essas distribuições são usadas para gerar novos valores aleatórios, que serão adicionados aos dados originais.
    * **Geração de Novos Valores**: O método np.random.normal() é usado para gerar novos dados a partir de uma distribuição normal, com a mesma média e desvio padrão das variáveis originais.
    * **Variação nas Variáveis**: Essas novas amostras sintéticas criam variações nas variáveis, aumentando a diversidade do conjunto de dados e, consequentemente, a capacidade de generalização de modelos de aprendizado de máquina.
    * **Validação do Conjunto Aumentado**: Após gerar o conjunto de dados aumentado, é importante validar se as novas amostras respeitam as características estatísticas do conjunto original. Isso pode ser feito verificando a distribuição das variáveis numéricas e categóricas no conjunto de dados expandido.

## Executar o Código

Rode o arquvio python com esse comando:
```python
python data_augmentation.py
```

Voltar aqui
