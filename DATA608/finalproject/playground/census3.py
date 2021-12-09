import pandas as pd

df1 = pd.read_csv('censusdemographics.csv')
df2 = pd.read_csv('censusdemographics2.csv')


frames = [df1, df2]


df = pd.concat(frames)


df.to_csv('censusdemographics_final.csv', index=False)