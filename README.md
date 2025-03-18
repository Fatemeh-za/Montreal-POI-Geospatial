# Montreal POI Geospatial Analysis

## Project Overview

This project focuses on analyzing and visualizing Points of Interest (POI) in Montreal using geospatial, statistical, and exploratory data analysis techniques. The analysis includes data preparation, geospatial visualizations, clustering, interactive maps, and integration of census data for deeper insights. Key outputs include heatmaps, choropleth maps, clustering visualizations, and spatial autocorrelation metrics.

---

## Data Description

### POI Dataset
- **File**: `POI.csv`
- **Description**: Contains detailed information on Points of Interest in Montreal, such as names, categories, locations, and boroughs.
- **Columns and Data Types**:
  - `ID` *(int)*: Unique identifier for each POI.
  - `Famille` *(str)*: Family of POIs (e.g., Cultural, Commercial).
  - `Catégorie` *(str)*: Specific POI category.
  - `Nom français` *(str)*: Name of the POI in French.
  - `Longitude`, `Latitude` *(float)*: Geographic coordinates of the POI.
  - `Arrondissement` *(str)*: Borough of the POI.
  - `Classification` *(str)*: Classification level (numeric).
  - 
### Geospatial Data
- **File**: `limites-administratives-agglomeration-nad83.shp`
- **Description**: Shapefile representing the administrative boundaries of Montreal’s boroughs.

### Census Data
- **File**: `98-401-X2021020_English_CSV_data.csv`
- **Description**: Census data providing demographic and socioeconomic statistics for Montreal boroughs.
- **Columns and Data Types**:
  - `GEO_NAME` *(str)*: Geographic name of the borough.
  - `CHARACTERISTIC_NAME` *(str)*: Census characteristic (e.g., population).
  - `TNR_SF` *(float)*: Statistical measure of the characteristic.


---

## Methods and Techniques

### Data Cleaning and Preprocessing
- Dropped irrelevant columns with excessive missing values.
- Handled missing values by imputing with appropriate replacements.
- Removed duplicate entries to ensure data quality.

### Exploratory Data Analysis (EDA)
- Analyzed frequency counts of POIs by family, category, and borough.
- Visualized distributions using scatter plots and count plots.

### Geospatial Analysis
- Generated static and interactive maps:
  - Interactive Folium map showing POIs by category.
  - Heatmap identifying areas with high POI densities.
  - Choropleth map displaying the establishment count by boroughs.

### Clustering
- Applied **KMeans** clustering to group POIs based on geographic coordinates.
- Created an interactive cluster map with markers color-coded for each cluster.

### Spatial Autocorrelation
Spatial autocorrelation measures whether the distribution of POI counts across geographic areas is random, clustered, or dispersed.

- **Moran's I**: A statistical metric used to determine spatial autocorrelation. It ranges between -1 and 1:
  - Positive values near 1 indicate clustering (similar values are close together).
  - Negative values near -1 indicate dispersion (dissimilar values are close together).
  - Values near 0 suggest a random distribution.
- **libpysal**: A Python library used to calculate spatial weights, which define relationships between areas based on shared boundaries or distances.
- **esda**: A Python library specifically for Exploratory Spatial Data Analysis, including Moran's I and other spatial metrics.

---

## Results

## Results

### Key Insights
- **Geospatial Clustering**: High-density clusters of recreational and cultural POIs were found in specific boroughs, highlighting the central hubs of these activities.
- **Spatial Patterns**:
  - Moran's I value: **0.0428**
  - p-value: **0.116**
  - These results suggest **weak spatial clustering** in the distribution of establishment counts across Montreal's boroughs. The p-value indicates that the spatial pattern observed is not statistically significant at a 95% confidence level.
- **Kernel Density Estimation**: Density maps revealed key areas with high concentrations of POIs, especially around downtown and more populous boroughs.
- **Demographic Correlations**: Merging POI data with census statistics unveiled correlations between borough characteristics (e.g., population, income levels) and the presence of certain types of establishments.




