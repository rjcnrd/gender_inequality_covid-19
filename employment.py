import dash_html_components as html
import dash_bootstrap_components as dbc

text1 = "Women are overrepresented in the UK health workforce working on the front line. 77% of the entire NHS workforce are women, and "
text_2_gross = "89 % of nurses and midwives are women. 👩🏽‍⚕️👩🏼‍⚕️👩🏾‍⚕️👩🏼‍⚕️👩🏾‍⚕️👩🏽‍⚕️👩🏼‍⚕️👩🏾‍⚕️👩🏽‍⚕️👨🏻‍⚕️"

lost_job_text = "Women are more likely to have lost their job since the lockdown: 17% of women are employed to work in retail and hospitality, compared to only 13% of men. \n"

earn_less = "Women earn less than men in the UK:" 
earn_less_focus = "Women earned 84 pence for £1 earned by a man"
earn_less_2 = " in April 2019."
money = "💵"

def employment_tab():
    children = [
        dbc.Row([
           
            dbc.Col([
                     html.P([
                         text1,
                         html.Span(text_2_gross, className="big-numbers"),
                         html.Br(),
                        html.Span(money,className="big-numbers"),
                         ]
                        ),

                
                     html.P([
                         
                         lost_job_text,
                         html.Br(),
                         html.Span(money,className="big-numbers"),
                        html.Br(),
                         earn_less,
                         html.Span(earn_less_focus, className="big-numbers"),
                         earn_less_2,

                     ]),
                         

                    ]),
                            

            dbc.Col([html.Img(src="assets/undraw_medical_care_movn.svg", style={'height': '250px'})],
            style={'textAlign': 'center'},
            md= 4)
        ])
    ]
    return children
