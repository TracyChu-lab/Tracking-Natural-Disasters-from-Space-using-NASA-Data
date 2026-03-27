# Tracking-Natural-Disasters-from-Space-using-NASA-Data
This project finds that wildfire activity follows clear spatial and seasonal patterns. By combining EONET event data with FIRMS satellite detections, the analysis shows strong consistency between the two sources, including a clear dominance of daytime detections and peak wildfire activity in late summer and early fall. 

# 📌 Project Overview

This project explores global and U.S. wildfire patterns using satellite-based and event-level data from NASA. By combining the EONET API (event metadata) and FIRMS wildfire detections (satellite observations), the analysis investigates where wildfires occur, how frequently they happen, how intense they are, and how they vary over time.

The project aims to identify spatial, temporal, and environmental patterns in wildfire activity, with a particular focus on seasonality and the role of temperature.


# 📊 Key Research Questions

•	Where are wildfires most concentrated globally?

•	How does wildfire activity vary across continents and U.S. states?

•	Do wildfires occur more during the day or at night?

•	What are the seasonal patterns of wildfire frequency and intensity?

•	How are wildfire activity and temperature related?

•	How do EONET (event-level) and FIRMS (satellite-level) data compare?


# 🗂️ Repository Structure

`├── code.ipynb        # Main notebook (data collection, cleaning, analysis, visualization)`

`├── quiz.py           # Streamlit interactive quiz application`

`├── essay.md          # Written report explaining findings`

`└── README.md         # Project overview and instructions`



# ⚙️ Data Sources

NASA EONET

• API-based dataset of natural hazard events

• Provides event-level data (type, location, time, magnitude)

• Used for: 

    • Global wildfire distribution

    • Event frequency analysis

    • Magnitude (burned area) analysis

NASA FIRMS (VIIRS)

• Satellite-based fire detection data

• Provides:

    • Fire locations (latitude/longitude)
    
    • Day/night detection
    
    • Fire Radiative Power (FRP, intensity)
    
• Used for:

    • Fire intensity analysis

    • Seasonal patterns

    • Validation of EONET results

Temperature Data (Open-Meteo)

• Historical daily temperature data aggregated to monthly averages

• Used to explain seasonal wildfire patterns


# 🔍 Methods

•	API data extraction and JSON parsing (EONET)

•	Data cleaning and transformation into structured DataFrames

•	Feature engineering (month, season, hemisphere, state classification)

•	Spatial analysis using latitude/longitude and maps (Folium)

•	Aggregation and grouping (monthly, state-level, continent-level)

•	Visualization using Seaborn and Matplotlib

•	Correlation analysis (temperature vs wildfire frequency & intensity)


# 📈 Key Findings

•	Wildfires are spatially clustered, especially in North America, Africa, and parts of South America and Oceania.

•	Within the U.S., wildfire magnitude and intensity are highly uneven, with western states experiencing larger and stronger fires.

•	Wildfires occur more frequently during the daytime, as shown in both EONET and FIRMS data.

•	Wildfire activity is strongly seasonal, peaking in late summer and early fall.

•	There is a strong positive correlation between temperature and wildfire activity, indicating that climate plays a key role in both fire occurrence and intensity.

•	EONET and FIRMS show consistent temporal patterns, despite differences in data structure and resolution.


# 🚀 How to Run the Project

Run the analysis notebook

Open code.ipynb in Jupyter or Google Colab and run all cells.

Run the Streamlit quiz app

Install dependencies:

`pip install streamlit`

Run the app:

`streamlit run quiz.py`

The app will open in your browser and allow users to interact with the project through a quiz.


# 📚 References

•	NASA EONET API: https://eonet.gsfc.nasa.gov/

•	NASA FIRMS: https://firms.modaps.eosdis.nasa.gov/

•	Open-Meteo API: https://open-meteo.com/


# 👤 Author

This project was developed by Tracy Chu and Lylian Li, as part of an exploratory data analysis assignment, combining data science techniques with environmental analysis to better understand natural hazard patterns.
