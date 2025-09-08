import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "netflix_g14_official_extended.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["HoursViewed"] = pd.to_numeric(df["HoursViewed"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Raggruppa per tipo e calcola il totale delle ore
type_summary = df.groupby('Type')['HoursViewed'].sum()

# Converte in miliardi per leggibilità
type_summary_billions = type_summary / 1e9

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Crea il grafico a torta
colors = ['#8b0000', '#cc0000']  # Film, Series
wedges, texts, autotexts = plt.pie(type_summary_billions.values, 
                                   labels=['Film', 'Serie TV'], 
                                   colors=colors,
                                   autopct='%1.1f%%',
                                   startangle=90,
                                   explode=(0.05, 0.05),
                                   shadow=True,
                                   textprops={'fontsize': 11, 'fontweight': 'bold'})

# Personalizza le etichette delle percentuali
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Aggiungi legenda con i valori
legend_labels = [f'Film: {type_summary_billions["Film"]:.1f}B ore', 
                 f'Serie TV: {type_summary_billions["Series"]:.1f}B ore']
plt.legend(wedges, legend_labels, title="Ore Totali Visualizzate",
           loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),
           frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

# Configura le proporzioni del subplot (più alto)
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.92, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "netflix_comparison_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
