from urllib.request import urlopen
import json


#https://data.cityofnewyork.us/Business/Zip-Code-Boundaries/i8iw-xf4u
with open('nyc_zip.json') as fp:
    counties = json.load(fp)



import pandas as pd
df = pd.read_csv("test.csv",
                   dtype={"postalCode": str, "unemp": float})

import plotly.express as px



fig = px.choropleth_mapbox(df, geojson=counties, locations='postalCode', color='unemp',
                           featureidkey="properties.ZIP",
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": 40.70229736498986, "lon": -74.01581689028704},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()