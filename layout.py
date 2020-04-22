import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd

from overview_tab.overview import create_overview_tab
from statistics_tab.statistics import create_statistics_tab
from testimonials_tab.testimonials import create_testimonials_tab
from urllib.error import URLError

# DATA IN - dummy for now
survey_df = pd.read_csv("data/dummy_data_new.csv",
                        index_col=0)

# DATA Postal Code - in the git for now
postal_code_df = pd.read_csv("data/ukpostcodes.csv")

# Threshold for plotting the data in the graph
map_threshold = 2

def create_layout():
    layout = html.Div(style={
    }, children=[
        html.Div(
    [
        html.H1(html.Span("Domestic Violence",className="section-heading-span"),className="section-heading"),
        html.P(children = [
            html.Span("20%",className="big-numbers"
        ),
            html.P("of women have experienced domestic abuse by their intimate partner in the last 12 month in the uk"),

        html.Span("one in five",className="big-numbers"
        ),
            html.P("families are headed by a single mother. More then two thirds of them are working. They are now unable to work from home as they have to take care of their children with schools closed all over the country.")

        ]),
        # html.Div(
        # dbc.Button(
        #     "Learn more",
        #     id="collapse-button",
        #     className="mb-3",
        #     color="primary"
        # ),
        # style={"text-align":"right"}),
        # dbc.Collapse(
        #     dbc.Container(
        #         create_overview_tab(survey_df, postal_code_df, map_threshold)
        #         ),
        #     id="collapse",
        # ), 
    ]),

     html.Div(
    [
        html.H1(html.Span("Health",className="section-heading-span"),className="section-heading"),
        html.P("Sesame snaps chocolate jujubes. Croissant danish muffin. Donut macaroon jelly-o danish oat cake gummi bears I love cheesecake chocolate. Bonbon dragée topping. Fruitcake cheesecake sugar plum cake marshmallow gingerbread caramels cake. I love sweet roll candy canes cheesecake donut candy canes topping. Carrot cake lollipop candy canes. Fruitcake I love bonbon cake I love pastry I love. Bonbon marzipan I love. Bear claw oat cake tart gingerbread tootsie roll. Liquorice powder soufflé. Icing topping ice cream pie donut oat cake gummies. Pudding oat cake cake I love macaroon."
        ),

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
        html.H1(html.Span("Domestic Work",className="section-heading-span"),className="section-heading"),

        html.P("Sesame snaps chocolate jujubes. Croissant danish muffin. Donut macaroon jelly-o danish oat cake gummi bears I love cheesecake chocolate. Bonbon dragée topping. Fruitcake cheesecake sugar plum cake marshmallow gingerbread caramels cake. I love sweet roll candy canes cheesecake donut candy canes topping. Carrot cake lollipop candy canes. Fruitcake I love bonbon cake I love pastry I love. Bonbon marzipan I love. Bear claw oat cake tart gingerbread tootsie roll. Liquorice powder soufflé. Icing topping ice cream pie donut oat cake gummies. Pudding oat cake cake I love macaroon."
        ),
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
    ],className="DashContent")
    return layout
    