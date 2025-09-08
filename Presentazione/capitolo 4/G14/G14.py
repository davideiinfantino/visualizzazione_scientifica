import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "imdb_ratings_median_2000_2024.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["MedianRatingIMDb"] = pd.to_numeric(df["MedianRatingIMDb"], errors="coerce")
df["TitlesCount"] = pd.to_numeric(df["TitlesCount"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Crea il grafico a barre verticali
bars = plt.bar(df["Year"], df["MedianRatingIMDb"], color="#cc0000", alpha=0.7, 
               edgecolor="#8b0000", linewidth=1, label="Valutazione Mediana IMDb")

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Valutazione Mediana IMDb", fontsize=12)
plt.grid(True, alpha=0.3, axis='y')

# Etichette solo per alcuni anni chiave (ogni 5 anni)
key_years = [2000, 2005, 2010, 2015, 2020, 2024]
for year in key_years:
    if year in df["Year"].values:
        value = df[df["Year"] == year]["MedianRatingIMDb"].iloc[0]
        plt.text(year, value + 0.02, f"{value:.2f}", ha="center", va="bottom", 
                 fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# Ruota le etichette dell'asse x per una migliore leggibilità
plt.xticks(rotation=45)

# Aggiungi la legenda fuori dal grafico (a destra)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot (stretto a destra e massima altezza)
plt.subplots_adjust(left=0.08, bottom=0.15, right=0.68, top=0.99, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "imdb_ratings_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
