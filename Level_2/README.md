# Cognifyz Data Analysis Internship — Level 2

This project analyzes the supplied restaurant dataset across all four Level 2 tasks.

## Included
- `main.py` — complete reproducible Python analysis
- `dataset.csv` — supplied dataset copy
- `analysis_summary.csv` — key metrics and findings
- `outputs/` — 9 charts
- `task3_interactive_restaurant_map.html` — interactive clustered restaurant map

## Tasks
1. **Restaurant Ratings:** rating distribution and average votes.
2. **Cuisine Combinations:** most common multi-cuisine combinations and average ratings.
3. **Geographic Analysis:** global coordinates, approximate India coordinate view, top 10 cities, and interactive map.
4. **Restaurant Chains:** repeated restaurant names, ratings, and total votes.

## Run
Install dependencies:
```bash
pip install pandas numpy matplotlib folium
```
Keep `main.py` and `dataset.csv` in the same folder, then run:
```bash
python main.py
```

## Method notes
- A rating of `0.0` is treated as unrated when calculating average ratings.
- Cuisine combinations are normalized by trimming spaces, removing duplicates, sorting cuisine names, and joining them alphabetically.
- Cuisine-combination rating comparisons include combinations with at least 10 rated records.
- For Task 3, approximate India coordinate bounds are longitude 68–97 and latitude 6–38; this is a rectangular filter, not an official political boundary.
- For Task 4, repeated restaurant names are treated as **potential chains**, not independently verified corporate chains. Average ratings exclude `0.0`; the highest-rated comparison requires at least 5 rated records.
- Total votes are used as a rough popularity indicator, not a measure of customer count.

## No PDF report
This submission package intentionally contains no PDF report.
