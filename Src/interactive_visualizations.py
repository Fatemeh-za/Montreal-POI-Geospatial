import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio


# Set default renderer to "browser"
pio.renderers.default = "browser"

# Create a combined subplot
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
