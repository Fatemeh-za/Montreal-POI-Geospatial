from sklearn.cluster import KMeans

# Apply KMeans clustering
coords = poi[["Latitude", "Longitude"]].dropna()
kmeans = KMeans(n_clusters=4, random_state=42)
poi["Cluster"] = kmeans.fit_predict(coords)

# Plot clusters
sns.scatterplot(data=poi, x="Longitude", y="Latitude", hue="Cluster", palette="viridis", alpha=0.7)
plt.title("KMeans Clustering of POIs")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Save interactive cluster map
cluster_map = folium.Map(location=[45.5017, -73.5673], zoom_start=12)
for idx, row in poi.dropna(subset=["Cluster"]).iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=4,
        color="red" if row["Cluster"] == 0 else "blue" if row["Cluster"] == 1 else "green" if row["Cluster"] == 2 else "purple",
        fill=True,
        popup=f"Cluster: {int(row['Cluster'])}; {row['Famille']}"
    ).add_to(cluster_map)
cluster_map.save("montreal_clusters.html")
