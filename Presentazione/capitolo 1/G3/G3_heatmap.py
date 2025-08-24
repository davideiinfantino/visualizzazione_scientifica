import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "unesco_cinema_worldwide_2000_2010.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Screens"] = pd.to_numeric(df["Screens"], errors="coerce")
df["FeatureFilmsProduced"] = pd.to_numeric(df["FeatureFilmsProduced"], errors="coerce")

# Filtra i dati e rimuove eventuali valori NaN
df = df.dropna()

print("Dati disponibili:")
print(df.head())

# Crea una matrice pivot con Years come colonne e Countries come righe
pivot_data = df.pivot_table(
    index='Country', 
    columns='Year', 
    values='Screens', 
    aggfunc='mean',
    fill_value=0
)

# Filtra solo i paesi con dati significativi (almeno 3 anni di dati)
countries_with_data = pivot_data.sum(axis=1)
countries_filtered = countries_with_data[countries_with_data > 0].index
pivot_data_filtered = pivot_data.loc[countries_filtered]

# Ordina i paesi per numero medio di schermi (dal maggiore al minore)
avg_screens = pivot_data_filtered.mean(axis=1).sort_values(ascending=False)
pivot_data_sorted = pivot_data_filtered.loc[avg_screens.index]

# Forza l'inclusione dell'Italia se non è nei top paesi
top_countries = 20
pivot_data_top = pivot_data_sorted.head(top_countries)

# Verifica se l'Italia è nei dati e la aggiunge se non c'è
if 'Italy' in pivot_data_filtered.index and 'Italy' not in pivot_data_top.index:
    # Rimuove l'ultimo paese e aggiunge l'Italia
    pivot_data_top = pivot_data_top.drop(pivot_data_top.index[-1])
    italy_data = pivot_data_filtered.loc[['Italy']]
    pivot_data_top = pd.concat([pivot_data_top, italy_data])
    print("🇮🇹 Italia aggiunta forzatamente alla visualizzazione!")

print(f"\nCreando heatmap per i top {len(pivot_data_top)} paesi...")
print("Paesi inclusi:")
for country in pivot_data_top.index:
    avg_val = pivot_data_top.loc[country].mean()
    print(f"- {country}: {avg_val:.0f} schermi medi")

# Crea la heatmap
plt.figure(figsize=(14, 10), facecolor='white')

# Usa il colormap personalizzato con i rossi
colors = ['#ffcccc', '#ff9999', '#ff6666', '#cc0000', '#990000', '#660000']
custom_cmap = sns.blend_palette(colors, as_cmap=True)

# Crea la heatmap con annotazioni
heatmap = sns.heatmap(
    pivot_data_top,
    annot=True,
    fmt='.0f',
    cmap=custom_cmap,
    cbar_kws={'label': 'Numero di Schermi'},
    linewidths=0.5,
    linecolor='white',
    annot_kws={'size': 8, 'weight': 'bold'},
    square=False
)

# Personalizza il grafico
plt.xlabel('Anno', fontsize=12, fontweight='bold')
plt.ylabel('Paese', fontsize=12, fontweight='bold')

# Ruota le etichette dell'asse x per una migliore leggibilità
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Configura le proporzioni del subplot
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.61, wspace=0.2, hspace=0.2)

# Salva il grafico
output_path = os.path.join(os.path.dirname(__file__), "G3_heatmap.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"\nHeatmap salvata come: {output_path}")

# Mostra il grafico
plt.show()

print(f"\n📊 HEATMAP GENERATA!")
print("=" * 50)
print("CARATTERISTICHE:")
print("• Colori rossi: Intensità proporzionale al numero di schermi")
print("• Righe: Paesi (ordinati per numero medio di schermi)")
print("• Colonne: Anni dal 2000 al 2010")
print("• Numeri: Valori esatti di schermi per paese/anno")
print("• Top 20 paesi con più schermi cinematografici")
print(f"• Risoluzione alta (300 DPI) salvata in: {output_path}")
