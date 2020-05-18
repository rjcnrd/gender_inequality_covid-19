import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from domestic_violence import domestic_violence_tab, domestic_violence_learn_more
from domestic_work import domestic_work_tab
from employment import employment_tab
from map_graph.draw_map import map_graph


# Bubble size on the map graph (the bigger the smaller the bubble). Size for the first layer of the map graph (the overview)
big_bubble_size = 0.1

# Bubble size on the map graph (the bigger the smaller the bubble). Size for the other layers of the graph
small_bubble_size = 0.01


def create_layout():
    layout = html.Div(style={
    }, children=[
        html.Div(
            [
                html.H1(html.Span("How are you feeling", className="section-heading-span"), className="section-heading"),
                html.Div(children=[
                    html.Div(children=[
                        dcc.Graph(figure=map_graph(big_bubble_size, small_bubble_size))])

                ])
            ]),
        html.Div(
            [
                html.H1(html.Span("Domestic Violence", className="section-heading-span"), className="section-heading"),
                dbc.Container(domestic_violence_tab()),
                html.Div(
                    dbc.Button(
                        "Learn more",
                        id="collapse-button",
                        className="mb-3",
                        color="primary"
                    ),
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

                # html.Div(
                #     dbc.Button(
                #         "Learn more",
                #         id="collapse-button-2",
                #         className="mb-3",
                #         color="primary",
                #     ),
                #     style={"text-align":"right"}),
                # dbc.Collapse(
                #     dbc.Container(
                #             create_statistics_tab(survey_df)
                #                 ),
                #     id="collapse-2",
                # ),
            ]),

        html.Div(
            [
                html.H1(html.Span("Domestic Work", className="section-heading-span"), className="section-heading"),

                dbc.Container(domestic_work_tab()),
                #    html.Div(
                #     dbc.Button(
                #         "Learn more",
                #         id="collapse-button-3",
                #         className="mb-3",
                #         color="primary",
                #     )
                #    ,
                #     style={"text-align":"right"}),

                #     dbc.Collapse(
                #         dbc.Container(

                #             create_testimonials_tab(survey_df)

                #             ),
                #         id="collapse-3",
                #     ),
            ])
    ], className="DashContent")
    return layout
