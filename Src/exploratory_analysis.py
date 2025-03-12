import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Summary statistics
print(poi["Famille"].value_counts())
print(poi["Catégorie"].value_counts())
print(poi["Arrondissement"].value_counts())

# Geospatial Distribution
plt.figure(figsize=(10, 6))
sns.scatterplot(data=poi, x="Longitude", y="Latitude", hue="Famille", alpha=0.6)
plt.title("Geospatial Distribution of POIs in Montreal")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.show()
