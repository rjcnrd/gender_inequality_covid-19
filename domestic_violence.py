import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def domestic_violence_tab():
    children = [
        dbc.Row([
            dbc.Col([html.Img(src="assets/undraw_icon_night_calls_domestic_violence.svg", style={'height': '250px'})],
                    style={'textAlign': 'center'},
                    md= 4),
            dbc.Col([html.Span("14 women and 2 children", className="big-numbers"
                               ),
                     html.P(
                         ["have been killed by men in the first three weeks of coronavirus lockdown in the UK, which is double that of a hypothetical average 21 days over the last 10 years. ",
                          dcc.Link("[Counting Dead Women]", href="https://kareningalasmith.com/2020/04/15/coronavirus-doesnt-cause-mens-violence-against-women/")]),


                     html.Span("+25%", className="big-numbers"
                               ),
                     html.P(
                         [
                             "increase in calls and contacts to Refuge National Domestic Abuse Helpline in the two first weeks of the lockdown. Refuge is the UKs largest domestic abuse charity. ",
                             dcc.Link("[Refuge]", href="https://www.refuge.org.uk/25-increase-in-calls-to-national-domestic-abuse-helpline-since-lockdown-measures-began/")
                         ]),
                     html.Span("1.6 Million", className="big-numbers"
                               ),
                     html.P(
                         [
                             "women from 16 to 74 in England and Wales experienced domestic abuse last year. 786,000 men also suffered from it. ",
                             dcc.Link("[ONS]", href="https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice/bulletins/domesticabuseinenglandandwalesoverview/november2019")
                         ])
                     ])
        ])
    ]
    return children
