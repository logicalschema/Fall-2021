import pandas as pd
import censusdata
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

'''
B02001_001E Total
B02008_001E	WHITE ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
B02009_001E BLACK OR AFRICAN AMERICAN ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
B02010_001E 	AMERICAN INDIAN AND ALASKA NATIVE ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
B02011_001E 	ASIAN ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
B02012_001E 	NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
B02013_001E 	SOME OTHER RACE ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
B03001_002E	Not HISPANIC OR LATINO ORIGIN BY SPECIFIC ORIGIN
B03001_003E HISPANIC OR LATINO ORIGIN BY SPECIFIC ORIGIN
'''




# New York is 36

'''
data = censusdata.download('acs5', 2019,
           censusdata.censusgeo([('state', '36'), ('zip code tabulation area', '11373')]),
          ['', 'B02001_001E', 'B02008_001E', 'B02009_001E', 'B02010_001E',
           'B02011_001E', 'B02012_001E', 'B02013_001E',
           'B03001_002E', 'B03001_003E'])
'''
df = pd.DataFrame()



with open('goodzips.txt') as f:
    lines = f.readlines()

for line in lines:
    zipcode = line.strip()
    row = censusdata.download('acs5', 2019,
           censusdata.censusgeo([('state', '36'), ('zip code tabulation area', zipcode)]),
          ['B02001_001E', 'B02008_001E', 'B02009_001E', 'B02010_001E', 'B02011_001E', 'B02012_001E', 'B02013_001E', 'B03001_002E', 'B03001_003E'])
    row["zipcode"] = zipcode
    df = df.append(row, ignore_index=False) 

print(df.head)
df.to_csv("censusdemographics.csv", encoding='utf-8')