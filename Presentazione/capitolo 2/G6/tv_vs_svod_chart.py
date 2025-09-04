import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "tv_vs_svod_minutes_2010_2020.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["TV_Minutes"] = pd.to_numeric(df["TV_Minutes"], errors="coerce")
df["SVOD_Minutes"] = pd.to_numeric(df["SVOD_Minutes"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Seleziona USA come paese rappresentativo (leader del mercato streaming)
df_usa = df[df["Country"] == "USA"]

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Linea per TV tradizionale
plt.plot(df_usa["Year"], df_usa["TV_Minutes"], marker="o", linestyle="-", color="#cc0000", linewidth=2, markersize=6, label="TV Tradizionale")

# Linea per SVOD
plt.plot(df_usa["Year"], df_usa["SVOD_Minutes"], marker="o", linestyle="-", color="#0066cc", linewidth=2, markersize=6, label="SVOD/Streaming")

# Colora l'area sotto le curve senza etichetta per la legenda
plt.fill_between(df_usa["Year"], df_usa["TV_Minutes"], color="#cc0000", alpha=0.2)
plt.fill_between(df_usa["Year"], df_usa["SVOD_Minutes"], color="#0066cc", alpha=0.2)

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Minuti di visione giornalieri", fontsize=12)
plt.grid(True, alpha=0.3)

# Etichette solo per il primo e l'ultimo punto di entrambe le serie
# TV Tradizionale
tv_first_year = df_usa["Year"].iloc[0]
tv_first_value = df_usa["TV_Minutes"].iloc[0]
tv_last_year = df_usa["Year"].iloc[-1]
tv_last_value = df_usa["TV_Minutes"].iloc[-1]

plt.text(tv_first_year, tv_first_value + 8, f"{tv_first_value:.0f}min", ha="center", va="bottom", fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))
plt.text(tv_last_year, tv_last_value + 8, f"{tv_last_value:.0f}min", ha="center", va="bottom", fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# SVOD
svod_first_value = df_usa["SVOD_Minutes"].iloc[0]
svod_last_value = df_usa["SVOD_Minutes"].iloc[-1]

plt.text(tv_first_year, svod_first_value + 8, f"{svod_first_value:.0f}min", ha="center", va="bottom", fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#0066cc", alpha=0.8))
plt.text(tv_last_year, svod_last_value + 8, f"{svod_last_value:.0f}min", ha="center", va="bottom", fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#0066cc", alpha=0.8))

# Aggiungi la legenda con styling estetico sopra il grafico
plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=8, borderpad=0.5, ncol=2)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.61, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "tv_vs_svod_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
