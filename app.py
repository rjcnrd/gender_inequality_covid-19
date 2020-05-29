# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

from layout import create_layout

from map_graph.draw_map import map_graph
from sankey_graph.draw_sankey import sankey_graph
from housework_piechart.draw_piechart import piechart
from scatter_mental_health.draw_scatter import draw_scatterbarplot

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = [dbc.themes.LUX]

# IMPORT MAP VARIABLES
# Bubble size on the map graph (the bigger the smaller the bubble). Size for the first layer of the map graph (the overview)
big_bubble_size = 0.1

# Bubble size on the map graph (the bigger the smaller the bubble). Size for the other layers of the graph
small_bubble_size = 0.01

# IMPORT DATA
sankey_df = pd.read_csv("https://raw.githubusercontent.com/rjcnrd/gender_inequality_covid-19/master/data/data_sankey_piechart.csv")

map_df = pd.read_csv(
    "https://raw.githubusercontent.com/rjcnrd/gender_inequality_covid-19/master/data/data_map_all_reports.csv")
data_scatter = pd.read_csv("https://raw.githubusercontent.com/rjcnrd/gender_inequality_covid-19/scatter_mental_health/data/data_scatterplot.csv")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
            <div class="app-entry">        
            {%app_entry%}
        </div>
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# app.layout = dbc.Container(
#     create_layout()
#     , className="app-entry")

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    # content will be rendered in this element
    html.Div(id='page-content')
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/":
        return dbc.Container(
            create_layout(map_df, sankey_df, data_scatter)
            , className="app-entry")
    elif pathname == "/map":
        return dcc.Graph(figure=map_graph(map_df, big_bubble_size, small_bubble_size))
    elif pathname == "/sankey":
        return dcc.Graph(figure=sankey_graph(sankey_df))
    elif pathname == "/piechart_housework":
        return dcc.Graph(figure=piechart(sankey_df))
    elif pathname == "/scatter_mental_health":
        return dcc.Graph(figure=draw_scatterbarplot(data_scatter))

    else:
        return html.Div([
            html.H3('You are on page {} which is not created yet'.format(pathname))
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
