import json
import gzip
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px


# app initialize
dash_app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

app = dash_app.server
dash_app.config["suppress_callback_exceptions"] = True



def build_banner():
   return html.Div(
      id="banner",
      className="banner",
      children=[
        html.Img(src=dash_app.get_asset_url("cunysps_2021_2linelogo_spsblue_1.png"), style={'height':'75%', 'width':'75%'}),
        html.H6("NYC Tobacco and Alcohol Licenses 2019"),
        ],
    )

def build_graph_title(title):
   return html.P(className="graph-title", children=title)


dash_app.layout = html.Div(
  children=[ 
    html.Div(
        id="top-row",
        children=[
            html.Div(
               className="row",
               id="top-row-header",
               children=[
                  html.Div(
                     className="column",
                     id="header-container",
                     children=[
                         build_banner(),
                         html.P(
                            id="instructions",
                            children=["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]
                         ),
                         build_graph_title("Species"),
                         dcc.Dropdown(
                           id="spc-dropdown",
                           options=[
                               {"label": i, "value": i} for i in spc
                           ],
                           multi=True,
                           value=[spc[0], spc[1], spc[52]],
                           ),
                         build_graph_title("Borough(s)"),
                         dcc.Dropdown(
                           id="borough-dropdown",
                           options=[
                               {"label": i, "value": i} for i in boro
                           ],
                           multi=True,
                           value=[boro[0], boro[1], boro[2], boro[3], boro[4]]
                           ),
                         build_graph_title("Steward(s)"),
                         dcc.Slider(
                           id="steward-slider",
                           min=0,
                           max=3,
                           step=None,
                           marks={
                               # 'None' '1or2' '3or4' '4orMore'
                               0: 'None',
                               1: '1 or 2',
                               2: '3 or 4',
                               3: '4 or More'
                           },
                           value=3
                           )

                   ]
                  ),
                  html.Div(
                     className="column",
                     id="top-row-graphs",
                     children=[

                          html.Div(
                            id="map",
                            className="row",
                            children=[
                            # dcc Graph here
                               dcc.Graph(id='map-graph')
                            ]

                          )
                     ]
                  ),
               ]
            ),
          ]
    ),
    html.Div(
      id="bottom-row",
      children=[
          html.Div(
              className="bottom-row",
              id="bottom-row-header",
              children=[
                  html.Div(
                     className="column",
                     id="form-bar-container",
                     children=[
                         build_graph_title("Tree Health and Stewardship"),
                         dcc.Graph(id='form-bar-graph'),
                     ]
                     ),
                  html.Div(
                     className="column",
                     id="form-text-container",
                     children=[
                         html.P(
                            id="lower-text-box"                         ),
                     ],
                  ),
              ]
              )
      ]
      )
])




# Running the server
if __name__ == "__main__":
    dash_app.run_server(debug=True)

