import dash_html_components as html
import dash_bootstrap_components as dbc

string = "Sesame snaps chocolate jujubes. Croissant danish muffin. Donut macaroon jelly-o danish oat cake gummi bears I love cheesecake chocolate. Bonbon dragée topping. Fruitcake cheesecake sugar plum cake marshmallow gingerbread caramels cake. I love sweet roll candy canes cheesecake donut candy canes topping. Carrot cake lollipop candy canes. Fruitcake I love bonbon cake I love pastry I love. Bonbon marzipan I love. Bear claw oat cake tart gingerbread tootsie roll. Liquorice powder soufflé. Icing topping ice cream pie donut oat cake gummies. Pudding oat cake cake I love macaroon."


def domestic_work_tab():
    children = dbc.Row([
        dbc.Col([html.Img(src="assets/undraw_icon_children.svg", style={'height': '250px'})],
                    style={'textAlign': 'center'},
                    md=4),
        dbc.Col([string])])

    return children
