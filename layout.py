import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from domestic_violence import domestic_violence_tab, domestic_violence_learn_more
from domestic_work import domestic_work_tab
from employment import employment_tab

from map_graph.draw_map import map_graph
from sankey_graph.draw_sankey import sankey_graph
from housework_piechart.draw_piechart import piechart


# Bubble size on the map graph (the bigger the smaller the bubble). Size for the first layer of the map graph (the overview)
big_bubble_size = 0.1

# Bubble size on the map graph (the bigger the smaller the bubble). Size for the other layers of the graph
small_bubble_size = 0.01


def create_layout(map_df ,sankey_df):
    layout = html.Div(style={
    }, children=[
        html.Div(
            [
                html.H1(html.Span("From where we collected your voices", className="section-heading-span"), className="section-heading"),
                dcc.Link("[Open chart in seperate tab]", href="/map", target='_blank'),

                html.Div(children=[
                    html.Div(children=[
                        dcc.Graph(figure=map_graph(map_df,big_bubble_size, small_bubble_size))])

                ])
            ]),

          html.Div(
            [
                html.H1(html.Span("Women's share of domestic work", className="section-heading-span"), className="section-heading"),
                dcc.Link("[Open chart in seperate tab]",
                                      href="/sankey", target='_blank'),
                html.Div(children=[
                    html.Div(children=[
                        dcc.Graph(figure=sankey_graph(sankey_df))])

                ])
            ]),

            html.Div(
            [
                html.H1(html.Span("Women's share of domestic work (simplified)", className="section-heading-span"), className="section-heading"),
                dcc.Link("[Open chart in seperate tab]",
                        href="/piechart_housework", target='_blank'),
                html.Div(children=[
                    html.Div(children=[
                        dcc.Graph(figure=piechart(sankey_df))])

                ])
            ]),

        



        html.Div(
            [
                html.H1(html.Span("Domestic Violence", className="section-heading-span"), className="section-heading"),
                dbc.Container(domestic_violence_tab()),
                html.Div(
                    style={"text-align": "right"}),
                dbc.Collapse(
                    dbc.Container(
                        domestic_violence_learn_more()
                    ),
                    id="collapse",
                ),
            ]),

        html.Div(
            [

                html.H1(html.Span("Employment", className="section-heading-span"), className="section-heading"),
                 dbc.Container(employment_tab()),

        
            ]),

        html.Div(
            [
                html.H1(html.Span("Domestic Work", className="section-heading-span"), className="section-heading"),

                dbc.Container(domestic_work_tab()),
               
            ])
    ], className="DashContent")
    return layout
