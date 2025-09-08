import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "budget_vs_boxoffice_2000_2024.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Budget_MUSD"] = pd.to_numeric(df["Budget_MUSD"], errors="coerce")
df["BoxOffice_MUSD"] = pd.to_numeric(df["BoxOffice_MUSD"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Crea il grafico scatter
plt.scatter(df["Budget_MUSD"], df["BoxOffice_MUSD"], color="#cc0000", alpha=0.6, 
           s=30, edgecolor="#8b0000", linewidth=0.5, label="Film (2000-2024)")

# Aggiungi una linea di tendenza
z = np.polyfit(df["Budget_MUSD"], df["BoxOffice_MUSD"], 1)
p = np.poly1d(z)
plt.plot(df["Budget_MUSD"], p(df["Budget_MUSD"]), color="#660000", linestyle="--", 
         linewidth=2, alpha=0.8, label="Linea di Tendenza")

plt.xlabel("Budget (Milioni USD)", fontsize=12)
plt.ylabel("Incassi Box Office (Milioni USD)", fontsize=12)
plt.grid(True, alpha=0.3)

# Aggiungi la legenda con styling estetico
plt.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot (stesse di G1)
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.61, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "budget_vs_boxoffice_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
