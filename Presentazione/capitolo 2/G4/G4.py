import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "netflix_subscribers_2007_2020.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["NetflixSubscribersMillions"] = pd.to_numeric(df["NetflixSubscribersMillions"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Linea principale con etichetta per la legenda
plt.plot(df["Year"], df["NetflixSubscribersMillions"], marker="o", linestyle="-", color="#cc0000", linewidth=2, markersize=6, label="Abbonati Netflix")

# Colora l'area sotto la curva senza etichetta per la legenda
plt.fill_between(df["Year"], df["NetflixSubscribersMillions"], color="#cc0000", alpha=0.3)

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Abbonati Netflix (Milioni)", fontsize=12)
plt.grid(True, alpha=0.3)

# Etichette solo per il primo e l'ultimo punto
first_year = df["Year"].iloc[0]
first_value = df["NetflixSubscribersMillions"].iloc[0]
last_year = df["Year"].iloc[-1]
last_value = df["NetflixSubscribersMillions"].iloc[-1]

plt.text(first_year, first_value + 5, f"{first_value:.1f}M", ha="center", va="bottom", fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))
plt.text(last_year, last_value + 5, f"{last_value:.1f}M", ha="center", va="bottom", fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# Aggiungi la legenda con styling estetico
plt.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.61, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "netflix_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
