import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dtab
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import base64
import plotly.graph_objects as go

app = dash.Dash(external_stylesheets=[dbc.themes.LITERA])

# read in data
# df = pd.read_csv()

test_png = 'images/ball_hoop.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

goals = []

app.layout = html.Div(
    [
        html.Div(className="banner",
                 children=[
                     # Basketball Logo
                     html.Img(src='data:images/ball_hoop.png;base64,{}'.format(test_base64)),

                     html.H2("Player and Team Dashboard", className="header__text",
                             style={"text-align": "center"}),

                     html.Br(),
                 ],

                 ),
        html.Div(
            [
                dcc.Tabs(id="tabs", children=[

                    dcc.Tab(label='Dashboard Overview', children=[

                    ]
                            ),
                    dcc.Tab(label='Team Dashboard', children=[

                        html.Br(),

                        html.Br(),

                        # Year Dropdown header
                        html.H4(
                            children=
                            'Select Year',
                            style={"text-align": "center"}
                        ),

                        html.Br(),

                        # Team Dropdown header
                        html.H4(
                            children=
                            'Select Year',
                            style={"text-align": "center"}
                        ),

                        dcc.Graph(
                            id='registered-user-graph'
                        ),

                    ]
                            ),
                    dcc.Tab(label='Player Dashboard', children=[

                    ]
                            )
                ]
                         )
            ])
    ], style={'marginLeft': 30, 'marginRight': 30, 'marginTop': 30})

if __name__ == '__main__':
    app.run_server(debug=True)
