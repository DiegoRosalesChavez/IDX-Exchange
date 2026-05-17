import pandas as pd
import numpy as np

df = pd.read_csv(r"C:/Users/Admin/Desktop/crmls/sold_week6_features.csv")

# Make sure key numeric fields are numeric
for col in ["ClosePrice", "LivingArea", "DaysOnMarket"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        
full_df = df.copy()

df["invalid_closeprice_flag"] = df["ClosePrice"] <= 0
df["invalid_livingarea_flag"] = df["LivingArea"] <= 0
df["invalid_dom_flag"] = df["DaysOnMarket"] < 0


# CLOSE PRICE IQR
Q1 = df['ClosePrice'].quantile(0.25)
Q3 = df['ClosePrice'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['closeprice_outlier_flag'] = (df['ClosePrice'] < lower) | (df['ClosePrice'] > upper)


# LIVING AREA IQR
Q1 = df['LivingArea'].quantile(0.25)
Q3 = df['LivingArea'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['livingarea_outlier_flag'] = (df['LivingArea'] < lower) | (df['LivingArea'] > upper)

# DAYS ON MARKET IQR
Q1 = df['DaysOnMarket'].quantile(0.25)
Q3 = df['DaysOnMarket'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['daysonmarket_outlier_flag'] = (df['DaysOnMarket'] < lower) | (df['DaysOnMarket'] > upper)


# Clean dataset: remove invalid rows and outliers
clean_df = df[
    (~df["invalid_closeprice_flag"]) &
    (~df["invalid_livingarea_flag"]) &
    (~df["invalid_dom_flag"]) &
    (~df["closeprice_outlier_flag"]) &
    (~df["livingarea_outlier_flag"]) &
    (~df["daysonmarket_outlier_flag"])
].copy()

# Comparison for the deliverable
print("Rows before filtering:", len(full_df))
print("Rows after filtering:", len(clean_df))

print("\nMedian values before filtering:")
print(full_df[["ClosePrice", "LivingArea", "DaysOnMarket"]].median(numeric_only=True))

print("\nMedian values after filtering:")
print(clean_df[["ClosePrice", "LivingArea", "DaysOnMarket"]].median(numeric_only=True))


df.to_csv("week7_flagged.csv", index=False)
clean_df.to_csv("week7_clean.csv", index=False)