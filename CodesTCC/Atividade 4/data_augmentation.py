import pandas as pd
import numpy as np

train_data_path = 'dados_treinamento.xlsx'  
df_train = pd.read_excel(train_data_path)

numerical_columns = df_train.select_dtypes(include=['float64', 'int64']).columns
categorical_columns = df_train.select_dtypes(include=['object']).columns

augmentation_factor = 3  
num_new_samples = len(df_train) * augmentation_factor

new_samples = {}
for col in numerical_columns:
    mean = df_train[col].mean()
    std = df_train[col].std()
    new_samples[col] = np.random.normal(loc=mean, scale=std, size=num_new_samples)

df_new_samples = pd.DataFrame(new_samples)

for col in categorical_columns:
    replicated_values = np.random.choice(df_train[col], size=num_new_samples, replace=True)
    df_new_samples[col] = replicated_values

df_augmented = pd.concat([df_train, df_new_samples], ignore_index=True)

augmented_data_path = 'dados_treinamento_aumentado.xlsx'
df_augmented.to_excel(augmented_data_path, index=False)

print(f"Conjunto de dados aumentado salvo em: {augmented_data_path}")
