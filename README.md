```markdown
# Coastal Tides Visualization – NOAA Tides + Coastline + Inundation Mapping

This project demonstrates an end-to-end geospatial workflow using **Python**, **GeoPandas**, **NOAA Tides & Currents API**, and optional **DEM-based inundation modeling**.  
It visualizes how **coastal water levels (tides)** change over time and how these changes affect the **shoreline** or potential **flooded areas** within a selected coastal region.

The goal is to show practical skills in:
- geospatial data processing (vector & raster),
- API integrations,
- spatial analysis,
- coastal/marine data workflows,
- producing maps (static and interactive).

---

## 🎯 Project Summary

This project retrieves **hourly water level data** from a selected NOAA tide station,  
downloads or loads coastal geodata (shoreline polygons),  
and visualizes how the coastline or inundation area changes at:

- high tide
- low tide
- intermediate levels

The system can operate in two modes:

1. **Simple mode** — visualize different water levels against a coastline polygon.  
2. **Advanced mode** — use a **DEM (Digital Elevation Model)** to compute true inundation polygons  
   (`dem <= water_level`) for more realistic flood maps.

The result can be exported as:
- static PNG / PDF maps (QGIS or Python/Matplotlib)
- interactive Folium web maps (Leaflet/GeoJSON)

---

## 🗺️ Example Use Case

**“How does the flooded area around a coastal harbor change between low tide and high tide?”**

1. Select a NOAA station (e.g., *8632200 – Sewells Point, VA*).  
2. Fetch real water-level data for a configurable date range.  
3. Pick representative time points (top 2 high tides, top 2 low tides).  
4. For each water level:
   - generate an inundation polygon (simple or DEM-based),
   - overlay on coastal map,
   - export visual results.

This creates a realistic, production-style geospatial mini-application.

---

## 📁 Project Structure

```

coastal_tides_viz/  
├── README.md  
├── requirements.txt  
├── data/  
│ ├── raw/ # original downloads (coastline, DEM, raw NOAA JSON/CSV)  
│ ├── interim/ # clipped/cleaned/intermediate files  
│ └── processed/ # final geodata used in maps  
├── maps/  
│ ├── static/ # exported PNG/PDF maps  
│ └── web/ # interactive maps (Folium HTML)  
├── notebooks/  
│ └── 01_exploration.ipynb  
└── src/  
├── config.py  
├── main.py  
├── data_io/  
│ ├── noaa_client.py  
│ ├── coastline_loader.py  
│ └── dem_loader.py  
├── processing/  
│ ├── tides.py  
│ ├── inundation.py  
│ └── geometry_utils.py  
└── viz/  
├── static_maps.py  
└── webmap.py

```

---

## 🌊 NOAA Tides & Currents API

This project uses the public NOAA CO-OPS API: water levels, predictions, metadata, and station information.

Typical endpoint used:

```

[https://api.tidesandcurrents.noaa.gov/api/prod/datagetter](https://api.tidesandcurrents.noaa.gov/api/prod/datagetter)  
?product=water_level  
&application=coastal_tides_viz  
&begin_date=YYYYMMDD  
&end_date=YYYYMMDD  
&datum=mllw  
&station=STATION_ID  
&time_zone=gmt  
&units=metric  
&format=json

```

You can freely select any NOAA water-level station along the U.S. coast.

---

## 🧩 Features

### ✔ Water Level Processing
- Fetch hourly water levels over any time range  
- Convert JSON to normalized DataFrame  
- Identify **high tide** and **low tide** events  
- Select characteristic timestamps automatically

### ✔ Coastline + AOI Handling
- Load global or regional shoreline datasets  
- Clip to an Area of Interest (AOI) defined in QGIS  
- Produce clean geometries for plotting

### ✔ Inundation Modeling
Two modes:

#### 1. Threshold mode (simple)
```

water_level >= polygon_height

````
Approximate inundation areas even without DEM.

#### 2. DEM mode (advanced)
- Load raster DEM  
- Compute mask: `dem <= water_level`  
- Convert raster mask → polygons  
- Clip to AOI  
- Visualize dynamic flooded zones

### ✔ Map Visualization
- Static maps via Matplotlib + GeoPandas  
- Interactive maps via Folium (Leaflet)  
- Multi-layer comparison (e.g., low–mid–high tide)

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/coastal_tides_viz.git
cd coastal_tides_viz
pip install -r requirements.txt
````

(Optional): If you want DEM-based inundation → install `rasterio` via wheels appropriate for your OS.

---

## ▶️ Running the Pipeline

```bash
python -m src.main
```

The script will:

1. Fetch water levels
    
2. Detect characteristic tides
    
3. (Later) compute inundation polygons
    
4. Save outputs to `data/processed/` and `maps/`
    

You will fill in processing/visualization steps as the project evolves.

---

## 📊 Data Sources

All used data sources are open:

- **NOAA Tides & Currents** – real water-level observations
    
- **GSHHG / NOAA coastline datasets** – global shoreline polygons
    
- **OpenStreetMap** – coastline and land/water polygons
    
- **SRTM / Copernicus DEM** – free elevation datasets where needed
    

---

## 🧱 Future Work (Roadmap)

- Add animated time-series map (GIF or HTML slider)
    
- Add support for multiple NOAA stations
    
- Add coordinate reference system (CRS) auto-detection
    
- Improve DEM polygonization
    
- Add web UI (FastAPI) for interactive queries
    

---

## 📣 Why This Project Matters

This project demonstrates real-world skills valuable for:

- **Geospatial Software Engineer**
    
- **GIS Developer**
    
- **Geo-ETL / spatial data engineering**
    
- **Marine geoscience / coastal analysis**
    

It shows both **software engineering** and **applied geospatial analysis** in a single reproducible workflow — exactly the type of work expected in many modern GIS & geoscience teams.

---

## 👤 Author

_Eugeny Mmamontov_  
Geospatial software developer in transition, focusing on marine/coastal data pipelines, Python GIS, and spatial analysis.

---

If you have any improvement suggestions or want to collaborate, feel free to open an issue or PR.
