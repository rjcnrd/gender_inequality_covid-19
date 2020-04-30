import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def domestic_work_tab():
    children = dbc.Row([
        dbc.Col([html.Img(src="assets/undraw_icon_children.svg", style={'height': '250px'})],
                style={'textAlign': 'center'},
                md=4),
        dbc.Col([html.Span("13 Million children", className="big-numbers"
                           ),
                 html.P(
                     [
                         "from PrePrimary to Secondary School are impacted by school closure in the UK, moving the work of caring for children from the paid economy—nurseries, schools, babysitters—to the unpaid one. ",
                         dcc.Link("[UNESCO]",
                                  href="https://en.unesco.org/covid19/educationresponse", target='_blank')]),
                 html.Span("2.9 Million Families", className="big-numbers"
                           ),
                 html.P(
                     [
                         "are headed by a single parent, 87 percent of whom are women. ",
                         dcc.Link("[ONS]",
                                  href="https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/families/bulletins/familiesandhouseholds/2019", target='_blank')]),
                 html.Span("+60%", className="big-numbers"
                           ),
                 html.P(
                     [
                         "unpaid work is carried by women compared to men. On average men do 16 hours a week of such unpaid work, which includes adult care and child care, laundry and cleaning, to the 26 hours of unpaid work done by women a week. ",
                         dcc.Link("[ONS]",
                                  href="https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/articles/womenshouldertheresponsibilityofunpaidwork/2016-11-10", target='_blank')])
                 ])])

    return children
