import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


title1 = "89 % of nurses and health visitors are women"
text1 = "and 77% of the entire NHS workforce are women. Women are overrepresented in the UK health workforce working on the front line."
source1="https://digital.nhs.uk/news-and-events/latest-news/narrowing-of-nhs-gender-divide-but-men-still-the-majority-in-senior-roles"

title2= "Women are more likely to have lost their job"
text2=" since the lockdown. 17% of women are employed to work in retail and hospitality, compared to only 13% of men."
source2 = "https://www.ifs.org.uk/publications/14791"

title3 = "Women earn 84 p for £1 earned by a man"
text3 = "based on their weekly salary as recorded in April 2019. With women being on average the party that earns less, more women will be asked to quit their job and take care of children while schools are closed. "
source3 ="https://researchbriefings.files.parliament.uk/documents/SN06838/SN06838.pdf"


def employment_tab():
    children = [
        dbc.Row([
           
              dbc.Col([html.Span(title1, className="big-numbers"
                           ),
                 html.P(
                     [
                         text1,
                         dcc.Link("[NHS]",
                                  href=source1, target='_blank')
                    ]),
                 html.Span(title2, className="big-numbers"
                           ),
                 html.P(
                     [
                         text2,
                         dcc.Link("[IFS]",
                                  href=source2, target='_blank')]),
                 html.Span(title3, className="big-numbers"
                           ),
                 html.P(
                     [
                         text3,
                         dcc.Link("[House of Commons Library]",
                                  href=source3, target='_blank')])
                 ]),  

            dbc.Col([html.Img(src="assets/undraw_medical_care_movn.svg", style={'height': '250px'})],
            style={'textAlign': 'center'},
            md= 4)
        ])
    ]
    return children
