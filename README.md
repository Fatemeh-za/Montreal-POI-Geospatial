# Montreal POI Geospatial Analysis

## Introduction

This project analyzes and visualizes the Points of Interest (POI) in Montreal. It covers various steps including data preparation, exploratory data analysis (EDA), geospatial visualizations, clustering, and interactive visualizations. Census data is also integrated to provide deeper insights.

## Data Loading and Preparation

- Loaded and cleaned POI and census data from CSV files.
- Handled missing values and duplicates.
- Aggregated POI data by arrondissement and merged it with census data.

## Exploratory Data Analysis (EDA)

- Conducted frequency analysis for POIs by family, category, and arrondissement.
- Visualized geospatial distribution with scatter plots.

## Geospatial Visualization

### Folium Interactive Map
An interactive map visualizing POI distributions with markers color-coded by family.  
[View Interactive Map](https://github.com/Fatemeh-za/Montreal-POI-Geospatial/blob/main/Results/montreal_establishments.html)

### Heatmap
Identified areas with high POI density.  
[View Heatmap](https://github.com/Fatemeh-za/Montreal-POI-Geospatial/blob/main/Results/POI%20Heatmap.html)

### Cluster Analysis
Applied KMeans and DBSCAN clustering techniques to categorize and visualize POI clusters.  
[View Clusters Map](https://github.com/Fatemeh-za/Montreal-POI-Geospatial/blob/main/Results/montreal_clusters.html)

### Choropleth Map
A choropleth map showing establishment counts by arrondissement.  
![Choropleth Map](https://github.com/Fatemeh-za/Montreal-POI-Geospatial/blob/main/Results/visualizations/choropleth_map.png)

## Interactive Visualizations with Plotly

- **Combined Plot**: Includes an interactive map of establishments and a bar chart of classification counts.
- **Kernel Density Estimation**: Visualizes the density of POIs in Montreal.  
[View Combined Plot](https://github.com/Fatemeh-za/Montreal-POI-Geospatial/blob/main/Results/interactive_visualizations.html)

## Key Insights

- **Geospatial Clustering**: Revealed clusters of establishments, highlighting areas with specific POI densities.
- **Census Data Integration**: Correlations between census data and POI distributions were uncovered.
- **POI Distribution**: Patterns of recreational and cultural establishments were observed across different arrondissements.

## Conclusion

This analysis delivers insights into Montreal’s POI landscape, integrating census data for a comprehensive view. It supports urban planning, tourism, and community development by providing actionable geospatial insights.

## Repository Structure

