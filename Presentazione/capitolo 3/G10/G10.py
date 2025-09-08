import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "italy_cinema_admissions_2010_2022.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["AdmissionsMillionsItaly"] = pd.to_numeric(df["AdmissionsMillionsItaly"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Linea principale con etichetta per la legenda
plt.plot(df["Year"], df["AdmissionsMillionsItaly"], marker="o", linestyle="-", color="#cc0000", linewidth=2, markersize=6, label="Ammissioni Cinema Italia")

# Colora l'area sotto la curva senza etichetta per la legenda
plt.fill_between(df["Year"], df["AdmissionsMillionsItaly"], color="#cc0000", alpha=0.3)

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Ammissioni Cinema (Milioni)", fontsize=12)
plt.grid(True, alpha=0.3)

# Etichette per punti chiave: primo, picco 2019, minimo 2020, e ultimo
first_year = df["Year"].iloc[0]
first_value = df["AdmissionsMillionsItaly"].iloc[0]

# Trova il valore del 2019 (prima del COVID)
year_2019 = df[df["Year"] == 2019]
if not year_2019.empty:
    value_2019 = year_2019["AdmissionsMillionsItaly"].iloc[0]
    plt.text(2019, value_2019 + 4, f"{value_2019}M", ha="center", va="bottom", fontsize=9, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# Trova il minimo del 2020 (COVID)
year_2020 = df[df["Year"] == 2020]
if not year_2020.empty:
    value_2020 = year_2020["AdmissionsMillionsItaly"].iloc[0]
    plt.text(2020, value_2020 + 4, f"{value_2020}M", ha="center", va="bottom", fontsize=9, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# Ultimo anno (2021)
last_year = df["Year"].iloc[-1]
last_value = df["AdmissionsMillionsItaly"].iloc[-1]
plt.text(last_year, last_value + 4, f"{last_value}M", ha="center", va="bottom", fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

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
output_path = os.path.join(os.path.dirname(__file__), "italy_cinema_admissions_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
