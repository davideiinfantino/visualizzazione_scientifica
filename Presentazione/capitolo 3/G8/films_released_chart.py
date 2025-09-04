import pandas as pd
import matplotlib.pyplot as plt
import os

# Ottiene il percorso del file CSV nella stessa directory dello script
csv_path = os.path.join(os.path.dirname(__file__), "films_released_worldwide_2010_2022.csv")
df = pd.read_csv(csv_path)

# Conversione dei campi numerici
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["FilmsReleasedWorldwide"] = pd.to_numeric(df["FilmsReleasedWorldwide"], errors="coerce")

# Rimuove eventuali valori NaN
df = df.dropna()

# Ordina per anno
df = df.sort_values("Year")

# Plot
plt.figure(figsize=(9,6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Plot come istogramma per differenziarlo dagli altri grafici
# Evidenzia il 2020 con un colore diverso per mostrare l'impatto COVID
colors = ["#cc0000" if year != 2020 else "#ff4444" for year in df["Year"]]
hatches = ["" if year != 2020 else "///" for year in df["Year"]]
bars = plt.bar(df["Year"], df["FilmsReleasedWorldwide"], color=colors, alpha=0.8, 
               edgecolor="#8b0000", linewidth=1, hatch=hatches)

# Crea elementi per la legenda
import matplotlib.patches as mpatches
normal_patch = mpatches.Patch(color='#cc0000', alpha=0.8, label='Film Rilasciati')
covid_patch = mpatches.Patch(color='#ff4444', alpha=0.8, hatch='///', label='Anno COVID (2020)')

plt.xlabel("Anno", fontsize=12)
plt.ylabel("Numero di Film Rilasciati", fontsize=12)
plt.grid(True, alpha=0.3)

# Etichette per punti chiave: primo, picco pre-COVID (2019), minimo COVID (2020), e ultimo
first_year = df["Year"].iloc[0]
first_value = df["FilmsReleasedWorldwide"].iloc[0]

# Trova il picco del 2019
peak_2019 = df[df["Year"] == 2019]
if not peak_2019.empty:
    peak_value = peak_2019["FilmsReleasedWorldwide"].iloc[0]
    plt.text(2019, peak_value + 200, f"{peak_value}", ha="center", va="bottom", fontsize=9, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# Trova il minimo del 2020
min_2020 = df[df["Year"] == 2020]
if not min_2020.empty:
    min_value = min_2020["FilmsReleasedWorldwide"].iloc[0]
    plt.text(2020, min_value + 200, f"{min_value}", ha="center", va="bottom", fontsize=9, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# Ultimo anno
last_year = df["Year"].iloc[-1]
last_value = df["FilmsReleasedWorldwide"].iloc[-1]
plt.text(last_year, last_value + 200, f"{last_value}", ha="center", va="bottom", fontsize=9, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cc0000", alpha=0.8))

# Aggiungi la legenda con styling estetico sopra il grafico
plt.legend(handles=[normal_patch, covid_patch], loc='lower center', bbox_to_anchor=(0.5, 1.05), frameon=True, fancybox=True, shadow=True, 
           facecolor='white', edgecolor='#cccccc', framealpha=0.95, 
           fontsize=8, borderpad=0.5, ncol=2)

# Rimuovi margini superiori e destro
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Configura le proporzioni del subplot
plt.subplots_adjust(left=0.11, bottom=0.083, right=0.617, top=0.61, wspace=0.2, hspace=0.2)

# Salva il grafico come immagine
output_path = os.path.join(os.path.dirname(__file__), "films_released_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Grafico salvato come: {output_path}")

plt.show()
