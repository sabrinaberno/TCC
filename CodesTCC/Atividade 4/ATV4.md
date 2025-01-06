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