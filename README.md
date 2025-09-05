# Visualizzazione Scientifica - L'Impatto dello Streaming sul Cinema

# Visualizzazione Scientifica - L'Impatto dello Streaming sul Cinema

## Descrizione del Progetto

Questo progetto analizza l'impatto delle piattaforme di streaming sull'industria cinematografica attraverso una serie di visualizzazioni scientifiche basate su dati reali dal 2000 al 2024. La presentazione segue un percorso logico che va dal contesto pre-streaming fino alle dinamiche attuali dell'industria.

## Indice della Presentazione

1. **Introduzione**
2. **Contesto pre-streaming (2000–2010)**
3. **L'avvento dello streaming (2010–oggi)**
4. **Impatto sul botteghino**
5. **Offerta e contenuti: cosa guardiamo?**
6. **Finestre di sfruttamento: dal cinema allo streaming**
7. **Budget e rischio**
8. **Conclusione**

## Struttura del Progetto

```
visualizzazione_scientifica/
├── README.md
├── requirement.txt
└── Presentazione/
    ├── capitolo 1/          # Contesto pre-streaming (2000-2010)
    │   ├── G1/             # Box Office Mondiale (2000-2010)
    │   ├── G2/             # Rilasci Cinematografici
    │   └── G3/             # Cinema UNESCO Mondiale
    ├── capitolo 2/          # L'avvento dello streaming (2010-oggi)
    │   ├── G4/             # Crescita Abbonati Netflix
    │   ├── G5/             # Penetrazione SVOD Globale
    │   ├── G6/             # TV vs Streaming (minuti)
    │   ├── G7/             # Andamento Streaming vs Box Office
    │   ├── G8/             # Declino Ammissioni Cinema Europa
    │   ├── G9/             # Confronto Spesa Cinema vs Streaming
    │   ├── G10/            # Andamento Spesa Streaming USA
    │   └── G11/            # Crescita Utenti Streaming USA
    ├── capitolo 3/          # Impatto sul botteghino
    │   ├── G8/             # Declino Ammissioni Cinema Europa
    │   ├── G9/             # Confronto Spesa Cinema vs Streaming
    │   └── G10/            # Andamento Spesa Streaming USA
    ├── capitolo 4/          # Offerta e contenuti: cosa guardiamo?
    │   ├── G12/            # Top 10 Serie Netflix
    │   ├── G13/            # Confronto Serie vs Film (Ore)
    │   ├── G14/            # Valutazioni IMDb nel Tempo
    │   └── G15/            # Finestre di sfruttamento
    └── capitolo 5/          # Budget e rischio
        ├── G16/            # Budget vs Box Office
        └── G17/            # Impatto Pandemia sul Box Office
```

## Analisi per Capitoli

### Capitolo 1: Contesto pre-streaming (2000–2010)
Stabilisce il panorama cinematografico prima dell'arrivo massiccio dello streaming:
- **G1**: Crescita costante del box office mondiale (2000-2010)
- **G2**: Numero di rilasci cinematografici per anno
- **G3**: Dati UNESCO su cinema e frequentazione globale

**Insight chiave**: Il cinema tradizionale mostrava una crescita stabile e prevedibile.

### Capitolo 2: L'avvento dello streaming (2010–oggi)
Documenta la rivoluzione digitale e i suoi effetti immediati:
- **G4**: Esplosione degli abbonati Netflix (2007-2020)
- **G5**: Penetrazione globale dei servizi SVOD
- **G6**: Spostamento da TV tradizionale a streaming
- **G7**: Correlazione inversa streaming-cinema
- **G11**: Crescita utenti streaming USA

**Insight chiave**: Lo streaming ha trasformato radicalmente le abitudini di consumo.

### Capitolo 3: Impatto sul botteghino  
Analizza l'effetto diretto dello streaming sui ricavi cinematografici:
- **G8**: Declino delle ammissioni cinematografiche in Europa
- **G9**: Confronto spesa cinema vs streaming
- **G10**: Andamento spesa streaming USA

**Insight chiave**: Trasferimento di valore dal cinema tradizionale alle piattaforme digitali.

### Capitolo 4: Offerta e contenuti - cosa guardiamo?
Analizza le preferenze del pubblico nell'era streaming:
- **G12**: Le serie TV più popolari su Netflix
- **G13**: Predominanza delle serie TV sui film (grafico a torta)
- **G14**: Evoluzione della qualità percepita (valutazioni IMDb)
- **G15**: Accelerazione delle finestre di distribuzione

**Insight chiave**: Le serie TV dominano l'engagement, le finestre si accorciano drasticamente.

### Capitolo 5: Budget e rischio
Esamina gli aspetti economici e finanziari:
- **G16**: Relazione budget-incassi nell'era streaming
- **G17**: Impatto della pandemia e vulnerabilità del settore

**Insight chiave**: Maggiore incertezza e nuovi modelli di rischio/rendimento.

## Caratteristiche Tecniche

### Stile Unificato
Tutti i grafici seguono uno stile visivo coerente:
- **Dimensioni**: 9x6 pollici (figsize=(9,6))
- **Colore principale**: Rosso (#cc0000) 
- **Trasparenza**: Alpha 0.7 per riempimenti
- **Font**: 12pt per etichette, 10pt per legenda
- **Layout**: Proporzioni standardizzate

### Tipologie di Grafici
- **Grafici a linee**: Trend temporali e evoluzione
- **Grafici a barre**: Confronti e distribuzioni  
- **Scatter plot**: Correlazioni budget-incassi
- **Grafici a torta**: Distribuzione serie vs film
- **Aree ombreggiate**: Evidenziazione periodi critici (pandemia)

## Dipendenze

Le librerie Python necessarie sono elencate in `requirement.txt`:

```
pandas
matplotlib
numpy
os (built-in)
```

## Installazione e Utilizzo

1. **Clona o scarica il progetto**
2. **Installa le dipendenze**:
   ```bash
   pip install -r requirement.txt
   ```
3. **Esegui i grafici**:
   ```bash
   # Esempio per il primo grafico
   cd "Presentazione/capitolo 1/G1"
   python G1.py
   ```

## Dataset

I dati utilizzati includono:
- Incassi del box office mondiale (Box Office Mojo)
- Statistiche Netflix ufficiali
- Dati UNESCO su cinema e cultura
- Valutazioni IMDb
- Statistiche di mercato streaming
- Dati economici dell'industria cinematografica

## Risultati Principali

### Tesi Centrale
La presentazione dimostra come lo streaming abbia **trasformato irreversibilmente** l'industria cinematografica, creando un nuovo ecosistema che privilegia:
- **Contenuti seriali** rispetto ai film tradizionali
- **Distribuzione immediata** rispetto alle finestre tradizionali  
- **Consumo domestico** rispetto all'esperienza cinematografica

### Evidenze per Capitolo

#### Contesto pre-streaming (2000-2010)
- Crescita lineare e prevedibile del box office
- Modello di business stabile basato su finestre di distribuzione lunghe
- Cinema come esperienza sociale dominante

#### L'avvento dello streaming (2010-oggi)  
- Crescita esponenziale degli abbonati (da milioni a miliardi)
- Cambiamento radicale delle abitudini di consumo
- Nascita di nuovi modelli di business

#### Impatto sul botteghino
- **Declino misurabile** delle ammissioni cinematografiche in Europa
- **Trasferimento di spesa** da cinema a streaming
- **Crescita spesa streaming** negli USA (miliardi di dollari annui)

#### Cosa guardiamo oggi
- **70%+ ore visualizzate** dedicate a serie TV vs film su Netflix
- Mantenimento qualità contenuti (valutazioni IMDb stabili)
- Preferenza per contenuti "binge-watchable"

#### Nuove dinamiche economiche
- Finestre cinema-streaming: **180 giorni → 35 giorni** (riduzione 80%)
- Maggiore volatilità nella relazione budget-incassi
- Vulnerabilità dimostrata durante la pandemia

### Impatti Trasformativi Identificati

1. **Democratizzazione dell'accesso**: Contenuti globali disponibili istantaneamente
2. **Personalizzazione**: Algoritmi vs programmazione tradizionale
3. **Produzione accelerata**: Necessità di contenuti continui
4. **Rischio distribuito**: Dai blockbuster ai cataloghi diversificati
5. **Geopolitica dei contenuti**: Competizione globale per l'attenzione

## Metodologia

- **Analisi temporale**: Focus sui cambiamenti dal 2000 al 2024
- **Comparazione**: Confronti diretti tra diversi periodi e metriche
- **Visualizzazione scientifica**: Grafici ottimizzati per chiarezza e precisione
- **Standardizzazione**: Stile unificato per facilità di lettura

## Conclusioni

### Trasformazione Paradigmatica
Il progetto documenta una **rivoluzione strutturale** nell'intrattenimento che va oltre un semplice cambiamento tecnologico. Lo streaming ha ridefinito:

- **QUANDO** consumiamo contenuti (on-demand vs orari fissi)
- **DOVE** li consumiamo (casa vs sala cinematografica) 
- **COSA** preferiamo (serie vs film)
- **COME** vengono prodotti e distribuiti (algoritmi vs intuizione)

### Implicazioni Future
1. **Cinema tradizionale**: Verso un modello "premium experience" per grandi produzioni
2. **Streaming**: Consolidamento in poche piattaforme globali dominanti
3. **Contenuti**: Maggiore diversificazione e personalizzazione
4. **Modelli economici**: Abbonamenti vs acquisti singoli
5. **Produzione**: Investimenti massicci in contenuti originali

### Metodologia Scientifica
Questo studio dimostra l'efficacia della **visualizzazione dati** per:
- Rendere evidenti trend complessi attraverso grafici chiari
- Supportare argomentazioni con evidenza quantitativa  
- Comunicare trasformazioni industriali a diversi pubblici
- Predire direzioni future basate su dati storici

La standardizzazione visiva permette confronti immediati tra diversi aspetti della trasformazione, creando una narrativa coerente e convincente.

## Autore

Progetto di Visualizzazione Scientifica - Sessione Settembre 2025

## Licenza

Progetto accademico per scopi educativi e di ricerca.