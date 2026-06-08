import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\Documents\IDX Exchange\Sold_Clean.csv")

df['CloseDate'] = pd.to_datetime(df['CloseDate'], errors='coerce')
df['PurchaseContractDate'] = pd.to_datetime(df['PurchaseContractDate'], errors='coerce')
df['ListingContractDate'] = pd.to_datetime(df['ListingContractDate'], errors='coerce')

df['ClosePrice'] = pd.to_numeric(df['ClosePrice'], errors='coerce')
df['ListPrice'] = pd.to_numeric(df['ListPrice'], errors='coerce')
df['OriginalListPrice'] = pd.to_numeric(df['OriginalListPrice'], errors='coerce')
df['LivingArea'] = pd.to_numeric(df['LivingArea'], errors='coerce')
df['DaysOnMarket'] = pd.to_numeric(df['DaysOnMarket'], errors='coerce')

# Price ratio
df['price_ratio'] = df['ClosePrice'] / df['ListPrice']

# Close to original list ratio
df['close_to_original_list_ratio'] = df['ClosePrice'] / df['OriginalListPrice']

# Price per square foot
df['price_per_sqft'] = df['ClosePrice'] / df['LivingArea']

# Days on market
df['days_on_market'] = df['DaysOnMarket']

# Year-Month
df['YrMo'] = df['CloseDate'].dt.year * 100 + df['CloseDate'].dt.month

# Listing to contract days
df['listing_to_contract_days'] = (
    df['PurchaseContractDate'] - df['ListingContractDate']
).dt.days

# Contract to close days
df['contract_to_close_days'] = (
    df['CloseDate'] - df['PurchaseContractDate']
).dt.days

summary_by_property = (
    df.groupby(['PropertyType', 'PropertySubType'])
      .agg(
          median_close_price=('ClosePrice', 'median'),
          avg_price_per_sqft=('price_per_sqft', 'mean'),
          avg_days_on_market=('DaysOnMarket', 'mean'),
          avg_price_ratio=('price_ratio', 'mean'),
          sales_count=('ClosePrice', 'count')
      )
      .reset_index()
)
summary_by_county = (
    df.groupby('CountyOrParish')
      .agg(
          median_close_price=('ClosePrice', 'median'),
          avg_price_per_sqft=('price_per_sqft', 'mean'),
          avg_days_on_market=('DaysOnMarket', 'mean'),
          avg_price_ratio=('price_ratio', 'mean'),
          sales_count=('ClosePrice', 'count')
      )
      .reset_index()
)

summary_by_mls_area = (
    df.groupby('MLSAreaMajor')
      .agg(
          median_close_price=('ClosePrice', 'median'),
          avg_price_per_sqft=('price_per_sqft', 'mean'),
          avg_days_on_market=('DaysOnMarket', 'mean'),
          avg_price_ratio=('price_ratio', 'mean'),
          sales_count=('ClosePrice', 'count')
      )
      .reset_index()
)

df.to_csv(r"C:\Users\Admin\Documents\IDX Exchange\sold_week6_features.csv", index=False)
summary_by_county.to_csv(r"C:\Users\Admin\Documents\IDX Exchange/week6_summary_by_county.csv", index=False)

print(df[['ClosePrice', 'price_ratio', 'price_per_sqft', 'YrMo']].head())
print(summary_by_county.head())