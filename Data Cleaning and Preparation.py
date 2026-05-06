import pandas as pd

sold = pd.read_csv(r'C:/Users/Admin/Desktop/crmls/priceratio.csv')
listings = pd.read_csv(r'C:/Users/Admin/Desktop/crmls/newlistings.csv')

def clean_df(df):
    df = df.copy()

    # dates
    for col in ['CloseDate', 'ListingContractDate', 'PurchaseContractDate', 'ContractStatusChangeDate']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # numeric columns
    for col in ['ClosePrice', 'LivingArea', 'DaysOnMarket', 'Latitude', 'Longitude']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # drop unneeded columns
    columns_to_drop = ['Flooring', 'ViewYN', 'PoolPrivateYN']
    existing_cols = [c for c in columns_to_drop if c in df.columns]
    df = df.drop(columns=existing_cols)

    # flags
    if {'ListingContractDate', 'CloseDate'}.issubset(df.columns):
        df['listing_after_close_flag'] = df['ListingContractDate'] > df['CloseDate']
    if {'PurchaseContractDate', 'CloseDate'}.issubset(df.columns):
        df['purchase_after_close_flag'] = df['PurchaseContractDate'] > df['CloseDate']
    if {'PurchaseContractDate', 'ListingContractDate'}.issubset(df.columns):
        df['negative_timeline_flag'] = df['PurchaseContractDate'] < df['ListingContractDate']

    if {'Latitude', 'Longitude'}.issubset(df.columns):
        df['missing_coords'] = df['Latitude'].isnull() | df['Longitude'].isnull()
        df['zero_coords'] = (df['Latitude'] == 0) | (df['Longitude'] == 0)
        df['invalid_longitude'] = df['Longitude'] > 0

    # remove invalid numeric rows
    if 'ClosePrice' in df.columns:
        df = df[df['ClosePrice'].isna() | (df['ClosePrice'] > 0)]
    if 'LivingArea' in df.columns:
        df = df[df['LivingArea'].isna() | (df['LivingArea'] > 0)]
    if 'DaysOnMarket' in df.columns:
        df = df[df['DaysOnMarket'].isna() | (df['DaysOnMarket'] >= 0)]

# Geographic flags
    if "Latitude" in df.columns and "Longitude" in df.columns:
        df["geo_missing_flag"] = df["Latitude"].isna() | df["Longitude"].isna()
        df["geo_zero_flag"] = (df["Latitude"] == 0) | (df["Longitude"] == 0)
        df["geo_positive_lon_flag"] = df["Longitude"].notna() & (df["Longitude"] > 0)
        df["geo_out_of_state_flag"] = (
            df["Latitude"].notna() & df["Longitude"].notna() &
            ~(df["Latitude"].between(32.5, 42.0) & df["Longitude"].between(-124.5, -114.1))
        )
    return df

print("Sold rows before:", len(sold))
sold_clean = clean_df(sold)
print("Sold rows after:", len(sold_clean))

print("Listings rows before:", len(listings))
listings_clean = clean_df(listings)
print("Listings rows after:", len(listings_clean))

sold_clean.to_csv(r'C:/Users/Admin/Desktop/crmls/sold_cleaned_data.csv', index=False)
listings_clean.to_csv(r'C:/Users/Admin/Desktop/crmls/listings_cleaned_data.csv', index=False)