import dash_html_components as html
import dash_bootstrap_components as dbc


def domestic_violence_tab():
    children = [
        dbc.Row([
            dbc.Col([]),
            dbc.Col([html.Span("20%", className="big-numbers"
                               ),
                     html.P(
                         "of women have experienced domestic abuse by their intimate partner in the last 12 month in the uk"),

                     html.Span("one in five", className="big-numbers"
                               ),
                     html.P(
                         "families are headed by a single mother. More then two thirds of them are working. They are now unable to work from home as they have to take care of their children with schools closed all over the country.")
                     ])
        ])
    ]
    return children
