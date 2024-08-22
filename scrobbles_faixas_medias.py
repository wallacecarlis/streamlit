import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Carregando o DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/wallacecarlis/arquivos_ml/main/artistas.csv")

# Configurações do Seaborn
sns.set_style("darkgrid")

# Gráfico 1: Linha de valor médio
fig1, ax1 = plt.subplots(figsize=(8, 3))
barras1 = sns.barplot(x = "Faixas", y = "Artistas", 
                      data = df, orient = "h", palette = "cividis")

# Calculando o valor médio das faixas
media_faixas = df['Faixas'].mean()

# Adicionando a linha de valor médio ao gráfico 1
ax1.axvline(media_faixas, color = 'brown', linestyle = '--', linewidth = 2, 
            label = f"Média: {media_faixas:.2f}")

# Inserindo valores dentro das barras
for i in barras1.patches:
    ax1.annotate(int(i.get_width()),
                 xy=((i.get_width() - (i.get_height() * 2000)),
                     i.get_y() + (i.get_height() / 2)),
                 color = "white",
                 fontweight = "bold",
                 va = "center_baseline",
                 ha = "right")

# Inserindo labels dentro das barras
for i in range(len(df)):
  valor = df.iloc[i, 1]
  artista = df.iloc[i, 0]
  ax1.text(valor - valor + 5000, i, artista, fontsize = 10, 
           fontweight = "bold", color = "white", va = "center")

ax1.text(0, -1.5, "Quantidade de faixas acessadas por artistas", 
         fontsize = 16, color = "#253760", fontweight = "bold")
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
ax1.yaxis.grid(False)
ax1.xaxis.grid(False)
ax1.set_ylabel("")
plt.tight_layout()

############# gráfico 2 ######################

# Gráfico 2: Faixa de valores médios
fig2, ax2 = plt.subplots(figsize=(8, 3))
barras2 = sns.barplot(x = "Faixas", y = "Artistas", 
                      data = df, orient = "h", palette = "cividis")

# Definindo a faixa ao redor da média (2% abaixo e 2% acima)
limite_inferior = media_faixas * 0.98
limite_superior = media_faixas * 1.02

# Adicionando a faixa de valores ao gráfico 2
ax2.axvspan(limite_inferior, limite_superior, color = "brown", alpha = 0.3, 
            label = f"Faixa Média: {limite_inferior:.2f} - {limite_superior:.2f}")

# Inserindo valores dentro das barras
for i in barras2.patches:
    if hasattr(i, 'get_width'):
       ax2.annotate(int(i.get_width()),
                     xy=((i.get_width() - (i.get_height() * 2000)),
                         i.get_y() + (i.get_height() / 2)),
                     color = "white",
                     fontweight = "bold",
                     va = "center_baseline",
                     ha = "right")

# Inserindo labels dentro das barras
for i in range(len(df)):
  valor = df.iloc[i, 1]
  artista = df.iloc[i, 0]
  ax2.text(valor - valor + 5000, i, artista, fontsize = 10, 
           fontweight = "bold", color = "white", va = "center")

ax2.text(0, -1.5, "Quantidade de faixas acessadas por artistas", 
         fontsize = 16, color = "#253760", fontweight = "bold")
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
ax2.yaxis.grid(False)
ax2.xaxis.grid(False)
plt.tight_layout()

# Exibindo os gráficos no Streamlit
st.title("Visualização de Dados com Streamlit, Matplotlib e Seaborn")
st.subheader("Linha de Média")
st.pyplot(fig1)

st.subheader("Faixa de Média")
st.pyplot(fig2)
