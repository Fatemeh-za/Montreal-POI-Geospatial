# Create a base map centered on Montreal
map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12)

# Add markers
for idx, row in poi.iterrows():
    if pd.notnull(row["Latitude"]) and pd.notnull(row["Longitude"]):
        popup_text = f"{row['Nom français']}<br>Classification: {row['Classification']}"
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=5,
            color="blue" if row["Famille"] == "Culturel" else "green",
            fill=True,
            popup=popup_text
        ).add_to(map_montreal)

# Save the interactive map
map_montreal.save("montreal_establishments.html")
