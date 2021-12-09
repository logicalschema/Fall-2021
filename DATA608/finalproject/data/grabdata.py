import pandas as pd
import numpy as np
import datetime


# tobacco
#Index(['DCA License Number', 'License Type', 'License Expiration Date',
#       'License Status', 'License Creation Date', 'Industry', 'Business Name',
#       'Business Name 2', 'Address Building', 'Address Street Name',
#       'Secondary Address Street Name', 'Address City', 'Address State',
#       'Address ZIP', 'Contact Phone Number', 'Address Borough',
#       'Borough Code', 'Community Board', 'Council District', 'BIN', 'BBL',
#       'NTA', 'Census Tract', 'Detail', 'Longitude', 'Latitude', 'Location'],
#      dtype='object')
# 'License Type', 'License Expiration Date', 'License Creation Date', 'Address ZIP', 'Borough Code'

#alcohol
#Index(['Serial Number', 'County', 'License Type Code', 'License Class Code',
#       'Certificate Number', 'Premise Name', 'DBA', 'Premise Address',
#       'Premise Address 2', 'Premise City', 'Premise State', 'Premise Zip',
#       'License Issued Date', 'License Expiration Date', 'Method of Operation',
#       'Days/Hours of Operation', 'Other', 'Georeference', 'Zone',
#       'Effective Date', 'Original Date'],
#      dtype='object')
#'County', 'License Type Code', 'License Class Code', 'Premise Zip', 'License Expiration Date', 'Effective Date'

# Zip codes found with valid data 
with open('zips_with_data_final.txt') as f:
    zipcodes = f.read().splitlines()

tobacco = pd.read_csv('Active_Tobacco_Retail_Dealer_Licenses.csv', low_memory=False)
alcohol = pd.read_csv('Liquor_Authority_Current_List_of_Active_Licenses.csv', low_memory=False)
poverty = pd.read_csv('poverty_final.csv')


# For cleaning the tobacco data
tobacco_cols = ['License Type', 'Address ZIP', 'Borough Code', 'License Creation Date', 'License Expiration Date']
tobacco = tobacco[tobacco_cols]

## Convert specific columns to other data types
tobacco['License Creation Date'] = pd.to_datetime(tobacco['License Creation Date'])
tobacco['License Expiration Date'] = pd.to_datetime(tobacco['License Expiration Date'])
tobacco['Address ZIP'] = tobacco['Address ZIP'].astype(str)


## Get tobacco licenses that were valid in 2019
# if creation < begin and [exp in 2019 or exp > 2019]
# if creation in 2019

begin = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2019,12,31)

tobacco = tobacco[
          (tobacco['License Creation Date'] <= begin) & ( pd.DatetimeIndex(tobacco['License Expiration Date']).year >= 2019)|
          (pd.DatetimeIndex(tobacco['License Creation Date']).year == 2019)     
	]


# For cleaning the alcohol data: removing non-NYC and unnecessary columns
alcohol_cols = ['County', 'License Type Code', 'License Class Code', 'Premise Zip', 'Effective Date', 'License Expiration Date']
alcohol = alcohol[alcohol_cols]
nyc = alcohol['County'].isin(['QUEENS', 'NEW YORK', 'KINGS', 'RICHMOND', 'BRONX'])
alcohol = alcohol[nyc]

## Cleaning an invalid zip listed as 014 or 694
alcohol['Premise Zip'].mask(alcohol['Premise Zip'] == '014', '10014', inplace=True)
alcohol['Premise Zip'].mask(alcohol['Premise Zip'] == '694', '11694', inplace=True)

## Truncating zip codes that have more than 5 characters
alcohol['Premise Zip'].mask(alcohol['Premise Zip'].str.len() > 5, alcohol['Premise Zip'].str[0:5], inplace=True)


## Convert specific columns to date
alcohol['License Expiration Date'] = pd.to_datetime(alcohol['License Expiration Date'])
alcohol['Effective Date'] = pd.to_datetime(alcohol['Effective Date'])

## Get alcohol licenses that are effective in 2019
# if effective date < begin and expiration >= 2019
# if effective date year = 2019

alcohol = alcohol[
          (alcohol['Effective Date'] < begin) & ( pd.DatetimeIndex(alcohol['License Expiration Date']).year >= 2019)|
          (pd.DatetimeIndex(alcohol['Effective Date']).year == 2019)     
    ]



# Cleanup of poverty dataframe

## Change zip to a string
poverty['zip'] = poverty['zip'].astype(str)

## Remove % and convert percentage to a float
poverty['percentage'] = poverty['percentage'].str.strip('%')
poverty['percentage'] = poverty['percentage'].astype(float)


alcohol_by_zip = alcohol.groupby(['Premise Zip']).size()

tobacco_by_zip = tobacco.groupby(['Address ZIP']).size()


# Make a copy of the poverty data, this will be our main dataframe
df = poverty.copy()

# Copy the counts for tobacco to df
counts = tobacco['Address ZIP'].value_counts()
counts = counts.to_frame().reset_index().rename({'index':'zip', 'Address ZIP': 'tobacco'}, axis='columns')

df = df.merge(counts, on="zip")

# Copy the counts for alcohol to df
counts = alcohol['Premise Zip'].value_counts()
counts = counts.to_frame().reset_index().rename({'index':'zip', 'Premise Zip': 'alcohol'}, axis='columns')

df = df.merge(counts, on="zip")

df.to_csv('zip_poverty_tobacco_alcohol.csv', index=False)