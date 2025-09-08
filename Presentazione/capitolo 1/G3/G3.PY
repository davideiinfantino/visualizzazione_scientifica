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
top_countries = 15  # Ridotto per migliore leggibilità
pivot_data_top = pivot_data_sorted.head(top_countries)

# Verifica se l'Italia è nei dati e la aggiunge se non c'è
if 'Italy' in pivot_data_filtered.index and 'Italy' not in pivot_data_top.index:
    # Rimuove l'ultimo paese e aggiunge l'Italia
    pivot_data_top = pivot_data_top.drop(pivot_data_top.index[-1])
    italy_data = pivot_data_filtered.loc[['Italy']]
    pivot_data_top = pd.concat([pivot_data_top, italy_data])
    print("🇮🇹 Italia aggiunta forzatamente alla visualizzazione!")

# Dataset finale per la visualizzazione
pivot_data_display = pivot_data_top

print(f"\nCreando heatmap per i top {len(pivot_data_display)} paesi...")
print("Paesi inclusi:")
for country in pivot_data_display.index:
    avg_val = pivot_data_display.loc[country].mean()
    print(f"- {country}: {avg_val:.0f} schermi medi")

# Crea la heatmap con dimensioni migliorate
plt.figure(figsize=(12,8), facecolor='white')

# Usa il colormap personalizzato con i rossi
colors = ['#ffeeee', '#ffcccc', '#ff9999', '#ff6666', '#cc0000', '#990000', '#660000']
custom_cmap = sns.blend_palette(colors, as_cmap=True)

# Prendi solo i top 15 paesi per una migliore leggibilità
pivot_data_display = pivot_data_top.head(15)

# Crea la heatmap con annotazioni più grandi
heatmap = sns.heatmap(
    pivot_data_display,
    annot=True,
    fmt='.0f',
    cmap=custom_cmap,
    cbar_kws={'label': 'Numero di Schermi', 'shrink': 0.8},
    linewidths=1,
    linecolor='white',
    annot_kws={'size': 10, 'weight': 'bold', 'color': 'black'},
    square=False,
    xticklabels=True,
    yticklabels=True
)

# Personalizza il grafico
plt.xlabel('Anno', fontsize=14, fontweight='bold')
plt.ylabel('Paese', fontsize=14, fontweight='bold')

# Ruota le etichette dell'asse x per una migliore leggibilità
plt.xticks(rotation=0, fontsize=12)
plt.yticks(rotation=0, fontsize=11)

# Titolo del grafico
plt.title('Schermi Cinematografici per Paese (2000-2010)', fontsize=16, fontweight='bold', pad=20)

# Configura le proporzioni del subplot per migliore visibilità
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.9, top=0.85, wspace=0.2, hspace=0.2)

# Salva il grafico
output_path = os.path.join(os.path.dirname(__file__), "G3_heatmap.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"\nHeatmap salvata come: {output_path}")

# Mostra il grafico
plt.show()

print("\n📊 HEATMAP GENERATA!")
print("=" * 50)
print("CARATTERISTICHE:")
print("• Colori rossi: Intensità proporzionale al numero di schermi")
print("• Righe: Paesi (ordinati per numero medio di schermi)")
print("• Colonne: Anni dal 2000 al 2010")
print("• Numeri: Valori esatti di schermi per paese/anno")
print("• Top 15 paesi con più schermi cinematografici")
print(f"• Risoluzione alta (300 DPI) salvata in: {output_path}")
