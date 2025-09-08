import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "streaming_catalog_sizes_2015_2024.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["TitlesAvailable"] = pd.to_numeric(df["TitlesAvailable"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Lista delle piattaforme
platforms = df["Platform"].unique()

# Definisce colori per ogni piattaforma
colors = {
    "Netflix": "#cc0000",
    "Prime Video": "#ff9900", 
    "Disney+": "#0066cc",
    "Max (HBO Max)": "#9900cc",
    "Apple TV+": "#009900"
}

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Plot per ogni piattaforma
for platform in platforms:
    platform_data = df[df["Platform"] == platform]
    if not platform_data.empty:
        plt.plot(platform_data["Year"], platform_data["TitlesAvailable"], 
                marker="o", linestyle="-", color=colors[platform], linewidth=2, 
                markersize=5, label=platform, alpha=0.8)
        
        # Colora l'area sotto la curva con trasparenza
        plt.fill_between(platform_data["Year"], platform_data["TitlesAvailable"], 
                        color=colors[platform], alpha=0.15)

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Titoli Disponibili", fontsize=12)
plt.grid(True, alpha=0.3)

# Trova la piattaforma con il valore più alto nel 2024
data_2024 = df[df["Year"] == 2024]
if not data_2024.empty:
    highest_platform = data_2024.loc[data_2024["TitlesAvailable"].idxmax()]
    platform_name = highest_platform["Platform"]
    highest_value = highest_platform["TitlesAvailable"]
    
    # Aggiungi etichetta solo per la piattaforma con il valore più alto
    plt.text(2024, highest_value + 500, f"{highest_value}", ha="center", va="bottom", 
             fontsize=9, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", 
                      edgecolor=colors[platform_name], alpha=0.8))

# Aggiungi la legenda con styling estetico
plt.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.61, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "streaming_catalog_sizes_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
