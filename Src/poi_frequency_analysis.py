import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create a numeric version of the 'Classification' column
poi['Classification_Numeric'] = poi['Classification'].str.extract('(\d+)').astype(float)

# Exploratory Data Analysis (EDA)

# Calculate frequency counts and proportions
famille_counts = poi['Famille'].value_counts()
categorie_counts = poi['Catégorie'].value_counts()
classification_counts = poi['Classification'].value_counts()

print("----- 'Famille' Frequency -----\n", famille_counts)
print("\n----- 'Catégorie' Frequency -----\n", categorie_counts)
print("\n----- 'Classification' Frequency -----\n", classification_counts)

# Create a 2x2 subplot grid for advanced visualization
fig, axs = plt.subplots(2, 2, figsize=(14, 12))

# (a) Count plot for Famille
sns.countplot(x="Famille", data=poi, ax=axs[0, 0], palette="Set2")
axs[0, 0].set_title("Distribution of Establishments by Famille")
axs[0, 0].set_xlabel("Famille")
axs[0, 0].set_ylabel("Count")
axs[0, 0].tick_params(axis='x', rotation=45)

# (b) Count plot for Classification
sns.countplot(x="Classification", data=poi, ax=axs[0, 1], palette="Set3")
axs[0, 1].set_title("Distribution of Classification Levels")
axs[0, 1].set_xlabel("Classification")
axs[0, 1].set_ylabel("Count")
axs[0, 1].tick_params(axis='x', rotation=45)

# (c) Boxplot: Distribution of Numeric Classification by Famille
sns.boxplot(x="Famille", y="Classification_Numeric", data=poi, ax=axs[1, 0], palette="Pastel1")
axs[1, 0].set_title("Numeric Classification by Famille")
axs[1, 0].set_xlabel("Famille")
axs[1, 0].set_ylabel("Numeric Classification")

# (d) Heatmap/Cross-tab: Famille vs. Classification Frequency
crosstab = pd.crosstab(poi['Famille'], poi['Classification'])
sns.heatmap(crosstab, annot=True, fmt="d", cmap="YlGnBu", ax=axs[1, 1])
axs[1, 1].set_title("Cross-tabulation: Famille vs. Classification")

plt.tight_layout()
plt.show()

# Print summary statistics (mean, median, min, max) for Classification_Numeric by Famille
classification_stats = poi.groupby('Famille')['Classification_Numeric'].agg(['mean', 'median', 'min', 'max'])
print("\n----- Statistical Summary of Numeric Classification by Famille -----")
print(classification_stats)
