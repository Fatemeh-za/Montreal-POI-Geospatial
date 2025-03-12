# Identify relevant columns in census data
required_columns = ['GEO_NAME', 'CHARACTERISTIC_NAME', 'TNR_SF']

# Filter the data to include only relevant columns
filtered_census_data = census_data[required_columns]

# Handle duplicate entries by aggregating
aggregated_census_data = filtered_census_data.groupby(['GEO_NAME', 'CHARACTERISTIC_NAME']).agg({'TNR_SF': 'mean'}).reset_index()

# Perform the pivot operation
census_pivot = aggregated_census_data.pivot(index='GEO_NAME', columns='CHARACTERISTIC_NAME', values='TNR_SF').reset_index()

# Rename columns to match the expected format
if 'GEO_NAME' in census_pivot.columns:
    census_pivot.rename(columns={"GEO_NAME": "Arrondissement"}, inplace=True)

# Display cleaned and pivoted data
print("\nCleaned and Pivoted Census Data:")
print(census_pivot.head())

# Aggregating POI data by arrondissement
aggregated_data = poi.groupby('Arrondissement').agg({'ID': 'count'}).rename(
    columns={'ID': 'Establishment_Count'}
).reset_index()

print("\nAggregated POI Data:")
print(aggregated_data.head())

# Merge the aggregated POI data with the cleaned census data
merged_data = aggregated_data.merge(census_pivot, on="Arrondissement", how="left")

print("\nMerged Data (POI with Census Data):")
print(merged_data.head())
