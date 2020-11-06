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
df = pd.read_csv('data/BBRef_data_clean.csv')

# Category figure label Dictionary
label_dict = {'FG%': 'Percent', '3P%': 'Percent', 'FT%': 'Percent', 'AST': 'Assists',
              'TRB': 'Rebounds', 'STL': 'Steals', 'BLK': 'Blocks', 'TOV': 'Turnovers', 'PTS': 'Points'}

# Picture Formatting
test_png = 'images/bball_pic.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

goals = []

app.layout = html.Div(
    [
        html.Div(className="banner",
                 children=[
                     # Basketball Logo
                     html.Img(src='data:images/ball_hoop.png;base64,{}'.format(test_base64)),

                     html.H2("NBA Player and Team Dashboard", className="header__text",
                             style={"text-align": "center"}),

                     html.Br(),

                     # Team selection header
                     html.H6(children=
                             'Select Year'
                             ),

                     # Team selection dropdown
                     dcc.Dropdown(id='year_input',
                                  options=[
                                      {'label': i, 'value': i} for i in df.year.unique()

                                  ],
                                  value=2020,
                                  style={"display": "block", "width": "50%"}
                                  ),

                     html.Br(),
                     html.Br(),

                 ],

                 ),
        html.Div([
            dcc.Tabs(id="tabs", children=[

                dcc.Tab(label='Player View Dashboard', children=[

                    html.Br(),
                    html.Br(),

                    # Year Dropdown header
                    # Team selection header
                    html.H6(children=
                            'Select Player'
                            ),

                    dcc.Dropdown(id='player_input',
                                 options=[
                                     {'label': i, 'value': i} for i in df.Player.unique()
                                 ],
                                 value='Kemba Walker',
                                 style={"display": "block", "width": "50%"}
                                 ),

                    html.Br(),
                    html.Br(),

                    # Card components
                    # CARD ROW 1
                    dbc.Row([

                        dbc.Col(

                            # FIELD GOAL PERCENTAGE CARD
                            dbc.Card(
                                [
                                    html.H2(id='FieldGoalPercentage_card'),
                                    html.P("Field Goal Percentage", className="card-text"),
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),

                        dbc.Col(

                            # THREE POINT PERCENTAGE CARD
                            dbc.Card(
                                [
                                    html.H2(id='ThreePointPercentage_card'),
                                    html.P("Three Point Percentage", className="card-text")
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),
                        dbc.Col(

                            # FREE THROW PERCENTAGE CARD
                            dbc.Card(
                                [
                                    html.H2(id='FreeThrowPercentage_card'),
                                    html.P("Free Throw Percentage", className="card-text"),
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),
                    ]),

                    html.Br(),

                    # CARD ROW 2
                    dbc.Row([
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H2(id='Rebounds_card'),
                                    html.P("Rebounds Per Game", className="card-text"),
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),

                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H2(id='Assists_card'),
                                    html.P("Assists Per Game", className="card-text")
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H2(id='Steals_card'),
                                    html.P("Steals Per Game", className="card-text"),
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),
                    ]),

                    html.Br(),

                    # CARD ROW 3
                    dbc.Row([
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H2(id='Blocks_card'),
                                    html.P("Blocks Per Game", className="card-text"),
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),

                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H2(id='Turnovers_card'),
                                    html.P("Turnovers Per Game", className="card-text")
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H2(id='Points_card'),
                                    html.P("Points Per Game", className="card-text"),
                                ],
                                body=True,
                                color="success",
                                inverse=True
                            ),
                            width=4
                        ),
                    ]),

                    html.Br(),
                    html.Br(),

                    # HEADER FOR CATEGORIES OVER THE YEARS
                    html.H4(children=
                        'Fantasy Per Game Category Stats (Year to Year)',
                        style={"text-align": "center"}
                    ),


                    # Category selection header
                    html.H6(children=
                            'Category'
                            ),

                    dcc.Dropdown(
                        id='category_input',
                        options=[
                            {'label': 'Field Goal %', 'value': 'FG%'},
                            {'label': 'Three Point %', 'value': '3P%'},
                            {'label': 'Free throw %', 'value': 'FT%'},
                            {'label': 'Rebounds Per Game', 'value': 'TRB'},
                            {'label': 'Assists Per Game', 'value': 'AST'},
                            {'label': 'Steals Per Game', 'value': 'STL'},
                            {'label': 'Blocks Per Game', 'value': 'BLK'},
                            {'label': 'Turnovers Per Game', 'value': 'TOV'},
                            {'label': 'Points Per Game', 'value': 'PTS'}
                        ],
                        value='FG%',
                        style={"display": "block", "width": "50%"}
                    ),


                    dcc.Graph(
                        id='categories-graph'
                    ),

                    dtab.DataTable(
                        id='player_categories_dt',
                        columns=[{"name": 'Year', "id": 'year'},
                                {"name": 'Field Goal %', "id": 'FG%'},
                                {"name": 'Three Point %', "id": '3P%'},
                                {"name": 'Free throw %', "id": 'FT%'},
                                {"name": 'Rebounds Per Game', "id": 'TRB'},
                                {"name": 'Assists Per Game', "id": 'AST'},
                                {"name": 'Steals Per Game', "id": 'STL'},
                                {"name": 'Blocks Per Game', "id": 'BLK'},
                                {"name": 'Turnovers Per Game', "id": 'TOV'},
                                {"name": 'Points Per Game', "id": 'PTS'}],
                        data=[],
                        style_data={
                            'width': '5px',
                            'maxWidth': '10px',
                            'minWidth': '5px'
                        },
                        style_cell={'textAlign': 'left',
                                    'width': '25%',
                                    'textOverflow': 'ellipsis',
                                    'overflow': 'hidden'
                        },
                        style_header={
                        'textAlign': 'center',

                        'fontWeight': 'bold'},
                        style_table= {
                            'width': '95%',
                            'margin-left': '3vw'
                        },
                        css=[{'selector': '.row', 'rule': 'margin: 0'}]
                    ),

                ]),


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
                        'Select team',
                        style={"text-align": "center"}
                    ),

                    dcc.Graph(
                        id='percent-of-cap-graph'
                    ),



                ]),
            ])
        ])
    ], style={'marginLeft': 30, 'marginRight': 30, 'marginTop': 30, 'marginBottom': 30})


# CALLBACK SECTION

# CARDS ROW 1


# Callback for the FIELD GOAL PERCENTAGE
@app.callback(
    # output value for the callback
    Output('FieldGoalPercentage_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):

    df_fgp = df[df['Player'] == player]
    df_fgp = df_fgp[df_fgp['year'] == year]
    fgp = df_fgp['FG%'].tolist()
    fgp = fgp[0]*100

    return ' {0:.2f}% '.format(fgp)

# Callback for the THREE POINT PERCENTAGE
@app.callback(
    # output value for the callback
    Output('ThreePointPercentage_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):

    df_3pp = df[df['Player'] == player]
    df_3pp = df_3pp[df_3pp['year'] == year]
    tpp = df_3pp['3P%'].tolist()
    tpp = tpp[0]*100

    return ' {0:.2f}% '.format(tpp)


# Callback for the FREE THROW PERCENTAGE
@app.callback(
    # output value for the callback
    Output('FreeThrowPercentage_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):

    df_ftp = df[df['Player'] == player]
    df_ftp = df_ftp[df_ftp['year'] == year]
    stat = df_ftp['FT%'].tolist()
    stat = stat[0]*100

    return ' {0:.2f}% '.format(stat)


# CARDS ROW 2

# Callback for the REBOUNDS
@app.callback(
    # output value for the callback
    Output('Rebounds_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):

    df_reb = df[df['Player'] == player]
    df_reb = df_reb[df_reb['year'] == year]
    stat = df_reb['TRB'].tolist()
    stat = stat[0]

    return ' {0:.2f} '.format(stat)

# Callback for the ASSISTS
@app.callback(
    # output value for the callback
    Output('Assists_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):

    df_ast = df[df['Player'] == player]
    df_ast = df_ast[df_ast['year'] == year]
    stat = df_ast['AST'].tolist()
    stat = stat[0]

    return ' {0:.2f} '.format(stat)


# Callback for the STEALS
@app.callback(
    # output value for the callback
    Output('Steals_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):
    df_stl = df[df['Player'] == player]
    df_stl = df_stl[df_stl['year'] == year]
    stat = df_stl['STL'].tolist()
    stat = stat[0]

    return ' {0:.2f} '.format(stat)


# CARDS ROW 3

# Callback for the BLOCKS
@app.callback(
    # output value for the callback
    Output('Blocks_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):
    df_blk = df[df['Player'] == player]
    df_blk = df_blk[df_blk['year'] == year]
    stat = df_blk['BLK'].tolist()
    stat = stat[0]

    return ' {0:.2f} '.format(stat)

# Callback for the TURNOVERS
@app.callback(
    # output value for the callback
    Output('Turnovers_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):
    df_tov = df[df['Player'] == player]
    df_tov = df_tov[df_tov['year'] == year]
    stat = df_tov['TOV'].tolist()
    stat = stat[0]

    return ' {0:.2f} '.format(stat)


# Callback for the POINTS
@app.callback(
    # output value for the callback
    Output('Points_card', 'children'),
    # Inputs
    [Input('player_input', 'value'),
     Input('year_input', 'value')])
def update_fig(player, year):
    df_pts = df[df['Player'] == player]
    df_pts = df_pts[df_pts['year'] == year]
    stat = df_pts['PTS'].tolist()
    stat = stat[0]

    return ' {0:.2f} '.format(stat)



# Callback for the PLAYER CATEGORIES OVER YEARS FIGURE
@app.callback(
    # output value for the callback
    Output('categories-graph', 'figure'),
    # Inputs
    [Input('player_input', 'value'),
     Input('category_input', 'value')])
def update_fig(player, category):

    # filter on player selected
    df_player = df[df['Player'] == player]

    # create figure
    figure_1 = go.Figure(data= go.Scatter( x=df_player['year'], y=df_player[category],
                   name='Player1', line=dict(color='black', width=4)))

    # add Axis labels and formatting
    figure_1.update_xaxes(title_text="Year")
    figure_1.update_yaxes(title_text=label_dict[category])

    return figure_1

# Callback for the PLAYER CATEGORIES DATA TABLE
@app.callback(
    Output('player_categories_dt', 'data'),
    [Input('player_input', 'value')])
def update_table(player):
    # Filter on selected player
    filtered_player_df = df[df['Player'] == player]

    # select columns needed for data table
    player_dt_df = filtered_player_df[['year', 'FG%','3P%', 'FT%', 'TRB', 'AST', 'STL','BLK', 'TOV', 'PTS']]

    return player_dt_df.to_dict(orient='records')





if __name__ == '__main__':
    app.run_server(debug=True)
