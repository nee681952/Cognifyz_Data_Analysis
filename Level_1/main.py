"""
Cognifyz Technologies - Data Analysis Internship
Level 1: Tasks 1 to 4
Dataset: dataset.csv

Run:
    python -m pip install pandas matplotlib
    python main.py

The script prints task results and saves charts in the outputs folder.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# -------------------- SETUP --------------------

DATA_FILE = "dataset.csv"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_FILE)
total_restaurants = len(df)

print("=" * 60)
print("COGNIFYZ DATA ANALYSIS INTERNSHIP - LEVEL 1")
print("=" * 60)
print(f"Dataset rows: {df.shape[0]}")
print(f"Dataset columns: {df.shape[1]}")

# -------------------- TASK 1: TOP CUISINES --------------------

print("\nTASK 1: TOP CUISINES")

cuisines = (
    df["Cuisines"]
    .dropna()
    .astype(str)
    .str.split(",")
    .explode()
    .str.strip()
)

cuisine_counts = cuisines.value_counts()
top_3_cuisines = cuisine_counts.head(3)
top_3_percentages = (top_3_cuisines / total_restaurants) * 100

for cuisine, count in top_3_cuisines.items():
    print(f"{cuisine}: {count} restaurants "
          f"({top_3_percentages[cuisine]:.2f}%)")

plt.figure(figsize=(8, 5))
plt.bar(top_3_cuisines.index, top_3_cuisines.values)
plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=12, ha="right")
for i, count in enumerate(top_3_cuisines.values):
    plt.text(i, count + 40, f"{count:,}", ha="center")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "task1_top_cuisines.png"), dpi=160)
plt.close()

# -------------------- TASK 2: CITY ANALYSIS --------------------

print("\nTASK 2: CITY ANALYSIS")

city_counts = df["City"].value_counts()
most_restaurants_city = city_counts.idxmax()
most_restaurants_count = city_counts.max()

print(f"City with the most restaurants: {most_restaurants_city}")
print(f"Number of restaurants: {most_restaurants_count}")

city_average_ratings = (
    df.groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
)

highest_rated_city = city_average_ratings.idxmax()
highest_city_average = city_average_ratings.max()
highest_city_count = df["City"].value_counts()[highest_rated_city]

print(f"City with the highest average rating: {highest_rated_city}")
print(f"Average rating: {highest_city_average:.2f}")
print(f"Number of restaurants in that city: {highest_city_count}")

print("\nTop 10 cities by average rating:")
print(city_average_ratings.head(10).round(2))

top_cities = city_counts.head(10)
plt.figure(figsize=(9, 5))
plt.barh(top_cities.index[::-1], top_cities.values[::-1])
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
for i, count in enumerate(top_cities.values[::-1]):
    plt.text(count + 25, i, f"{count:,}", va="center")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "task2_top_cities.png"), dpi=160)
plt.close()

# -------------------- TASK 3: PRICE RANGE DISTRIBUTION --------------------

print("\nTASK 3: PRICE RANGE DISTRIBUTION")

price_counts = df["Price range"].value_counts().sort_index()
price_percentages = (price_counts / total_restaurants) * 100

for price_range, count in price_counts.items():
    print(f"Price Range {price_range}: {count} restaurants "
          f"({price_percentages[price_range]:.2f}%)")

plt.figure(figsize=(8, 5))
plt.bar(price_counts.index.astype(str), price_counts.values)
plt.title("Restaurant Price Range Distribution")
plt.xlabel("Price Range Category")
plt.ylabel("Number of Restaurants")
for i, count in enumerate(price_counts.values):
    plt.text(i, count + 45, f"{count:,}", ha="center")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "task3_price_range.png"), dpi=160)
plt.close()

# -------------------- TASK 4: ONLINE DELIVERY --------------------

print("\nTASK 4: ONLINE DELIVERY")

delivery_counts = df["Has Online delivery"].value_counts()
delivery_percentages = (delivery_counts / total_restaurants) * 100

for delivery, count in delivery_counts.items():
    print(f"Online delivery {delivery}: {count} restaurants "
          f"({delivery_percentages[delivery]:.2f}%)")

average_ratings_by_delivery = (
    df.groupby("Has Online delivery")["Aggregate rating"].mean()
)

print("\nAverage ratings by online delivery:")
for delivery, rating in average_ratings_by_delivery.items():
    print(f"{delivery}: {rating:.2f}")

higher_rating_group = average_ratings_by_delivery.idxmax()
print(f"Group with the higher average rating: {higher_rating_group}")

ordered_delivery_counts = delivery_counts.reindex(["Yes", "No"])
plt.figure(figsize=(7, 5))
plt.bar(ordered_delivery_counts.index, ordered_delivery_counts.values)
plt.title("Restaurants by Online Delivery Availability")
plt.xlabel("Has Online Delivery")
plt.ylabel("Number of Restaurants")
for i, count in enumerate(ordered_delivery_counts.values):
    plt.text(i, count + 45, f"{count:,}", ha="center")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "task4_delivery_counts.png"), dpi=160)
plt.close()

ordered_average_ratings = average_ratings_by_delivery.reindex(["Yes", "No"])
plt.figure(figsize=(7, 5))
plt.bar(ordered_average_ratings.index, ordered_average_ratings.values)
plt.title("Average Rating by Online Delivery Availability")
plt.xlabel("Has Online Delivery")
plt.ylabel("Average Aggregate Rating")
plt.ylim(0, 5)
for i, rating in enumerate(ordered_average_ratings.values):
    plt.text(i, rating + 0.08, f"{rating:.2f}", ha="center")
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "task4_delivery_average_ratings.png"),
    dpi=160
)
plt.close()

print("\nAll Level 1 tasks completed.")
print(f"Charts saved in: {OUTPUT_DIR}")
