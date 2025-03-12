import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio


# Load POI data
poi = pd.read_csv('/MTL/POI.csv')

# Fill missing values in 'Nom court' column
poi['Nom court'].fillna("N/A", inplace=True)

# Convert Longitude and Latitude to numeric
poi['Longitude'] = pd.to_numeric(poi['Longitude'], errors='coerce')
poi['Latitude'] = pd.to_numeric(poi['Latitude'], errors='coerce')

# Drop 'Nom court' column due to too many missing values
poi_cleaned = poi.drop(columns=["Nom court"])

# Fill missing value in 'Bureau' column
poi_cleaned["Bureau"].fillna(poi_cleaned["Bureau"].mode()[0], inplace=True)

# Remove duplicate rows
poi_cleaned = poi_cleaned.drop_duplicates()

# Save cleaned data to a new CSV file
poi_cleaned.to_csv('/MTL/POI_cleaned.csv', index=False)

print("Data cleaning completed.")


# Load the census data with appropriate encoding
census_data = pd.read_csv("MTL/98-401-X2021020_English_CSV_data.csv", encoding='latin1')

# Display basic information
print("Raw Census Data:")
print(census_data.head())
