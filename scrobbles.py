# Importando as bibliotecas
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Acessando a base de dados
df = pd.read_csv("https://raw.githubusercontent.com/wallacecarlis/arquivos_ml/main/artistas.csv")

# Gerando o gráfico no matplotlib
sns.set_style("darkgrid")
fig, ax = plt.subplots(figsize = (8, 3))

barras = sns.barplot(x = df.Faixas, y = df.Artistas, 
                     data = df, orient = "h", palette = "cividis")

# Calculando e inserindo uma linha de valor médio
media_faixas = df["Faixas"].mean()
ax.axvline(media_faixas, 
           color = "brown", 
           linestyle = "--", 
           linewidth = 2, 
           label = f"Média: {media_faixas:.2f}")

for i in barras.patches:
  ax.annotate(int(i.get_width()),
              xy = ((i.get_width() - (i.get_height() * 2000)),
                          i.get_x() + i.get_y() + (i.get_height() / 2)),
                          color = "white",
                          fontweight = "bold",
                          va = "center_baseline",
                          ha = "right")
  
for i in range(len(df)):
  valor = df.iloc[i, 1]
  artista = df.iloc[i, 0]
  ax.text(valor - valor + 5000, i, artista, fontsize = 10, fontweight = "bold", color = "white", va = "center")

ax.text(0, -1.5, "Quantidade de faixas acessadas por artistas", fontsize = 16, color = "#253760", fontweight = "bold")
plt.text(0, -1, "$\\bf{Artistas - Last FM}$\n", va = "top", ha = "left", fontsize = 10, color = "grey")
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
ax.yaxis.grid(False)
ax.xaxis.grid(False)
plt.tight_layout()

# Visualizando no streamlit
st.title("Scrobbels - Music")
st.pyplot(fig)