import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "europe_cinema_admissions_2010_2022.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["AdmissionsMillions"] = pd.to_numeric(df["AdmissionsMillions"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Lista dei paesi
countries = df["Country"].unique()

# Definisce colori per ogni paese
colors = {
    "France": "#cc0000",
    "Germany": "#ff9900", 
    "Italy": "#009900",
    "Spain": "#9900cc",
    "UK": "#0066cc"
}

# Plot
plt.figure(figsize=(12,8), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Plot per ogni paese
for country in countries:
    country_data = df[df["Country"] == country]
    if not country_data.empty:
        plt.plot(country_data["Year"], country_data["AdmissionsMillions"], 
                marker="o", linestyle="-", color=colors[country], linewidth=2, 
                markersize=5, label=country, alpha=0.8)
        
        # Colora l'area sotto la curva con trasparenza
        plt.fill_between(country_data["Year"], country_data["AdmissionsMillions"], 
                        color=colors[country], alpha=0.15)

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Ammissioni Cinema (Milioni)", fontsize=12)
plt.grid(True, alpha=0.3)

# Evidenzia il crollo del 2020 con una linea verticale
plt.axvline(x=2020, color='red', linestyle='--', alpha=0.5, linewidth=1)
plt.text(2020.1, 180, "COVID-19", rotation=90, fontsize=9, color='red', alpha=0.7)

# Aggiungi etichette per alcuni valori chiave nel 2020
for country in ["Italy", "Germany"]:
    country_2020 = df[(df["Country"] == country) & (df["Year"] == 2020)]
    if not country_2020.empty:
        value_2020 = country_2020["AdmissionsMillions"].iloc[0]
        plt.text(2020, value_2020 + 5, f"{value_2020}M", ha="center", va="bottom", 
                 fontsize=8, fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.2", facecolor="white", 
                          edgecolor=colors[country], alpha=0.8))

# Aggiungi la legenda con styling estetico
plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=9, borderpad=0.6, ncol=3)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot
plt.tight_layout()

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "europe_cinema_admissions_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
