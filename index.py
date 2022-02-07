from dash import dcc
from dash import html
from dash import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import aberdeen_city, aberdeenshire, angus, argyll_and_bute, city_of_edinburgh, clackmannanshire, dumfries_and_galloway, dundee_city, east_ayrshire, east_dunbartonshire, east_lothian, east_renfrewshire, falkirk, fife, glasgow_city, highland, inverclyde, midlothian, moray, na_h_eileanan_siar, north_ayrshire, north_lanarkshire, orkney_islands, perth_and_kinross, renfrewshire, scottish_borders, shetland_islands, south_ayrshire, south_lanarkshire, stirling, west_dunbartonshire, west_lothian, summary_page
external_stylesheets=['assets/style.css']

navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),

            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Select a local authority", header=True),
                    dbc.DropdownMenuItem("Aberdeen City", href="/local-authorities/aberdeen-city"),
                    dbc.DropdownMenuItem("Aberdeenshire", href="/local-authorities/aberdeenshire"),
                    dbc.DropdownMenuItem("Angus", href="/local-authorities/angus"),
                    dbc.DropdownMenuItem("Argyll and Bute", href="/local-authorities/argyll-and-bute"),
                    dbc.DropdownMenuItem("City of Edinburgh", href="/local-authorities/city-of-edinburgh"),
                    dbc.DropdownMenuItem("Clackmannanshire", href="/local-authorities/clackmannanshire"),
                    dbc.DropdownMenuItem("Dumfries and Galloway", href="/local-authorities/dumfries-and-galloway"),
                    dbc.DropdownMenuItem("Dundee City", href="/local-authorities/dundee-city"),
                    dbc.DropdownMenuItem("East Ayrshire", href="/local-authorities/east-ayrshire"),
                    dbc.DropdownMenuItem("East Dunbartonshire", href="/local-authorities/east-dunbartonshire"),
                    dbc.DropdownMenuItem("East Lothian", href="/local-authorities/east-lothian"),
                    dbc.DropdownMenuItem("East Renfrewshire", href="/local-authorities/east-renfrewshire"),
                    dbc.DropdownMenuItem("Falkirk", href="/local-authorities/falkirk"),
                    dbc.DropdownMenuItem("Fife", href="/local-authorities/fife"),
                    dbc.DropdownMenuItem("Glasgow City", href="/local-authorities/glasgow-city"),
                ],
                nav=True,
                in_navbar=True,
                label="Local Authorities (A-G)",
            ),

            dbc.DropdownMenu(
                children=[

                    dbc.DropdownMenuItem("Highland", href="/local-authorities/highland"),
                    dbc.DropdownMenuItem("Inverclyde", href="/local-authorities/inverclyde"),
                    dbc.DropdownMenuItem("Midlothian", href="/local-authorities/midlothian"),
                    dbc.DropdownMenuItem("Moray", href="/local-authorities/moray"),
                    dbc.DropdownMenuItem("Na h-Eileanan Siar", href="/local-authorities/na-h-eileanan-siar"),
                    dbc.DropdownMenuItem("North Ayrshire", href="/local-authorities/north-ayrshire"),
                    dbc.DropdownMenuItem("North Lanarkshire", href="/local-authorities/north-lanarkshire"),
                    dbc.DropdownMenuItem("Orkney Islands", href="/local-authorities/orkney-islands"),
                    dbc.DropdownMenuItem("Perth and Kinross", href="/local-authorities/perth-and-kinross"),
                    dbc.DropdownMenuItem("Renfrewshire", href="/local-authorities/renfrewshire"),
                    dbc.DropdownMenuItem("Scottish Borders", href="/local-authorities/scottish-borders"),
                    dbc.DropdownMenuItem("Shetland Islands", href="/local-authorities/shetland-islands"),
                    dbc.DropdownMenuItem("South Ayrshire", href="/local-authorities/south-ayrshire"),
                    dbc.DropdownMenuItem("South Lanarkshire", href="/local-authorities/south-lanarkshire"),
                    dbc.DropdownMenuItem("Stirling", href="/local-authorities/stirling"),
                    dbc.DropdownMenuItem("West Dunbartonshire", href="/local-authorities/west-dunbartonshire"),
                    dbc.DropdownMenuItem("West Lothian", href="/local-authorities/west-lothian"),
                ],
                nav=True,
                in_navbar=True,
                label="Local Authorities (H-Z)",
            ),
        ],
        brand="Scottish Communities",
        brand_href="/",
        color="light",
        sticky="top"
    )

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return summary_page.layout
    elif pathname == '/local-authorities/aberdeen-city':
        return aberdeen_city.layout
    elif pathname == '/local-authorities/aberdeenshire':
        return aberdeenshire.layout
    elif pathname == '/local-authorities/angus':
        return angus.layout
    elif pathname == '/local-authorities/argyll-and-bute':
        return argyll_and_bute.layout
    elif pathname == '/local-authorities/city-of-edinburgh':
        return city_of_edinburgh.layout
    elif pathname == '/local-authorities/clackmannanshire':
        return clackmannanshire.layout
    elif pathname == '/local-authorities/dumfries-and-galloway':
        return dumfries_and_galloway.layout
    elif pathname == '/local-authorities/dundee-city':
        return dundee_city.layout
    elif pathname == '/local-authorities/east-ayrshire':
        return east_ayrshire.layout
    elif pathname == '/local-authorities/east-dunbartonshire':
        return east_dunbartonshire.layout
    elif pathname == '/local-authorities/east-lothian':
        return east_lothian.layout
    elif pathname == '/local-authorities/east-renfrewshire':
        return east_renfrewshire.layout
    elif pathname == '/local-authorities/falkirk':
        return falkirk.layout
    elif pathname == '/local-authorities/fife':
        return fife.layout
    elif pathname == '/local-authorities/glasgow-city':
        return glasgow_city.layout
    elif pathname == '/local-authorities/highland':
        return highland.layout
    elif pathname == '/local-authorities/inverclyde':
        return inverclyde.layout
    elif pathname == '/local-authorities/midlothian':
        return midlothian.layout
    elif pathname == '/local-authorities/moray':
        return moray.layout
    elif pathname == '/local-authorities/na-h-eileanan-siar':
        return na_h_eileanan_siar.layout
    elif pathname == '/local-authorities/north-ayrshire':
        return north_ayrshire.layout
    elif pathname == '/local-authorities/north-lanarkshire':
        return north_lanarkshire.layout
    elif pathname == '/local-authorities/orkney-islands':
        return orkney_islands.layout
    elif pathname == '/local-authorities/perth-and-kinross':
        return perth_and_kinross.layout
    elif pathname == '/local-authorities/renfrewshire':
        return renfrewshire.layout
    elif pathname == '/local-authorities/scottish-borders':
        return scottish_borders.layout
    elif pathname == '/local-authorities/shetland-islands':
        return shetland_islands.layout
    elif pathname == '/local-authorities/south-ayrshire':
        return south_ayrshire.layout
    elif pathname == '/local-authorities/south-lanarkshire':
        return south_lanarkshire.layout
    elif pathname == '/local-authorities/stirling':
        return stirling.layout
    elif pathname == '/local-authorities/west-dunbartonshire':
        return west_dunbartonshire.layout
    elif pathname == '/local-authorities/west-lothian':
        return west_lothian.layout

    else:
        return '404 not found'

if __name__ == '__main__':
    app.run_server(debug=True)