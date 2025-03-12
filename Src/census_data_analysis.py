import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

# Display the first few rows to identify relevant columns
print("Raw Census Data:")
print(census_data.head())

# Identify relevant columns
required_columns = ['GEO_NAME', 'CHARACTERISTIC_NAME', 'TNR_SF']

# Filter the data to include only relevant columns
filtered_census_data = census_data[required_columns]

# Handle duplicate entries by aggregating (e.g., taking the mean of duplicates)
aggregated_census_data = filtered_census_data.groupby(['GEO_NAME', 'CHARACTERISTIC_NAME']).agg({'TNR_SF': 'mean'}).reset_index()

# Perform the pivot operation
census_pivot = aggregated_census_data.pivot(index='GEO_NAME', columns='CHARACTERISTIC_NAME', values='TNR_SF').reset_index()

# Rename columns to match the expected format
if 'GEO_NAME' in census_pivot.columns:
    census_pivot.rename(columns={"GEO_NAME": "Arrondissement"}, inplace=True)

# Display cleaned and pivoted data
print("\nCleaned and Pivoted Census Data:")
print(census_pivot.head())

# Load cleaned POI data
poi = pd.read_csv('/Users/FATEMEH/Desktop/POI_cleaned.csv')

# Now, aggregate your POI data by arrondissement
aggregated_data = poi.groupby('Arrondissement').agg({'ID': 'count'}).rename(
    columns={'ID': 'Establishment_Count'}
).reset_index()

print("\nAggregated POI Data:")
print(aggregated_data.head())

# Merge the aggregated POI data with the cleaned census data
merged_data = aggregated_data.merge(census_pivot, on="Arrondissement", how="left")

print("\nMerged Data (POI with Census Data):")
print(merged_data.head())

# Visualization Part
pio.renderers.default = "browser"

# Create a combined subplot with two columns
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Establishment Map", "Classification Counts"),
    specs=[[{"type": "scattermapbox"}, {"type": "xy"}]]
)

# Create Mapbox Scatter Traces
map_fig = px.scatter_mapbox(
    poi,
    lat="Latitude",
    lon="Longitude",
    color="Famille",
    hover_name="Nom français",
    hover_data=["Classification"],
    zoom=10,
    height=600
)
for trace in map_fig.data:
    fig.add_trace(trace, row=1, col=1)

# Create a Bar Chart for Classification Counts
classif_counts = poi['Classification'].value_counts().reset_index()
classif_counts.columns = ['Classification', 'Count']

bar_trace = go.Bar(
    x=classif_counts['Classification'],
    y=classif_counts['Count'],
    marker_color='lightsalmon',
    text=classif_counts['Count'],
    textposition='auto'
)
fig.add_trace(bar_trace, row=1, col=2)

# Update Layout Settings
fig.update_layout(
    mapbox=dict(
        style="open-street-map",
        center={"lat": poi["Latitude"].mean(), "lon": poi["Longitude"].mean()},
        zoom=10,
    ),
    margin={"r": 0, "t": 50, "l": 0, "b": 0},
    height=600,
    title_text="Combined Plot: Establishment Map & Classification Counts",
    showlegend=False
)

# Display the combined figure
fig.show()
