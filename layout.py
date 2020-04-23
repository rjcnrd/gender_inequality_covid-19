import dash_html_components as html
import dash_bootstrap_components as dbc

from domestic_violence import domestic_violence_tab, domestic_violence_learn_more
from domestic_work import domestic_work_tab
from employment import employment_tab


def create_layout():
    layout = html.Div(style={
    }, children=[
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
                html.H1(html.Span("Health", className="section-heading-span"), className="section-heading"),
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
