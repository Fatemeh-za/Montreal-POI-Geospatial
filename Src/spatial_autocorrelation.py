
# Import necessary libraries
import matplotlib.pyplot as plt

def compute_morans_i(poi, gdf):
    """
    Compute Moran's I spatial autocorrelation for establishment counts in Montreal boroughs.

    Parameters:
    - poi (DataFrame): The POI data as a pandas DataFrame.
    - gdf (GeoDataFrame): The Montreal borough shapefile as a GeoDataFrame.

    Outputs:
    - Moran's I value
    - p-value for Moran's I
    - Choropleth map showing establishment counts by borough.
    """
    # Ensure the GeoDataFrame uses the correct coordinate reference system (CRS)
    gdf = gdf.to_crs(epsg=3857)

    # Aggregate POI data by arrondissement (borough)
    aggregated_data = poi.groupby('Arrondissement').agg({'ID': 'count'}).rename(columns={'ID': 'Establishment_Count'}).reset_index()

    # Merge the aggregated data with the GeoDataFrame
    merged_gdf = gdf.merge(aggregated_data, left_on="NOM", right_on="Arrondissement", how="left")

    # Fill missing establishment counts with 0
    merged_gdf["Establishment_Count"] = merged_gdf["Establishment_Count"].fillna(0)

    # Create spatial weights using Queen contiguity (shared polygon boundaries)

    w = ps.weights.Queen.from_dataframe(merged_gdf, use_index=True)

    # Compute Moran's I for establishment counts
    moran = esda.moran.Moran(merged_gdf["Establishment_Count"], w)

    # Print Moran's I value and p-value
    print(f"Moran's I: {moran.I}")
    print(f"p-value: {moran.p_sim}")

    # Visualize the choropleth map for context
    fig, ax = plt.subplots(figsize=(12, 10))
    merged_gdf.plot(column='Establishment_Count', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    ax.set_title("Establishment Count by Borough", fontsize=16)
    ax.set_axis_off()
    # Save the choropleth map to a file
    fig.savefig("establishment_count_choropleth.png", dpi=300)
    print("Choropleth map saved as 'establishment_count_choropleth.png'")
    plt.show()

compute_morans_i(poi, gdf)
