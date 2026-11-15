
import pandas as pd

# Load the dataset
df = pd.read_csv("dataset.csv")

# Display dataset columns
print("Dataset Columns:")
print(df.columns.tolist())

# Display first five records
print("\nFirst Five Records:")
print(df.head())

# Check for review-related columns
print("\nReview-related columns:")
for column in df.columns:
    if "review" in column.lower() or "rating" in column.lower():
        print(column)

import matplotlib.pyplot as plt

# Count each rating category
rating_counts = df["Rating text"].value_counts()

print("\nRating Category Counts:")
print(rating_counts)

# Calculate average rating for each category
average_rating = df.groupby("Rating text")["Aggregate rating"].mean()

print("\nAverage Rating by Category:")
print(average_rating)

# Create a bar chart
rating_counts.plot(kind="bar", figsize=(8, 5))

plt.title("Distribution of Restaurant Rating Categories")
plt.xlabel("Rating Category")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("task1_rating_categories.png")
plt.show()

# Combine both analysis results
summary = pd.DataFrame({
    "Restaurant Count": rating_counts,
    "Average Rating": average_rating
})

# Save results
summary.to_csv("task1_restaurant_reviews_summary.csv")

print("\nAnalysis saved successfully!")
print(summary)

# Task 1 - Final Summary

print("\n========== TASK 1 SUMMARY ==========")

print("Total restaurants analysed:", len(df))

print("\nRating Category Distribution:")
print(rating_counts)

print("\nAverage Rating by Category:")
print(average_rating)

print("\nNote: Written customer reviews are not available")
print("in the supplied dataset.")

import os

print("\n========== OUTPUT FILE CHECK ==========")

files = [
    "task1_rating_categories.png",
    "task1_restaurant_reviews_summary.csv"
]

for file in files:
    if os.path.exists(file):
        print(file, "- Created successfully")
    else:
        print(file, "- Not found")

# Final Conclusion

print("\n========== CONCLUSION ==========")

print("Restaurant rating categories were analysed successfully.")
print("A bar chart was generated to visualise rating distribution.")
print("Average ratings were calculated for each category.")
print("Written review text was not available in the dataset.")
print("Sentiment and review-length analysis require review text.")

# ==========================================
# LEVEL 3 - TASK 2: VOTES ANALYSIS
# ==========================================

print("\n========== TASK 2: VOTES ANALYSIS ==========")

# Restaurant with highest votes
highest_votes = df.loc[df["Votes"].idxmax()]

print("\nRestaurant with Highest Votes:")
print("Restaurant Name:", highest_votes["Restaurant Name"])
print("Votes:", highest_votes["Votes"])
print("Aggregate Rating:", highest_votes["Aggregate rating"])

# Restaurant with lowest votes
lowest_votes = df.loc[df["Votes"].idxmin()]

print("\nRestaurant with Lowest Votes:")
print("Restaurant Name:", lowest_votes["Restaurant Name"])
print("Votes:", lowest_votes["Votes"])
print("Aggregate Rating:", lowest_votes["Aggregate rating"])

# Correlation between Votes and Aggregate Rating

correlation = df["Votes"].corr(df["Aggregate rating"])

print("\n========== VOTES AND RATINGS CORRELATION ==========")

print("Correlation:", round(correlation, 3))

if correlation > 0:
    print("There is a positive correlation between votes and ratings.")
elif correlation < 0:
    print("There is a negative correlation between votes and ratings.")
else:
    print("There is no linear correlation between votes and ratings.")

# Scatter Plot: Votes vs Aggregate Rating

import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

plt.scatter(
    df["Votes"],
    df["Aggregate rating"],
    alpha=0.4
)

plt.title("Restaurant Votes vs Aggregate Ratings")
plt.xlabel("Number of Votes")
plt.ylabel("Aggregate Rating")
plt.grid(True)

plt.tight_layout()
plt.savefig("task2_votes_vs_ratings.png")
plt.show()

# Average Votes Analysis

average_votes = df["Votes"].mean()
median_votes = df["Votes"].median()
total_votes = df["Votes"].sum()

print("\n========== AVERAGE VOTES ANALYSIS ==========")

print("Total Votes:", total_votes)
print("Average Votes:", round(average_votes, 2))
print("Median Votes:", median_votes)

# Top 10 Restaurants by Votes

top_10_votes = df.nlargest(10, "Votes")[
    ["Restaurant Name", "City", "Votes", "Aggregate rating"]
]

print("\n========== TOP 10 MOST-VOTED RESTAURANTS ==========")

print(top_10_votes.to_string(index=False))

# Save the results
top_10_votes.to_csv("task2_top_10_restaurants.csv", index=False)

print("\nTop 10 restaurants saved successfully!")

# Bar Chart: Top 10 Restaurants by Votes

plt.figure(figsize=(12, 6))

plt.barh(
    top_10_votes["Restaurant Name"],
    top_10_votes["Votes"]
)

plt.title("Top 10 Restaurants by Number of Votes")
plt.xlabel("Number of Votes")
plt.ylabel("Restaurant Name")

plt.gca().invert_yaxis()
plt.tight_layout()

plt.savefig("task2_top_10_votes.png")
plt.show()

# Task 2 - Votes Analysis Summary

votes_summary = pd.DataFrame({
    "Metric": [
        "Total Restaurants",
        "Total Votes",
        "Average Votes",
        "Median Votes",
        "Votes-Rating Correlation"
    ],
    "Value": [
        len(df),
        total_votes,
        round(average_votes, 2),
        median_votes,
        round(correlation, 3)
    ]
})

votes_summary.to_csv("task2_votes_analysis_summary.csv", index=False)

print("\n========== TASK 2 SUMMARY ==========")
print(votes_summary.to_string(index=False))

print("\nTask 2 summary saved successfully!")

# Task 2 - Final Conclusion

print("\n========== TASK 2 CONCLUSION ==========")

print("1. Identified restaurants with the highest and lowest votes.")
print("2. Calculated total, average and median votes.")
print("3. Analysed the relationship between votes and ratings.")
print("4. Created a scatter plot for votes and ratings.")
print("5. Identified and visualised the top 10 most-voted restaurants.")

print("\nTask 2 analysis completed successfully!")

# ==========================================
# LEVEL 3 - TASK 3
# PRICE RANGE VS ONLINE DELIVERY AND TABLE BOOKING
# ==========================================

print("\n========== TASK 3: SERVICE AVAILABILITY ==========")

# Group restaurants by price range
service_analysis = df.groupby("Price range").agg(
    Total_Restaurants=("Restaurant ID", "count"),
    Online_Delivery=("Has Online delivery",
                     lambda x: (x == "Yes").sum()),
    Table_Booking=("Has Table booking",
                   lambda x: (x == "Yes").sum())
)

print("\nService Availability by Price Range:")
print(service_analysis)

# Calculate Service Availability Percentages

service_analysis["Online Delivery %"] = (
    service_analysis["Online_Delivery"] /
    service_analysis["Total_Restaurants"] * 100
)

service_analysis["Table Booking %"] = (
    service_analysis["Table_Booking"] /
    service_analysis["Total_Restaurants"] * 100
)

print("\n========== SERVICE AVAILABILITY PERCENTAGES ==========")

print(service_analysis.round(2))

# Compare Online Delivery and Table Booking

import numpy as np

price_ranges = service_analysis.index.astype(str)

x = np.arange(len(price_ranges))
width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(
    x - width / 2,
    service_analysis["Online Delivery %"],
    width,
    label="Online Delivery"
)

plt.bar(
    x + width / 2,
    service_analysis["Table Booking %"],
    width,
    label="Table Booking"
)

plt.title("Online Delivery and Table Booking by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Availability Percentage (%)")

plt.xticks(x, price_ranges)
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("task3_service_availability.png")
plt.show()

# Identify Highest Service Availability

highest_delivery = service_analysis["Online Delivery %"].idxmax()

highest_booking = service_analysis["Table Booking %"].idxmax()

print("\n========== HIGHEST SERVICE AVAILABILITY ==========")

print(
    "Highest Online Delivery:",
    "Price Range", highest_delivery
)

print(
    "Delivery Availability:",
    round(service_analysis.loc[highest_delivery, "Online Delivery %"], 2),
    "%"
)

print(
    "\nHighest Table Booking:",
    "Price Range", highest_booking
)

print(
    "Table Booking Availability:",
    round(service_analysis.loc[highest_booking, "Table Booking %"], 2),
    "%"
)

# Compare Lowest and Highest Price Ranges

lowest_price = service_analysis.index.min()
highest_price = service_analysis.index.max()

print("\n========== PRICE RANGE COMPARISON ==========")

print("\nLowest Price Range:", lowest_price)
print(
    "Online Delivery:",
    round(service_analysis.loc[lowest_price, "Online Delivery %"], 2),
    "%"
)
print(
    "Table Booking:",
    round(service_analysis.loc[lowest_price, "Table Booking %"], 2),
    "%"
)

print("\nHighest Price Range:", highest_price)
print(
    "Online Delivery:",
    round(service_analysis.loc[highest_price, "Online Delivery %"], 2),
    "%"
)
print(
    "Table Booking:",
    round(service_analysis.loc[highest_price, "Table Booking %"], 2),
    "%"
)

# Online Delivery Availability Chart

plt.figure(figsize=(8, 5))

plt.bar(
    price_ranges,
    service_analysis["Online Delivery %"]
)

plt.title("Online Delivery Availability by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Online Delivery (%)")

plt.tight_layout()
plt.savefig("task3_online_delivery.png")
plt.show()


# Table Booking Availability Chart

plt.figure(figsize=(8, 5))

plt.bar(
    price_ranges,
    service_analysis["Table Booking %"]
)

plt.title("Table Booking Availability by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Table Booking (%)")

plt.tight_layout()
plt.savefig("task3_table_booking.png")
plt.show()

# Save Task 3 Analysis Results

service_analysis.to_csv("task3_price_range_service_analysis.csv")

print("\n========== TASK 3 RESULTS ==========")

print(service_analysis.round(2))

print("\nTask 3 analysis saved successfully!")

# Task 3 - Final Conclusion

print("\n========== TASK 3 CONCLUSION ==========")

print("1. Analysed restaurants across different price ranges.")
print("2. Calculated online delivery availability percentages.")
print("3. Calculated table booking availability percentages.")
print("4. Compared service availability across price categories.")
print("5. Created three visualisations.")
print("6. Exported the analysis results to a CSV file.")

print("\nLevel 3 - Task 3 completed successfully!")