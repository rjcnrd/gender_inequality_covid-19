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



        dcc.Tabs(className="tabs", children=[

            dcc.Tab(label='OVERVIEW', children=[
                dbc.Container(
                    create_overview_tab(survey_df, postal_code_df, map_threshold))
            ],
                    style=TAB_STYLE,
                    selected_style=SELECTED_STYLE),

            dcc.Tab(label='STATISTICS',
                    children=dbc.Container(create_statistics_tab(survey_df)),
                    style=TAB_STYLE,
                    selected_style=SELECTED_STYLE),

            dcc.Tab(label='TESTIMONIALS',
                    children=[
                        dbc.Container(create_testimonials_tab(survey_df), className="testimonialsFrame")
                    ],
                    style=TAB_STYLE,
                    selected_style=SELECTED_STYLE),
        ])
    ],className="DashContent")
    return layout
    