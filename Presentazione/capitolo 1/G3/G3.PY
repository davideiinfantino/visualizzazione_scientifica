import pandas as pd
import plotly.graph_objects as go
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

# Calcola la media per paese nel periodo 2000-2010 per gli schermi
screens_avg = df.groupby("Country")["Screens"].mean().reset_index()
screens_avg.columns = ["Country", "AvgScreens"]

# Mappatura completa dei nomi dei paesi per il codice ISO
country_mapping = {
    'USA': 'United States',
    'UK': 'United Kingdom', 
    'Germany': 'Germany',
    'France': 'France',
    'Italy': 'Italy',
    'India': 'India',
    'China': 'China',
    'Japan': 'Japan',
    'Brazil': 'Brazil',
    'Canada': 'Canada',
    'Spain': 'Spain',
    'Russia': 'Russia',
    'Mexico': 'Mexico',
    'Australia': 'Australia',
    'South Korea': 'South Korea',
    'Argentina': 'Argentina',
    'Turkey': 'Turkey',
    'South Africa': 'South Africa',
    'Nigeria': 'Nigeria',
    'Egypt': 'Egypt',
    'Sweden': 'Sweden',
    'Norway': 'Norway',
    'Denmark': 'Denmark',
    'Finland': 'Finland',
    'Poland': 'Poland',
    'Netherlands': 'Netherlands',
    'Belgium': 'Belgium',
    'Switzerland': 'Switzerland',
    'Austria': 'Austria',
    'Portugal': 'Portugal',
    'Greece': 'Greece',
    'Ireland': 'Ireland',
    'Czech Republic': 'Czech Republic',
    'Hungary': 'Hungary',
    'Romania': 'Romania',
    'Bulgaria': 'Bulgaria',
    'Slovakia': 'Slovakia',
    'Slovenia': 'Slovenia',
    'Croatia': 'Croatia',
    'Serbia': 'Serbia',
    'Ukraine': 'Ukraine',
    'Belarus': 'Belarus',
    'Lithuania': 'Lithuania',
    'Latvia': 'Latvia',
    'Estonia': 'Estonia',
    'Chile': 'Chile',
    'Colombia': 'Colombia',
    'Peru': 'Peru',
    'Venezuela': 'Venezuela',
    'Ecuador': 'Ecuador',
    'Uruguay': 'Uruguay',
    'Paraguay': 'Paraguay',
    'Bolivia': 'Bolivia',
    'Morocco': 'Morocco',
    'Algeria': 'Algeria',
    'Tunisia': 'Tunisia',
    'Kenya': 'Kenya',
    'Ethiopia': 'Ethiopia',
    'Ghana': 'Ghana',
    'Ivory Coast': 'Cote d\'Ivoire',
    'Tanzania': 'Tanzania',
    'Uganda': 'Uganda',
    'Thailand': 'Thailand',
    'Vietnam': 'Vietnam',
    'Philippines': 'Philippines',
    'Malaysia': 'Malaysia',
    'Indonesia': 'Indonesia',
    'Pakistan': 'Pakistan',
    'Bangladesh': 'Bangladesh',
    'Iran': 'Iran',
    'Iraq': 'Iraq'
}

screens_avg["CountryISO"] = screens_avg["Country"].map(country_mapping)

print("Dati disponibili:")
print(screens_avg)

# Configurazioni per diverse viste continentali
continental_views = {
    "Europa": {"lon": 10, "lat": 50, "title": "Schermi Cinematografici - Europa (Media 2000-2010)"},
    "Nord_America": {"lon": -100, "lat": 45, "title": "Schermi Cinematografici - Nord America (Media 2000-2010)"},
    "Sud_America": {"lon": -60, "lat": -15, "title": "Schermi Cinematografici - Sud America (Media 2000-2010)"},
    "Asia": {"lon": 100, "lat": 30, "title": "Schermi Cinematografici - Asia (Media 2000-2010)"},
    "Africa": {"lon": 20, "lat": 0, "title": "Schermi Cinematografici - Africa (Media 2000-2010)"},
    "Oceania": {"lon": 135, "lat": -25, "title": "Schermi Cinematografici - Oceania (Media 2000-2010)"}
}

# Crea una figura per ogni continente
figures = {}
output_paths = {}

for continent, config in continental_views.items():
    fig = go.Figure(data=go.Choropleth(
        locations=screens_avg["CountryISO"],
        z=screens_avg["AvgScreens"],
        locationmode='country names',
        colorscale=[[0, '#ffcccc'], [0.5, '#cc0000'], [1, '#660000']],
        colorbar_title="Schermi Medi",
        hovertemplate='<b>%{location}</b><br>Schermi: %{z:.0f}<extra></extra>',
    ))
    
    fig.update_layout(
        title=config["title"],
        geo=go.layout.Geo(
            showframe=False,
            showcoastlines=True,
            coastlinecolor="white",
            showland=True,
            landcolor='lightgray',
            showocean=True,
            oceancolor='lightblue',
            projection_type='orthographic',
            projection_rotation={"lon": config["lon"], "lat": config["lat"], "roll": 0},
            center={"lon": config["lon"], "lat": config["lat"]},
            showlakes=False,
            showcountries=True,
            countrycolor="white"
        ),
        width=900,
        height=700,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    figures[continent] = fig
    
    # Salva ogni vista continentale
    output_path = os.path.join(os.path.dirname(__file__), f"globe_3d_{continent.lower()}.html")
    fig.write_html(output_path)
    output_paths[continent] = output_path
    print(f"Vista {continent} salvata come: {output_path}")
    
    # Salva anche come immagine PNG (richiede kaleido)
    try:
        png_path = os.path.join(os.path.dirname(__file__), f"globe_3d_{continent.lower()}.png")
        fig.write_image(png_path, width=900, height=700, scale=2)
        print(f"Immagine {continent} salvata come: {png_path}")
    except Exception as e:
        print(f"Impossibile salvare PNG per {continent}: {e}")

# Vista globale originale
fig_global = go.Figure(data=go.Choropleth(
    locations=screens_avg["CountryISO"],
    z=screens_avg["AvgScreens"],
    locationmode='country names',
    colorscale=[[0, '#ffcccc'], [0.5, '#cc0000'], [1, '#660000']],
    colorbar_title="Schermi Medi",
    hovertemplate='<b>%{location}</b><br>Schermi: %{z:.0f}<extra></extra>',
))

fig_global.update_layout(
    title="Schermi Cinematografici - Vista Globale (Media 2000-2010)",
    geo=go.layout.Geo(
        showframe=False,
        showcoastlines=True,
        coastlinecolor="white",
        showland=True,
        landcolor='lightgray',
        showocean=True,
        oceancolor='lightblue',
        projection_type='orthographic',
        projection_rotation={"lon": 0, "lat": 30, "roll": 0},
        center={"lon": 0, "lat": 30},
        showlakes=False,
        showcountries=True,
        countrycolor="white"
    ),
    width=900,
    height=700,
    paper_bgcolor='white',
    plot_bgcolor='white'
)

# Salva la vista globale
output_path_global = os.path.join(os.path.dirname(__file__), "globe_3d_global.html")
fig_global.write_html(output_path_global)
print(f"Vista Globale salvata come: {output_path_global}")

# Salva anche come PNG
try:
    png_path_global = os.path.join(os.path.dirname(__file__), "globe_3d_global.png")
    fig_global.write_image(png_path_global, width=900, height=700, scale=2)
    print(f"Immagine Globale salvata come: {png_path_global}")
except Exception as e:
    print(f"Impossibile salvare PNG globale: {e}")

# Mostra la vista globale
print("\nAprendo la vista globo 3D...")
fig_global.show()

print("\nRiassunto dati per paese (Media 2000-2010):")
print("=" * 50)
for _, row in screens_avg.iterrows():
    print(f"{row['Country']}: {row['AvgScreens']:.0f} schermi")

print("\n" + "=" * 60)
print("ISTRUZIONI PER L'USO:")
print("1. Vista Globo 3D: Simula un mappamondo sferico, ruotabile con il mouse")
print("2. Intensità colore rosso = Maggior numero di schermi cinematografici")
print("3. Passa il mouse sui paesi per vedere i valori esatti")
print("4. Usa i controlli del mouse per ruotare, zoomare e esplorare il globo")
print("\nFILE GENERATI PER LA PRESENTAZIONE:")
print("- globe_3d_global.png/html: Vista mondiale completa")
print("- globe_3d_europa.png/html: Focalizzata sull'Europa")
print("- globe_3d_nord_america.png/html: Focalizzata sul Nord America")  
print("- globe_3d_sud_america.png/html: Focalizzata sul Sud America")
print("- globe_3d_asia.png/html: Focalizzata sull'Asia")
print("- globe_3d_africa.png/html: Focalizzata sull'Africa")
print("- globe_3d_oceania.png/html: Focalizzata sull'Oceania")
print("\n📊 I file PNG sono pronti per essere inseriti nella presentazione!")
print("=" * 60)
