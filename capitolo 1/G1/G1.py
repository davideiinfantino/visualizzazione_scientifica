import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "worldwide_box_office.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["TotalGross"] = pd.to_numeric(df["TotalGross"], errors="coerce")

# Filtra i dati dal 2000 al 2010 e rimuove eventuali valori NaN
df = df[(df["Year"] >= 2000) & (df["Year"] <= 2010)].dropna()

# Ordina per anno
df = df.sort_values("Year")

# Converte gli incassi in miliardi di $
df["TotalGross_Billion"] = df["TotalGross"] / 1e9

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Linea principale con etichetta per la legenda
plt.plot(df["Year"], df["TotalGross_Billion"], marker="o", linestyle="-", color="#cc0000", linewidth=2, markersize=6, label="Incassi Totali")

# Colora l'area sotto la curva senza etichetta per la legenda
plt.fill_between(df["Year"], df["TotalGross_Billion"], color="#cc0000", alpha=0.3)

plt.title("Botteghino Mondiale (2000–2010)", fontsize=14)
plt.xlabel("Anno", fontsize=12)
plt.ylabel("Incassi totali (Miliardi $)", fontsize=12)
plt.grid(True, alpha=0.3)

# Aggiungi etichette solo per il primo e ultimo punto con posizionamento ottimizzato
first_year = df["Year"].iloc[0]
first_value = df["TotalGross_Billion"].iloc[0]
last_year = df["Year"].iloc[-1]
last_value = df["TotalGross_Billion"].iloc[-1]

# Calcola l'offset dinamico basato sui valori del grafico
y_range = max(df["TotalGross_Billion"]) - min(df["TotalGross_Billion"])
offset = y_range * 0.12  # 12% del range come offset per più spazio

# Etichette con sfondo bianco e bordo per migliore leggibilità
plt.text(first_year, first_value + offset, f"{first_value:.1f}B", 
         ha="center", va="bottom", fontsize=10, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#cc0000", alpha=0.9))

plt.text(last_year, last_value + offset, f"{last_value:.1f}B", 
         ha="center", va="bottom", fontsize=10, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#cc0000", alpha=0.9))

# Aggiungi la legenda con styling estetico
plt.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

plt.tight_layout()

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "box_office_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
