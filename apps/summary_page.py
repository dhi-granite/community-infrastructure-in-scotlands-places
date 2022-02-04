from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import dash_bootstrap_components as dbc

font = html.Link(href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap", rel="stylesheet")
external_stylesheets=[dbc.themes.BOOTSTRAP, font]

la_info = pd.read_csv("data/scotland/la_info.csv")
la_info.rename(columns={"SIMD decile": "Mean SIMD decile", "MAOs per 100k people": "Mutual aid organisations per 100k people"}, inplace=True)

la_info_wanted_cols = ["Local authority", "Mean SIMD decile", "Businesses per 1000 people", "Charities per 1000 people", "Community spaces per 1000 people", "Mutual aid organisations per 100k people", "Development trusts per 100k people"]
la_info_cols = la_info.columns

la_info_table = go.Figure(data=[go.Table(
    header=dict(values=la_info_wanted_cols,
                fill_color='lightgray',
                align='left'),
    cells=dict(values=[la_info["Local authority"], la_info["Mean SIMD decile"], la_info["Businesses per 1000 people"], la_info["Charities per 1000 people"], la_info["Community spaces per 1000 people"], la_info["Mutual aid organisations per 100k people"], la_info["Development trusts per 100k people"]],
               fill_color='#DBF1FC',
               align='left'))
])

layout = dbc.Container(

    [
        html.H3("Scottish Communities - Community Infrastructure"),
        html.Hr(),
        html.Div(
            children=[
                html.Div(
                    children=[
                       dcc.Graph(
                            id='la_info_table',
                            figure=la_info_table,
                            config = {'displayModeBar': False}
                        )
                    ],    
                style={"width": "100%", "height": "100%"}
                )
            ]
        )
    ]
)  