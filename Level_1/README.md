# Cognifyz Data Analysis Internship – Level 1

## Project overview
This project completes the four tasks listed in the Cognifyz Data Analysis Internship Level 1 task document using Python and the supplied restaurant dataset.

## Tasks
1. Top Cuisines – identify the three most common cuisines and calculate their percentages.
2. City Analysis – identify the city with the most restaurants and calculate average ratings by city.
3. Price Range Distribution – calculate category counts and percentages and create a bar chart.
4. Online Delivery – calculate delivery availability percentages and compare average ratings.

## Dataset
- File: `dataset.csv`
- Records: 9,551
- Columns: 21

## Requirements
- Python 3
- pandas
- matplotlib

Install dependencies:
```bash
python -m pip install pandas matplotlib
```

## Run the project
Keep `main.py` and `dataset.csv` in the same folder, then run:
```bash
python main.py
```

Charts are saved automatically in the `outputs` folder.

## Important interpretation note
The city with the highest average rating is Inner City (4.90), based on only two restaurant records. Average ratings from cities with very few records should be interpreted cautiously. In this dataset, London has the highest average rating (4.54) among cities with at least five restaurant records.

Percentages for cuisine counts use all 9,551 dataset records as the denominator. A restaurant may serve more than one cuisine, so cuisine percentages are not expected to add up to 100%.
