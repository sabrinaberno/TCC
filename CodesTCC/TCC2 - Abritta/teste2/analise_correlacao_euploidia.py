
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados da planilha com data augmentation
df = pd.read_excel("dados_treinamento_aumentado.xlsx")

# Verificar se a coluna alvo existe
coluna_alvo = "porcentagem_euploidia" if "porcentagem_euploidia" in df.columns else df.columns[-1]

# Calcular correlação de Pearson entre variáveis e a variável-alvo
correlacoes = df.corr(numeric_only=True)[coluna_alvo].drop(coluna_alvo).sort_values(ascending=False)

# Exibir top 10 correlações positivas
print("🔝 Top 10 correlações mais fortes (positivas):")
print(correlacoes.head(10))

# Exibir top 10 correlações negativas
print("\n🔻 Top 10 correlações mais fracas (negativas):")
print(correlacoes.tail(10))

# Gerar gráfico de correlação
plt.figure(figsize=(10, 8))
sns.barplot(x=correlacoes.values, y=correlacoes.index, palette="viridis")
plt.title("Correlação entre variáveis de entrada e porcentagem de euploidia")
plt.xlabel("Correlação de Pearson")
plt.ylabel("Variáveis")
plt.tight_layout()
plt.grid(True, axis='x')
plt.show()
