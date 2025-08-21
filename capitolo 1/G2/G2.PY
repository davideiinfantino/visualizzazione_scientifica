import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "worldwide_box_office.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Releases"] = pd.to_numeric(df["Releases"], errors="coerce")

# Filtra i dati dal 2000 al 2010 e rimuove eventuali valori NaN
df = df[(df["Year"] >= 2000) & (df["Year"] <= 2010)].dropna()

# Ordina per anno
df = df.sort_values("Year")

# Crea il grafico a barre
plt.figure(figsize=(9, 6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

bars = plt.bar(df["Year"], df["Releases"], color="#cc0000", alpha=0.8, edgecolor="#cc0000", linewidth=2, label="Numero di Uscite")

plt.title("Numero di Uscite Cinematografiche (2000–2010)", fontsize=14)
plt.xlabel("Anno", fontsize=12)
plt.ylabel("Numero di Film Rilasciati", fontsize=12)
plt.grid(True, alpha=0.3)

# Aggiungi etichette sopra ogni barra con posizionamento ottimizzato
for bar, value in zip(bars, df["Releases"]):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 8, 
             f"{int(value)}", ha="center", va="bottom", fontsize=9, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# Imposta i limiti dell'asse y per dare spazio alle etichette
plt.ylim(0, max(df["Releases"]) * 1.15)

# Aggiungi la legenda con styling estetico
plt.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

plt.tight_layout()

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "releases_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico G2 salvato come: {output_path}")

plt.show()
