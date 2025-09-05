import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "netflix_top10_series_official.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Rank"] = pd.to_numeric(df["Rank"], errors="coerce")
df["Views"] = pd.to_numeric(df["Views"], errors="coerce")
df["HoursViewed"] = pd.to_numeric(df["HoursViewed"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per rank
df = df.sort_values("Rank")

# Converte le visualizzazioni in milioni per una migliore leggibilità
df["ViewsMillions"] = df["Views"] / 1000000

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Crea il grafico a barre orizzontali
bars = plt.barh(df["Title"], df["ViewsMillions"], color="#cc0000", alpha=0.7, 
                edgecolor="#8b0000", linewidth=1, label="Visualizzazioni Netflix")

plt.xlabel("Visualizzazioni (Milioni)", fontsize=12)
plt.ylabel("Serie TV", fontsize=12)
plt.grid(True, alpha=0.3, axis='x')

# Aggiungi la legenda con styling estetico
plt.legend(loc='lower right', frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Inverti l'ordine dell'asse y per avere il rank 1 in alto
plt.gca().invert_yaxis()

# Configura le proporzioni del subplot (massima altezza)
plt.subplots_adjust(left=0.25, bottom=0.083, right=0.85, top=0.99, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "netflix_top10_series_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
