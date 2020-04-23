import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def domestic_work_tab():
    children = dbc.Row([
        dbc.Col([html.Img(src="assets/undraw_icon_children.svg", style={'height': '250px'})],
                style={'textAlign': 'center'},
                md=4),
        dbc.Col([html.Span("13M children", className="big-numbers"
                           ),
                 html.P(
                     [
                         "from PrePrimary to Secondary School are impacted by school closure in the UK, moving the work of caring for children from the paid economy—nurseries, schools, babysitters—to the unpaid one. ",
                         dcc.Link("[UNESCO]",
                                  href="https://en.unesco.org/covid19/educationresponse")]),
                 html.Span("2.9 Million", className="big-numbers"
                           ),
                 html.P(
                     [
                         "families are headed by a single parent, 87 percent of whom are women. ",
                         dcc.Link("[ONS]",
                                  href="https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/families/bulletins/familiesandhouseholds/2019")])
                 ])])

    return children
