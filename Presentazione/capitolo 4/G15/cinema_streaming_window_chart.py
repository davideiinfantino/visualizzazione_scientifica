import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "cinema_to_streaming_window_2000_2024.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["WindowDays"] = pd.to_numeric(df["WindowDays"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Linea principale con etichetta per la legenda
plt.plot(df["Year"], df["WindowDays"], marker="o", linestyle="-", color="#cc0000", linewidth=2, markersize=6, label="Finestra Cinema-Streaming (giorni)")

# Colora l'area sotto la curva senza etichetta per la legenda
plt.fill_between(df["Year"], df["WindowDays"], color="#cc0000", alpha=0.3)

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Giorni di Finestra", fontsize=12)
plt.grid(True, alpha=0.3)

# Aggiungi la legenda con styling estetico (stessa posizione di G1)
plt.legend(loc='upper right', frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot (stesse di G1)
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.61, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "cinema_streaming_window_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
