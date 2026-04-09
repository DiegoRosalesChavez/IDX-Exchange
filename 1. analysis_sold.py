

#Steps
#add new dfyyyymm line and add to frames line




import pandas as pd
import numpy as np






# Load data

df202401 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202401_filled.csv", encoding="ISO-8859-1")
df202402 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202402.csv", encoding="ISO-8859-1")
df202403 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202403_filled.csv", encoding="ISO-8859-1")
df202404 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202404_filled.csv", encoding="ISO-8859-1")
df202405 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202405_filled.csv", encoding="ISO-8859-1")
df202406 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202406_filled.csv", encoding="ISO-8859-1")
df202407 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202407_filled.csv", encoding="ISO-8859-1")
df202408 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202408.csv", encoding="ISO-8859-1")
df202409 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202409.csv", encoding="ISO-8859-1")
df202410 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202410.csv", encoding="ISO-8859-1")
df202411 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202411.csv", encoding="ISO-8859-1")
df202412 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202412.csv", encoding="ISO-8859-1")

df202501 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202501_filled.csv", encoding="ISO-8859-1")
df202502 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202502.csv", encoding="ISO-8859-1")
df202503 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202503.csv", encoding="ISO-8859-1")
df202504 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202504.csv", encoding="ISO-8859-1")
df202505 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202505.csv", encoding="ISO-8859-1")
df202506 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202506.csv", encoding="ISO-8859-1")
df202507 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202507.csv", encoding="ISO-8859-1")
df202508 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202508.csv", encoding="ISO-8859-1")
df202509 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202509.csv", encoding="ISO-8859-1")
df202510 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202510.csv", encoding="ISO-8859-1")
df202511 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202511.csv", encoding="ISO-8859-1")
df202512 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202512.csv", encoding="ISO-8859-1")

df202601 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202601.csv", encoding="ISO-8859-1")
df202602 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202602.csv", encoding="ISO-8859-1")
df202603 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSSold202603.csv", encoding="ISO-8859-1")



# Combine dataframes
frames = [df202401, df202402, df202403, df202404, df202405, df202406, df202407, df202408, df202409, df202410, df202411, df202412, df202501,df202502, df202503, df202504, df202505, df202506, df202507, df202508, df202509, df202510, df202511, df202512, df202601, df202602, df202603]
combine = pd.concat(frames)



# Count missing values in Latitude and Longitude columns
missing_latitude_count = combine['Latitude'].isnull().sum()
print(f"Number of observations with missing latitude values: {missing_latitude_count}")

missing_longitude_count = combine['Longitude'].isnull().sum()
print(f"Number of observations with missing longitude values: {missing_longitude_count}")

# Total number of observations
total_observations = combine.shape[0]
print(f"Total number of observations: {total_observations}")

# Convert the 'CloseDate' column to datetime if it isn't already
combine['CloseDate'] = pd.to_datetime(combine['CloseDate'], errors='coerce')

main=combine.copy()


columns_to_drop = [
    'Flooring', 'ViewYN', 'WaterfrontYN', 'BasementYN', 'PoolPrivateYN',
    'ListAgentEmail', 'ListAgentFirstName', 'ListAgentLastName', 'CoListAgentFirstName',
    'CoListAgentLastName', 'AssociationFeeFrequency', 'AboveGradeFinishedArea', 
    'ListingKeyNumeric', 'MLSAreaMajor', 'TaxAnnualAmount', 'MlsStatus', 
    'ElementarySchool', 'BuilderName', 'BuyerOfficeAOR', 'BuyerAgencyCompensationType',
    'StreetNumberNumeric', 'BuyerAgencyCompensation', 'TaxYear', 'ContractStatusChangeDate',
    'ElementarySchoolDistrict', 'CoBuyerAgentFirstName', 'PurchaseContractDate',
    'ListingContractDate', 'BelowGradeFinishedArea', 'BusinessType', 'MiddleOrJuniorSchool',
    'FireplaceYN', 'HighSchool', 'HighSchoolDistrict', 'AssociationFee', 
    'MiddleOrJuniorSchoolDistrict', 'latfilled', 'lonfilled', 'BuyerAgentAOR', 
    'ListAgentAOR'
]

main = main.drop(columns=columns_to_drop)


# Define the start date as January 1, 2023
start_date = pd.Timestamp('2023-01-01')

# Filter the DataFrame to keep only observations from January 1, 2023, onwards
filtered_data = main[main['CloseDate'] >= start_date]

# Update 'main' DataFrame with the filtered data
main = filtered_data.copy()



main['CloseDate'] = pd.to_datetime(main['CloseDate'])
main['soldyear'] = main['CloseDate'].dt.year
main['soldmonth'] = main['CloseDate'].dt.month
main['yrmo']=main['soldyear']*100+main['soldmonth']




main['priceratio']=main['ClosePrice']/main['OriginalListPrice']
main= main[main.PropertyType=='Residential']
#main= main[main.PropertySubType=='SingleFamilyResidence']

main['q25'] = main.groupby(['yrmo'])['priceratio'].transform(lambda x: x.quantile(.25))
main['q75'] = main.groupby(['yrmo'])['priceratio'].transform(lambda x: x.quantile(.75))
main['iqr']=main.q75-main.q25
main['lowoutlier']=main.q25-1.5*main.iqr
main['highoutlier']=main.q75+1.5*main.iqr

main['q25dom'] = main.groupby(['yrmo'])['DaysOnMarket'].transform(lambda x: x.quantile(.25))
main['q75dom'] = main.groupby(['yrmo'])['DaysOnMarket'].transform(lambda x: x.quantile(.75))
main['iqrdom']=main.q75dom-main.q25dom
main['lowoutlierdom']=main.q25dom-1.5*main.iqrdom
main['highoutlierdom']=main.q75dom+1.5*main.iqrdom

main['pricesqft']=main['ClosePrice']/main['LivingArea']


###########


priceratio=main.copy()



# Update priceratio to NaN if it's less than lowoutlier or greater than highoutlier
priceratio['priceratio'] = np.where(
    (priceratio['priceratio'] < priceratio['lowoutlier']) | (priceratio['priceratio'] > priceratio['highoutlier']),
    np.nan,
    priceratio['priceratio']
)


# Update DaysOnMarket to NaN if it's less than lowoutlierdom or greater than highoutlierdom
priceratio['DaysOnMarket'] = np.where(
    (priceratio['DaysOnMarket'] < priceratio['lowoutlierdom']) | (priceratio['DaysOnMarket'] > priceratio['highoutlierdom']),
    np.nan,
    priceratio['DaysOnMarket']
)



columns_to_drop2 = [
    'soldyear', 'soldmonth', 'yrmo', 'q25', 'q75', 'iqr', 
    'lowoutlier', 'highoutlier', 'q25dom', 'q75dom', 'iqrdom', 'lowoutlierdom', 'highoutlierdom'
]

priceratio = priceratio.drop(columns=columns_to_drop2)




priceratio.to_csv('/Users/Admin/Desktop/crmls/priceratio.csv', index=False)




