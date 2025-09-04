import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "boxoffice_vs_svod_2010_2021.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["GlobalBoxOffice_BillionUSD"] = pd.to_numeric(df["GlobalBoxOffice_BillionUSD"], errors="coerce")
df["GlobalSVODSubscribers_Millions"] = pd.to_numeric(df["GlobalSVODSubscribers_Millions"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Crea il grafico con doppio asse Y
fig, ax1 = plt.subplots(figsize=(9,6), facecolor='white')
ax1.set_facecolor('white')

# Primo asse Y - Box Office (sinistra)
color1 = '#cc0000'
ax1.set_xlabel('Anno', fontsize=12)
ax1.set_ylabel('Box Office Globale (Miliardi USD)', color=color1, fontsize=12)
line1 = ax1.plot(df["Year"], df["GlobalBoxOffice_BillionUSD"], marker="o", linestyle="-", 
                 color=color1, linewidth=2, markersize=6, label="Box Office Globale")
ax1.fill_between(df["Year"], df["GlobalBoxOffice_BillionUSD"], color=color1, alpha=0.2)
ax1.tick_params(axis='y', labelcolor=color1)

# Secondo asse Y - SVOD Subscribers (destra)
ax2 = ax1.twinx()
color2 = '#0066cc'
ax2.set_ylabel('Abbonati SVOD Globali (Milioni)', color=color2, fontsize=12)
line2 = ax2.plot(df["Year"], df["GlobalSVODSubscribers_Millions"], marker="o", linestyle="-", 
                 color=color2, linewidth=2, markersize=6, label="Abbonati SVOD Globali")
ax2.fill_between(df["Year"], df["GlobalSVODSubscribers_Millions"], color=color2, alpha=0.2)
ax2.tick_params(axis='y', labelcolor=color2)

# Griglia
ax1.grid(True, alpha=0.3)

# Etichette per punti chiave
# Box Office - primo e ultimo punto
box_first_year = df["Year"].iloc[0]
box_first_value = df["GlobalBoxOffice_BillionUSD"].iloc[0]
box_last_year = df["Year"].iloc[-1]
box_last_value = df["GlobalBoxOffice_BillionUSD"].iloc[-1]

ax1.text(box_first_year, box_first_value + 1.5, f"{box_first_value:.1f}B", ha="center", va="bottom", 
         fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=color1, alpha=0.8))
ax1.text(box_last_year, box_last_value + 1.5, f"{box_last_value:.1f}B", ha="center", va="bottom", 
         fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=color1, alpha=0.8))

# SVOD - primo e ultimo punto
svod_first_value = df["GlobalSVODSubscribers_Millions"].iloc[0]
svod_last_value = df["GlobalSVODSubscribers_Millions"].iloc[-1]

ax2.text(box_first_year, svod_first_value + 30, f"{svod_first_value}M", ha="center", va="bottom", 
         fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=color2, alpha=0.8))
ax2.text(box_last_year, svod_last_value + 30, f"{svod_last_value}M", ha="center", va="bottom", 
         fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=color2, alpha=0.8))

# Combina le legende di entrambi gli assi
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower center', bbox_to_anchor=(0.5, 1.02), 
           frameon=True, fancybox=True, shadow=True, facecolor='white', edgecolor='#cccccc', 
           framealpha=0.95, fontsize=8, borderpad=0.5, ncol=2)

# Rimuovi margini superiori e destro
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

# Configura le proporzioni del subplot
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.61, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "boxoffice_vs_svod_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
