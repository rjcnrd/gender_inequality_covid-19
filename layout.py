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

# TAB STYLE IS EQUAL  to H3 in default style
TAB_STYLE = {
    'background': '#00a0dd',
    'color': 'white',
    'border': 'none',
    'border-top': 'none',
    'font-family':'BUKA',
    'font-size': '6rem',
    'text-transform': 'uppercase',
    'letter-spacing': ' 3px',
    'margin-top': '0',
    'margin-bottom': '0.5rem',
    'font-weight': '600',
    'line-height': '1.2',
}

SELECTED_STYLE = {
    'background': '#00a0dd',
    'color': '#d80052',
    'border-top': 'none',
    'border': 'none',
      'font-family':'BUKA',
    'font-size': '6rem',
    'text-transform': 'uppercase',
    'letter-spacing': ' 3px',
    'margin-top': '0',
    'margin-bottom': '0.5rem',
    'font-weight': '600',
    'line-height': '1.2',
}


def create_layout():
    layout = html.Div(style={
    }, children=[
        html.Div(
    [
        html.H1(html.Span("Domestic Abuse",className="graph-heading-span"),className="graph-heading"),
        html.P("Sesame snaps chocolate jujubes. Croissant danish muffin. Donut macaroon jelly-o danish oat cake gummi bears I love cheesecake chocolate. Bonbon dragée topping. Fruitcake cheesecake sugar plum cake marshmallow gingerbread caramels cake. I love sweet roll candy canes cheesecake donut candy canes topping. Carrot cake lollipop candy canes. Fruitcake I love bonbon cake I love pastry I love. Bonbon marzipan I love. Bear claw oat cake tart gingerbread tootsie roll. Liquorice powder soufflé. Icing topping ice cream pie donut oat cake gummies. Pudding oat cake cake I love macaroon."
        ),
        dbc.Button(
            "Learn more",
            id="collapse-button",
            className="mb-3",
            color="primary",
        ),
        dbc.Collapse(
            dbc.Container(

                create_overview_tab(survey_df, postal_code_df, map_threshold)
                
                ),
            id="collapse",
        ),
    ]),

     html.Div(
    [
        html.H1(html.Span("Health",className="graph-heading-span"),className="graph-heading"),
        html.P("Sesame snaps chocolate jujubes. Croissant danish muffin. Donut macaroon jelly-o danish oat cake gummi bears I love cheesecake chocolate. Bonbon dragée topping. Fruitcake cheesecake sugar plum cake marshmallow gingerbread caramels cake. I love sweet roll candy canes cheesecake donut candy canes topping. Carrot cake lollipop candy canes. Fruitcake I love bonbon cake I love pastry I love. Bonbon marzipan I love. Bear claw oat cake tart gingerbread tootsie roll. Liquorice powder soufflé. Icing topping ice cream pie donut oat cake gummies. Pudding oat cake cake I love macaroon."
        ),
        dbc.Button(
            "Learn more",
            id="collapse-button-2",
            className="mb-3",
            color="primary",
        ),
        dbc.Collapse(
            dbc.Container(

                create_statistics_tab(survey_df)
                
                ),
            id="collapse-2",
        ),
    ]),

    html.Div(
    [
        html.H1(html.Span("Domestic Work",className="graph-heading-span"),className="graph-heading"),

        html.P("Sesame snaps chocolate jujubes. Croissant danish muffin. Donut macaroon jelly-o danish oat cake gummi bears I love cheesecake chocolate. Bonbon dragée topping. Fruitcake cheesecake sugar plum cake marshmallow gingerbread caramels cake. I love sweet roll candy canes cheesecake donut candy canes topping. Carrot cake lollipop candy canes. Fruitcake I love bonbon cake I love pastry I love. Bonbon marzipan I love. Bear claw oat cake tart gingerbread tootsie roll. Liquorice powder soufflé. Icing topping ice cream pie donut oat cake gummies. Pudding oat cake cake I love macaroon."
        ),
        dbc.Button(
            "Learn more",
            id="collapse-button-3",
            className="mb-3",
            color="primary",
        ),
        dbc.Collapse(
            dbc.Container(

                create_testimonials_tab(survey_df)
                
                ),
            id="collapse-3",
        ),
    ]),

      html.Div(
    [
        html.H1(html.Span("Representation in Politics",className="graph-heading-span"),className="graph-heading"),
        html.P("Sesame snaps chocolate jujubes. Croissant danish muffin. Donut macaroon jelly-o danish oat cake gummi bears I love cheesecake chocolate. Bonbon dragée topping. Fruitcake cheesecake sugar plum cake marshmallow gingerbread caramels cake. I love sweet roll candy canes cheesecake donut candy canes topping. Carrot cake lollipop candy canes. Fruitcake I love bonbon cake I love pastry I love. Bonbon marzipan I love. Bear claw oat cake tart gingerbread tootsie roll. Liquorice powder soufflé. Icing topping ice cream pie donut oat cake gummies. Pudding oat cake cake I love macaroon."
        ),
        dbc.Button(
            "Learn more",
            id="collapse-button-4",
            className="mb-3",
            color="primary",
        ),
        dbc.Collapse(
            dbc.Container(

                create_testimonials_tab(survey_df)
                
                ),
            id="collapse-4",
        ),
    ]),
    ],className="DashContent")
    return layout
    