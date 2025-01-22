# Código da Atividade 2

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

# Carregar a planilha de dados dos embriões
file_path = "PlanilhaDeDadosDosEmbriões4.xlsx"  
data = pd.read_excel(file_path)

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

## Executar o Código "normalizacao_zscore.py"

1. Instale as dependências, caso necessário:
```python
pip install pandas numpy openpyxl
```
2. Coloque uma planilha de dados no local:
```python
file_path = "ColoqueSuaPlanilhaAqui.xlsx"  
```
3. Por fim, rode o arquvio python "divisao_dados.py" com esse comando:
```python
python normalizacao_zscore.py
```

## Explicação Técninca do código 
Este código em Importação das Bibliotecas **Python** utiliza as bibliotecas ```pandas``` e ```numpy``` para ler, normalizar e salvar um conjunto de dados em um arquivo Excel. Em seguida, está uma explicação técnica e detalhada do código:

1. **Importação das Bibliotecas**
```python
import pandas as pd
import numpy as np
```
* Pandas (```pd```): Uma biblioteca robusta e eficiente para análise e manipulação de dados estruturados, especialmente tabelas (DataFrames). O Pandas é fundamental para o tratamento de dados em Python, oferecendo operações de leitura/escrita, filtragem, transformação, agregação e estatísticas.
* Numpy (```np```): Uma biblioteca para computação científica que fornece objetos de arrays multidimensionais e funções de álgebra linear. Aqui, numpy é utilizado para identificar colunas numéricas e para operações de cálculo estatístico (média e desvio padrão).

2. **Leitura do Arquivo Excel**
```python
file_path = "PlanilhaDeDadosDosEmbriões4.xlsx"  
data = pd.read_excel(file_path)
```
* O método ```pd.read_excel(file_path)``` lê o arquivo Excel e converte em um DataFrame do Pandas, que é a estrutura de dados principal utilizada para análise. Ele automaticamente interpreta as planilhas do arquivo Excel, transformando-as em uma tabela estruturada.
* **Considerações**: Este método possui uma grande flexibilidade, sendo capaz de lidar com diferentes tipos de dados, como texto, números, datas e booleanos. 

3. **Seleção das Colunas Numéricas**
```python
numeric_columns = data.select_dtypes(include=[np.number]).columns
```
* O método ```select_dtypes``` permite filtrar as colunas do DataFrame baseadas no tipo de dados. A cláusula ```include=[np.number]``` faz com que apenas as colunas que contêm dados numéricos sejam selecionadas. O resultado é uma lista contendo os nomes das colunas numéricas.
* **Considerações**: Embora o método seja eficiente para este propósito, vale ressaltar que ele considera apenas os tipos de dados numéricos reconhecidos pelo ```numpy``` e ```pandas```, como ```inteiros``` e ```floats```. 

4. **Cópia dos Dados para Normalização**
```python
normalized_data = data.copy()
```
* A função ```copy()``` cria uma cópia profunda do DataFrame ```data```, ou seja, cria uma nova instância do DataFrame com os mesmos dados. Isso garante que o DataFrame original não seja modificado durante o processo de normalização.
* **Considerações**: A cópia é necessária para evitar efeitos colaterais sobre o DataFrame original. Como o Pandas trabalha com referências, alterações diretas em ```data``` durante o loop de normalização poderiam modificar os dados originais, o que não é desejado.

5. **Normalização das Colunas Numéricas**
```python
for col in numeric_columns:
    mean = data[col].mean()
    std = data[col].std()
    normalized_data[col] = (data[col] - mean) / std
```
* A normalização é realizada em cada coluna numérica identificada anteriormente. O loop itera sobre todas as colunas numéricas, e para cada coluna:
    * *Cálculo da Média*: A média dos valores é calculada com o método ```mean()```, que fornece a média aritmética dos dados.
    * *Cálculo do Desvio Padrão*: O desvio padrão é calculado com o método ```std()```, que mede a dispersão dos dados em relação à média.
    * *Aplicação da Fórmula Z-score*: A normalização de cada valor da coluna é realizada pela fórmula:

        $$
            Z = \frac{X - \mu}{\sigma}
        $$

        Onde:
        - \( Z \) é o valor normalizado,
        - \( X \) é o valor original da célula,
        - \( μ \) é a média da coluna,
        - \( σ \) é o desvio padrão da coluna.

* **Considerações**: A normalização z-score é uma técnica comum quando os dados possuem diferentes escalas e é importante colocá-los em uma distribuição comum. 

6. **Salvamento do DataFrame Normalizado**
```python
output_file = "Planilha_normalizada.xlsx"
normalized_data.to_excel(output_file, index=False)
```
* O DataFrame normalizado é exportado para um novo arquivo Excel utilizando o método ```to_excel()```. O parâmetro ```index=False``` garante que o índice do DataFrame não seja incluído na planilha exportada, o que é desejável para evitar a inclusão de uma coluna extra.
