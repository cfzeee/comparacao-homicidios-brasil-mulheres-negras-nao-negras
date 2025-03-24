import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Carregar os arquivos CSV corretamente
df_negras = pd.read_csv("/Users/cfz/Downloads/negras.csv", sep=";")
df_nao_negras = pd.read_csv("/Users/cfz/Downloads/nao-negras.csv", sep=";")

# 2️⃣ Garantir que a coluna "período" não tem espaços extras
df_negras.columns = df_negras.columns.str.strip()
df_nao_negras.columns = df_nao_negras.columns.str.strip()

# 3️⃣ Fazer o merge dos DataFrames pela coluna "período"
df_comparacao = df_negras.merge(df_nao_negras, on="período", suffixes=("_negras", "_nao_negras"))

# 4️⃣ Manter apenas as colunas necessárias
df_comparacao = df_comparacao[["período", "valor_negras", "valor_nao_negras"]]

# 5️⃣ Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(df_comparacao["período"], df_comparacao["valor_negras"], label="Negras", marker="o")
plt.plot(df_comparacao["período"], df_comparacao["valor_nao_negras"], label="Não Negras", marker="o")
plt.xlabel("Ano")
plt.ylabel("Taxa de Homicídios")
plt.title("Comparação de Homicídios de Mulheres Negras e Não Negras")
plt.legend()
plt.grid()
plt.show()
