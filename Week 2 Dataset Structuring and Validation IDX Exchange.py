import pandas as pd

# Data that is going to be used
sold = pd.read_csv('C:/Users/Admin/Documents/IDX Exchange/priceratioMay.csv')
listings = pd.read_csv('C:/Users/Admin/Documents/IDX Exchange/newlistingsMay.csv')

# Info in Data Sets
print("Sold Dataset Info:")
print(sold.info())
print("\nFirst 5 rows of Listings:")
print(listings.head())

print("\nUnique Property Types found:", sold['PropertyType'].unique())

# Filter to only show residentials
sold_res = sold[sold['PropertyType'] == 'Residential'].copy()
listings_res = listings[listings['PropertyType'] == 'Residential'].copy()

# Calculate the percentage of missing values per column
null_counts = sold_res.isnull().sum()
null_pct = sold_res.isnull().mean() * 100
missing_report = pd.DataFrame({'Null Count': null_counts, 'Percentage': null_pct})
print("\nColumns with more than 90% missing values:")
print(null_pct[null_pct > 90])

# Code to generate min, max, mean, median, and percentiles for the boxplot and Histogram
stats_fields = ['ClosePrice', 'ListPrice', 'OriginalListPrice', 'LivingArea',
'LotSizeAcres', 'BedroomsTotal', 'BathroomsTotalInteger', 'DaysOnMarket',  'YearBuilt']
print("\nNumeric Distribution Summary for Sold Residential:")
print(sold_res[stats_fields].describe(percentiles=[.25, .5, .75]))
print(f"\nMedian Close Price: ${sold_res['ClosePrice'].median():,.2f}")
print(f"Average Close Price: ${sold_res['ClosePrice'].mean():,.2f}")
