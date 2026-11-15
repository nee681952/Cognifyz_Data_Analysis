
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("dataset.csv")

# Display dataset information
print("Dataset Shape:", df.shape)

# TASK 1: RESTAURANT RATINGS

# Step 1: Select the Aggregate rating column
ratings = df["Aggregate rating"]

# Step 2: Count each exact rating
rating_counts = ratings.value_counts().sort_index()

print("\nEXACT RATING DISTRIBUTION")
print(rating_counts)

# Step 3: Calculate rating ranges
# Zero ratings are kept as a separate unrated category.
rating_ranges = {
    "0.0 (Unrated)": ((ratings == 0).sum()),
    ">0–2.0": ((ratings > 0) & (ratings <= 2)).sum(),
    ">2.0–3.0": ((ratings > 2) & (ratings <= 3)).sum(),
    ">3.0–4.0": ((ratings > 3) & (ratings <= 4)).sum(),
    ">4.0–5.0": ((ratings > 4) & (ratings <= 5)).sum()
}

print("\nRATING RANGE DISTRIBUTION")

for rating_range, count in rating_ranges.items():
    print(rating_range, ":", count)

# Step 4: Find the average number of votes
average_votes = df["Votes"].mean()

print("\nAVERAGE NUMBER OF VOTES")
print(round(average_votes, 2))


# Create a bar chart for rating ranges

plt.figure(figsize=(9, 5))

plt.bar(
    list(rating_ranges.keys()),
    list(rating_ranges.values())
)

plt.title("Restaurant Rating Distribution")
plt.xlabel("Rating Range")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=15)

# Add values above bars
for i, count in enumerate(rating_ranges.values()):
    plt.text(i, count + 30, str(count), ha="center")

plt.tight_layout()

# Save the chart
import os
os.makedirs("outputs", exist_ok=True)

plt.savefig("outputs/task1_restaurant_ratings.png")

plt.show()


# TASK 2: CUISINE COMBINATION ANALYSIS

# Step 1: Select required columns
cuisine_df = df[["Cuisines", "Aggregate rating"]].dropna().copy()

# Step 2: Clean and standardize cuisine combinations
# Sorting ensures the same combination is counted together.
def clean_cuisines(value):
    cuisines = [c.strip() for c in value.split(",") if c.strip()]
    return ", ".join(sorted(cuisines))

cuisine_df["Cuisine Combination"] = (
    cuisine_df["Cuisines"].astype(str).apply(clean_cuisines)
)

# Step 3: Keep combinations containing at least two cuisines
cuisine_df["Cuisine Count"] = (
    cuisine_df["Cuisine Combination"].str.count(",") + 1
)

multi_cuisine = cuisine_df[
    cuisine_df["Cuisine Count"] >= 2
].copy()

# Step 4: Find the most common combinations
combination_counts = (
    multi_cuisine["Cuisine Combination"].value_counts()
)

print("\nTOP 10 MOST COMMON CUISINE COMBINATIONS")
print(combination_counts.head(10))

# Step 5: Calculate average ratings
# Rating 0 means unrated, so exclude it from rating averages.
rated_cuisines = multi_cuisine[
    multi_cuisine["Aggregate rating"] > 0
]

combination_ratings = (
    rated_cuisines.groupby("Cuisine Combination")
    .agg(
        Restaurant_Count=("Aggregate rating", "count"),
        Average_Rating=("Aggregate rating", "mean")
    )
)

# Step 6: Show average ratings for common combinations
top_combinations = combination_ratings.loc[
    combination_counts.head(10).index
].sort_values(
    by="Average_Rating",
    ascending=False
)

print("\nAVERAGE RATINGS OF TOP 10 COMBINATIONS")
print(top_combinations.round(2))

# Step 7: Find higher-rated combinations
# Require at least 10 rated restaurants for comparison.
reliable_combinations = combination_ratings[
    combination_ratings["Restaurant_Count"] >= 10
]

print("\nTOP 10 HIGHER-RATED COMBINATIONS")
print(
    reliable_combinations
    .sort_values("Average_Rating", ascending=False)
    .head(10)
    .round(2)
)


# Create average rating chart

import os

os.makedirs("outputs", exist_ok=True)

chart_data = top_combinations.sort_values(
    "Average_Rating",
    ascending=True
)

plt.figure(figsize=(10, 6))

plt.barh(
    chart_data.index,
    chart_data["Average_Rating"]
)

plt.title("Average Ratings of Common Cuisine Combinations")
plt.xlabel("Average Rating")
plt.ylabel("Cuisine Combination")

plt.xlim(0, 5)

plt.tight_layout()

plt.savefig(
    "outputs/task2_cuisine_combinations.png"
)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("dataset.csv")

# Display longitude and latitude information
print("Dataset shape:", df.shape)

print("\nGeographic columns:")
print(df[["Longitude", "Latitude"]].head())

# Check missing values
print("\nMissing geographic values:")
print(df[["Longitude", "Latitude"]].isnull().sum())

# Check basic statistics
print("\nGeographic statistics:")
print(df[["Longitude", "Latitude"]].describe())


# Select geographic columns and remove missing values
geo_df = df[["Longitude", "Latitude", "City"]].dropna().copy()

# Keep only valid coordinate ranges
geo_df = geo_df[
    (geo_df["Longitude"].between(-180, 180)) &
    (geo_df["Latitude"].between(-90, 90))
]

print("\nTotal valid restaurant locations:", len(geo_df))

print("\nCleaned geographic data:")
print(geo_df.head())


# Create the restaurant location plot
plt.figure(figsize=(12, 7))

plt.scatter(
    geo_df["Longitude"],
    geo_df["Latitude"],
    alpha=0.4,
    s=12
)

plt.title("Geographic Distribution of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.grid(True)
plt.tight_layout()

# Save the chart
plt.savefig("outputs/task3_geographic_analysis.png", dpi=300)

plt.show()

print("\nGeographic plot saved successfully!")


# Count restaurants in each city
city_counts = df["City"].value_counts()

# Display the top 10 cities
top_cities = city_counts.head(10)

print("\nTop 10 Cities with Most Restaurants:")
print(top_cities)

# Create a bar chart
plt.figure(figsize=(12, 6))

top_cities.plot(kind="bar")

plt.title("Top 10 Cities by Restaurant Count")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)

plt.tight_layout()

# Save the chart
plt.savefig("outputs/task3_top_restaurant_cities.png", dpi=300)

plt.show()


# Filter restaurant locations within India's approximate boundaries
india_df = geo_df[
    (geo_df["Longitude"].between(68, 97)) &
    (geo_df["Latitude"].between(6, 38)) &
    (geo_df["Longitude"] != 0) &
    (geo_df["Latitude"] != 0)
].copy()

print("\nRestaurants in India's geographic boundary:", len(india_df))

# Plot restaurant locations in India
plt.figure(figsize=(10, 8))

plt.scatter(
    india_df["Longitude"],
    india_df["Latitude"],
    alpha=0.4,
    s=12
)

plt.title("Geographic Distribution of Restaurants in India")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.grid(True)
plt.tight_layout()

plt.savefig("outputs/task3_india_geographic_analysis.png", dpi=300)

plt.show()


# Task 4: Restaurant Chains

# Select restaurant name and rating columns
chain_df = df[[
    "Restaurant Name",
    "Aggregate rating",
    "Votes"
]].dropna(subset=["Restaurant Name"]).copy()

# Count how many times each restaurant name appears
restaurant_counts = chain_df["Restaurant Name"].value_counts()

# Select restaurant names appearing at least twice
chains = restaurant_counts[restaurant_counts >= 2]

print("\nTop 10 Restaurant Chains by Outlet Count:")
print(chains.head(10))

print("\nTotal repeated restaurant names:", len(chains))


# Calculate ratings and popularity of restaurant chains

# Exclude restaurants with zero ratings
rated_chains = chain_df[chain_df["Aggregate rating"] > 0].copy()

# Group data by restaurant name
chain_analysis = rated_chains.groupby("Restaurant Name").agg(
    Outlet_Count=("Restaurant Name", "count"),
    Average_Rating=("Aggregate rating", "mean"),
    Total_Votes=("Votes", "sum")
)

# Keep only repeated restaurant names
chain_analysis = chain_analysis[
    chain_analysis.index.isin(chains.index)
]

# Sort by number of outlets
chain_analysis = chain_analysis.sort_values(
    by="Outlet_Count",
    ascending=False
)

print("\nRestaurant Chain Analysis:")
print(chain_analysis.head(10).round(2))


# Get the top 10 restaurant chains
top_chains = chains.head(10)

# Create a bar chart
plt.figure(figsize=(12, 6))

top_chains.sort_values().plot(kind="barh")

plt.title("Top 10 Restaurant Chains by Outlet Count")
plt.xlabel("Number of Restaurant Records")
plt.ylabel("Restaurant Name")

plt.tight_layout()

# Save chart
plt.savefig("outputs/task4_top_restaurant_chains.png", dpi=300)

plt.show()


# Select top 10 chains from the analysis table
top_rated_chains = chain_analysis.head(10)

# Create average rating chart
plt.figure(figsize=(12, 6))

top_rated_chains["Average_Rating"].sort_values().plot(kind="barh")

plt.title("Average Ratings of Top Restaurant Chains")
plt.xlabel("Average Rating")
plt.ylabel("Restaurant Name")

plt.xlim(0, 5)
plt.tight_layout()

# Save chart
plt.savefig("outputs/task4_chain_average_ratings.png", dpi=300)

plt.show()


# Most popular chain based on total votes
most_popular = chain_analysis.sort_values(
    by="Total_Votes",
    ascending=False
).iloc[0]

print("\nMost Popular Restaurant Chain:")
print(most_popular)

# Highest-rated chain with at least 5 rated records
reliable_chains = chain_analysis[
    chain_analysis["Outlet_Count"] >= 5
]

highest_rated = reliable_chains.sort_values(
    by="Average_Rating",
    ascending=False
).iloc[0]

print("\nHighest Rated Restaurant Chain:")
print(highest_rated)
