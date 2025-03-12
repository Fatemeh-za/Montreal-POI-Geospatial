# Montreal POI Geospatial Analysis

## Introduction

This project aims to analyze and visualize the Points of Interest (POI) in Montreal. The analysis includes data loading, cleaning, exploratory data analysis (EDA), geospatial visualizations, clustering, and interactive visualizations. Additionally, we integrate and analyze census data to provide further insights.

## Data Loading and Preparation

We loaded the POI and census data from CSV files, cleaned them, and handled missing values and duplicates. We aggregated POI data by arrondissement and merged it with the cleaned census data.

## Exploratory Data Analysis (EDA)

We conducted exploratory data analysis to understand the distribution of POIs:
- **Count of POIs by Family, Category, and Arrondissement**
- **Geospatial Distribution:** A scatterplot showed the distribution of POIs across Montreal by their families.

## Geospatial Visualization

### Folium Interactive Map

We created an interactive map using Folium to visualize the distribution of POIs:
- Markers were added for each POI, with different colors representing different families.
- [Interactive Map](results/montreal_establishments.html)

### Heatmap

We created a heatmap to identify areas with high POI concentration:
- [Heatmap](results/poi_heatmap.html)

### Cluster Analysis

We applied KMeans and DBSCAN clustering to categorize the POIs and visualized the clusters:
- **KMeans Clustering Map:** [Clusters Map](results/montreal_clusters.html)

### Choropleth Map

We created a choropleth map to show the establishment count by arrondissement:
- [Choropleth Map](results/visualizations/choropleth_map.png)

## Interactive Visualizations with Plotly

We created interactive visualizations using Plotly:
- **Combined Plot:** An interactive map of establishments and a bar chart of classification counts.
- **Kernel Density Estimation:** Visualizes the density of establishments.
- [Interactive Combined Plot](results/interactive_visualizations.html)

## Key Insights

- **Geospatial Clustering:** The clustering analysis revealed distinct clusters of POIs, indicating areas with a high concentration of certain types of establishments.
- **POI Distribution:** The scatterplot and interactive map showed that recreational and cultural POIs are densely clustered in specific areas of Montreal.
- **Census Data Integration:** The analysis of census data uncovered new trends and correlations that complement the POI data.

## Conclusion

This project provides a comprehensive analysis and visualization of POIs in Montreal, along with insights from the census data. The techniques used include data cleaning, EDA, geospatial analysis with Folium, clustering with KMeans and DBSCAN, and interactive visualizations with Plotly. The insights derived can be useful for urban planning, tourism, and community development.

## Repository Structure

- **data/**: Directory containing the raw data files (POI.csv and census data CSV).
- **notebooks/**: Jupyter Notebooks for different stages of the analysis.
- **scripts/**: Python scripts for data cleaning, EDA, geospatial analysis, clustering, and visualizations.
- **results/**: Directory containing the results, including HTML maps and visualizations.
- **README.md**: This file.
- **requirements.txt**: List of required Python packages.

## Requirements

To install the required Python packages, use:

```sh
pip install -r requirements.txt
