# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import dash_core_components as dcc
import dash_html_components as html

from layout import create_layout

from map_graph.draw_map import map_graph

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = [dbc.themes.LUX]


#IMPORT MAP VARIABLES
# Bubble size on the map graph (the bigger the smaller the bubble). Size for the first layer of the map graph (the overview)
big_bubble_size = 0.1

# Bubble size on the map graph (the bigger the smaller the bubble). Size for the other layers of the graph
small_bubble_size = 0.01

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
                create_layout()
                , className="app-entry")
    elif pathname == "/map":
        return dcc.Graph(figure=map_graph(big_bubble_size, small_bubble_size))

    else:
        return html.Div([
            html.H3('You are on page {} which is not created yet'.format(pathname))
        ])


if __name__ == '__main__':
    app.run_server(debug=True)



