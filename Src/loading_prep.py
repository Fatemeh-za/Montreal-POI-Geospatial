import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

# Load the POI data
poi = pd.read_csv('/POI.csv')

# Load the census data with appropriate encoding
census_data = pd.read_csv("MTL/98-401-X2021020_English_CSV_data.csv", encoding='latin1')

# Display basic information
print("Raw Census Data:")
print(census_data.head())
