import pandas as pd


demo = pd.read_csv('censusdemographics_final.csv')
other = pd.read_csv('zip_poverty_tobacco_alcohol.csv')

demo.rename({'zipcode': 'zip'}, axis=1, inplace=True)
demo['zip'] = demo['zip'].astype(str)
demo = demo.drop(columns=['Unnamed: 0'])

other['zip'] = other['zip'].astype(str)


df = other.copy()

'''
B02001_001E     int64
B02008_001E     int64
B02009_001E     int64
B02010_001E     int64
B02011_001E     int64
B02012_001E     int64
B02013_001E     int64
B03001_002E     int64
B03001_003E     int64
'''

print(demo.dtypes)

df = df.merge(demo, on="zip")

print(df.head())


df.to_csv('combined_final.csv', index=False)