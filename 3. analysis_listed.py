#add latest dfyyyymm
#add to frames


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import numpy as np
import datetime

import csv
import calendar




df202401 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202401.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202402 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202402.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202403 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202403.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202404 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202404.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202405 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202405.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202406 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202406.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202407 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202407.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202408 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202408.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202409 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202409.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202410 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202410.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202411 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202411.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202412 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202412.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202501 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202501.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202502 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202502.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202503 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202503.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202504 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202504.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202505 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202505.csv", encoding = "ISO-8859-1") # df is Pandas dataframe

df202506 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202506.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202507 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202507.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202508 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202508.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202509 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202509.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202510 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202510.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202511 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202511.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202512 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202512.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202601 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202601.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202602 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202602.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202603 = pd.read_csv("/Users/idxexchange/Desktop/crmls/CRMLSListing202603.csv", encoding = "ISO-8859-1") # df is Pandas dataframe


frames=[df202401,df202402,df202403,df202404,df202405, df202406, df202407, df202408, df202409, df202410, df202411, df202412, df202501, df202502, df202503, df202504, df202505,df202506, df202507, df202508, df202509,df202510,df202511,df202512, df202601, df202602, df202603]
combine=pd.concat(frames)

main=combine.copy()

main= main[main.PropertyType=='Residential']
#main= main[main.PropertySubType=='SingleFamilyResidence']



###########

newlistings=main.copy()
newlistings.to_csv('/Users/Admin/Desktop/crmls/newlistings.csv', index=False)



