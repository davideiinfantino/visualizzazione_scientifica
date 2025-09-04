import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "svod_penetration_world_2010_2020.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["SVOD_Penetration_Percent"] = pd.to_numeric(df["SVOD_Penetration_Percent"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Seleziona alcuni paesi rappresentativi per non sovraffollare il grafico
selected_countries = ["USA", "UK", "Germany", "France", "Italy", "China", "Japan"]
df_selected = df[df["Country"].isin(selected_countries)]

# Definisce colori per ogni paese
colors = {
    "USA": "#cc0000",
    "UK": "#0066cc", 
    "Germany": "#ff9900",
    "France": "#009900",
    "Italy": "#9900cc",
    "China": "#ff0066",
    "Japan": "#00cc99"
}

# Plot
plt.figure(figsize=(12,8), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Plot per ogni paese
for country in selected_countries:
    country_data = df_selected[df_selected["Country"] == country]
    if not country_data.empty:
        plt.plot(country_data["Year"], country_data["SVOD_Penetration_Percent"], 
                marker="o", linestyle="-", color=colors[country], linewidth=2, 
                markersize=5, label=country, alpha=0.8)
        
        # Colora l'area sotto la curva con trasparenza
        plt.fill_between(country_data["Year"], country_data["SVOD_Penetration_Percent"], 
                        color=colors[country], alpha=0.15)

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Penetrazione SVOD (%)", fontsize=12)
plt.grid(True, alpha=0.3)

# Trova il paese con il valore più alto nel 2020
last_year_data = df_selected[df_selected["Year"] == 2020]
if not last_year_data.empty:
    highest_country = last_year_data.loc[last_year_data["SVOD_Penetration_Percent"].idxmax()]
    country_name = highest_country["Country"]
    last_value = highest_country["SVOD_Penetration_Percent"]
    
    # Aggiungi etichetta solo per il paese con il valore più alto
    plt.text(2020 + 0.1, last_value, f"{last_value}%", 
            ha="left", va="center", fontsize=9, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", 
                     edgecolor=colors[country_name], alpha=0.8))

# Aggiungi la legenda con styling estetico
plt.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=10, borderpad=0.8, ncol=2)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot
plt.tight_layout()

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "svod_penetration_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
