from dash import dcc
from dash import html
from dash import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Input, Output
from app import app

font = html.Link(href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap", rel="stylesheet")
external_stylesheets=[dbc.themes.BOOTSTRAP, font]

iz_info = pd.read_csv("data/aberdeenshire/iz_info_aberdeenshire.csv")
iz_info_table = pd.read_csv("data/aberdeenshire/iz_info_dash_table_aberdeenshire.csv")
shs_mao = pd.read_csv("data/aberdeenshire/mao_shs_aberdeenshire.csv")
businesses_decile = pd.read_csv("data/aberdeenshire/businesses_decile_aberdeenshire.csv")
charities_decile = pd.read_csv("data/aberdeenshire/charity_decile_aberdeenshire.csv")
ccch_decile = pd.read_csv("data/aberdeenshire/ccch_decile_aberdeenshire.csv")

iz_info = iz_info.sort_values("Community")
iz_info_wanted_cols = ["Community", "Mean SIMD Decile", "Female life expectancy", "Male life expectancy", "Businesses per 1000 people", "Local charities per 1000 people"]

summary_table = go.Figure(data=[go.Table(
    header=dict(values=iz_info_wanted_cols,
                fill_color='lightgray',
                align='left'),
    cells=dict(values=[iz_info["Community"], iz_info["Mean SIMD Decile"], iz_info["Female life expectancy"], iz_info["Male life expectancy"], iz_info["Businesses per 1000 people"], iz_info["Local charities per 1000 people"]],
               fill_color='#DBF1FC',
               align='left')),  
])


scatter_charities_businesses = px.scatter(
    iz_info,
    x="Businesses per 1000 people",
    y="Local charities per 1000 people",
    labels={"Businesses per 1000 people": "Businesses per 1000 people", "Local charities per 1000 people": "Local charities per 1000 people"},
    width=700,
    height=400,
    title="Number of businesses versus number of charities per 1000 people by intermediate zone",
    hover_data=['Community', "Mean SIMD Decile"],
    color="Mean SIMD Decile",
    color_continuous_scale='agsunset',
)

scatter_charities_cspaces = px.scatter(
    iz_info,
    x="Community spaces per 1000 people",
    y="Local charities per 1000 people",
    labels={"Community spaces per 1000 people": "Number of community spaces per 1000 people", "Local charities per 1000 people": "Local charities per 1000 people"},
    width=700,
    height=400,
    title="Number of community spaces versus number of charities per 1000 people by intermediate zone",
    hover_data=['Community', "Mean SIMD Decile"],
    color="Mean SIMD Decile",
    color_continuous_scale='agsunset',
)

charities = px.bar(
    charities_decile,
    x="Mean SIMD Decile",
    y="Local charities per 1000 people",
    labels={"Mean SIMD Decile": "SIMD Decile intermediate zones (most deprived to least deprived)", "Local charities per 1000 people": "Mean number of local charities per 1000 people"},
    custom_data=['Range'],
    width=700,
    height=400,
)

string = "* Where the value is 0, there are no data points within the Intermediate Zones of that decile, or no Intermediate Zones of that decile.*"
text = f"<i>{string}</i>"

charities.update_layout(margin=dict(t=150))

charities.add_annotation(dict(font=dict(color="black",size=12),
                            x=6,
                            y=1.1,
                            showarrow=False,
                            text=text,
                            textangle=0,
                            xref="x",
                            yref="paper"
                           ))

charities.update_xaxes(range=[0, 11])
charities.update_xaxes(tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

charities.update_traces(
    hovertemplate="<br>".join([
        "SIMD Decile: %{x}",
        "Mean number of charities per 1000 people: %{y}",
        "Range: %{customdata[0]}"
    ])
)


businesses = px.bar(
    businesses_decile,
    x="Mean SIMD Decile",
    y="Businesses per 1000 people",
    labels={"Mean SIMD Decile": "SIMD Decile intermediate zones (most deprived to least deprived)", "Businesses per 1000 people": "Mean number of businesses per 1000 people"},
    custom_data=['Range'],
    width=700,
    height=400,
)

businesses.update_layout(margin=dict(t=150))

businesses.add_annotation(dict(font=dict(color="black",size=12),
                            x=6,
                            y=1.1,
                            showarrow=False,
                            text=text,
                            textangle=0,
                            xref="x",
                            yref="paper"
                           )) 

businesses.update_xaxes(range=[0, 11])
businesses.update_xaxes(tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

businesses.update_traces(
    hovertemplate="<br>".join([
        "SIMD Decile: %{x}",
        "Mean number of businesses per 1000 people: %{y}",
        "Range: %{customdata[0]}"
    ])
)


community = px.bar(
    ccch_decile,
    x="Mean SIMD Decile",
    y="Community spaces per 1000 people",
    labels={"Mean SIMD Decile": "SIMD Decile intermediate zones (most deprived to least deprived)", "Community spaces per 1000 people": "Community spaces per 1000"},
    custom_data=['Range'],
    width=700,
    height=400,
)

community.update_layout(margin=dict(t=150))

community.add_annotation(dict(font=dict(color="black",size=12),
                            x=6,
                            y=1.1,
                            showarrow=False,
                            text=text,
                            textangle=0,
                            xref="x",
                            yref="paper"
                           ))

community.update_traces(
    hovertemplate="<br>".join([
        "SIMD Decile: %{x}",
        "Mean number of community spaces per 1000 people: %{y}",
        "Range: %{customdata[0]}"
    ])
)

community.update_xaxes(range=[0, 11])
community.update_xaxes(tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


map_la = html.Div(
                children=[
                    html.Iframe(
                        src="../assets/aberdeenshire_map.html", 
                        style={"height": "500px", "width": "70%", "margin": "auto"} 
                    )
                ],
                style={"textAlign": "center"}
            )


layout = dbc.Container(
    [
        html.H3("Community Assets in Aberdeenshire"),
        html.Hr(),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H2(f"Mutual aid organisations per 100k people: {shs_mao['MAOs per 100k people'][0]}"),
                        html.H2(f"'I could rely on someone in my neighbourhood to help me' (%): {shs_mao['I could rely on someone in my neighbourhood to help me (%)'][0]}")
                    ], 
                    style={"border": "1px solid black", "textAlign": "center", "padding": "10px"} 
                ),
            ],    
            style={"width": "100%"}
        ),

        dbc.Card(
            [
                dbc.CardHeader(
                    dbc.Tabs(
                        [
                            dbc.Tab(label="Map", tab_id="map"),
                            dbc.Tab(label="Table", tab_id="table"),
                            dbc.Tab(label="Charities", tab_id="charities"),
                            dbc.Tab(label="Businesses", tab_id="businesses"),
                            dbc.Tab(label="Community spaces", tab_id="community"),
                            dbc.Tab(label="Charities/Businesses", tab_id="charities-businesses-scatter"),
                            dbc.Tab(label="Charities/Community spaces", tab_id="charities-cspaces-scatter"),
                        ],
                        id="card-tabs",
                        active_tab="map"
                    )
                ),
                dbc.CardBody(html.Div(id="aberdeenshire-card-content", className="card-text"))
            ]
        ),
    ]
)  
      
@app.callback(
        Output("aberdeenshire-card-content", "children"), 
        [Input("card-tabs", "active_tab")],
    )
def tab_content(active_tab):
    if active_tab:
        if active_tab == "map":
            return map_la
            
        elif active_tab == "table":
            return dcc.Graph(
                id='iz_info_table',
                figure=summary_table,
                config = {'displayModeBar': False}
            )

        elif active_tab == "charities":
            return html.Div(
                children=[
                    dcc.Graph(
                    id='charities',
                    figure=charities,
                    responsive=True,
                    style={"width": "100%", "height": "100%"},
                    config = {'displayModeBar': False}
                    ),
                ],
            ), 

        elif active_tab == "businesses":
            return html.Div(
                children=[
                    dcc.Graph(
                        id='businesses',
                        figure=businesses,
                        responsive=True,
                        style={"width": "100%", "height": "100%"},
                        config = {'displayModeBar': False}
                    ), 
                ], 
            ),

        elif active_tab == "community":
            return html.Div(
                children=[
                    dcc.Graph(
                        id='community',
                        figure=community,
                        responsive=True,
                        style={"width": "100%", "height": "100%"},
                        config = {'displayModeBar': False}
                    ), 
                ], 
            ),

        elif active_tab == "charities-businesses-scatter":
            return html.Div(
                children=[
                    dcc.Graph(
                        id='charities-businesses',
                        figure=scatter_charities_businesses,
                        responsive=True,
                        style={"width": "100%", "height": "100%"},
                        config = {'displayModeBar': False}
                    ),
                ],
            ), 

        elif active_tab == "charities-cspaces-scatter":
            return html.Div(
                children=[
                    dcc.Graph(
                        id='charities-cspaces',
                        figure=scatter_charities_cspaces,
                        responsive=True,
                        style={"width": "100%", "height": "100%"},
                        config = {'displayModeBar': False}
                    ),
                ],
            ),  
                   
        return "no tab selected"