import pandas as pd
import plotly.graph_objects as go

sankey_df = pd.read_csv("data/sankey.csv")


def sankey_graph():
    subdf = sankey_df

    living_dim = go.parcats.Dimension(
        values=subdf.living_category_var_names,
        categoryorder='category ascending', label="I am living with... "
    )
    household_dim = go.parcats.Dimension(values=subdf.housework_mapped, label="I take care of ...",
                                         categoryarray=[0, 1, 2],
                                         ticktext=['all or most<br>of the <br>housework',
                                                   'as much<br>housework<br>as others',
                                                   'less then others <br>or none of  <br>the housework',
                                                   ])

    color = subdf.housework_mapped
    colorscale = ["#9F8CF3", "#F9C2C2", "#FFAECA"]

    fig = go.Figure(data=[go.Parcats(
        dimensions=[living_dim, household_dim],

        line={'color': color, 'colorscale': colorscale},
        hoveron='color',
        hovertemplate="%{bandcolorcount} Women" +
        '<extra></extra>',
    )])

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        height=500,  # height of the graph
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=60, r=60, t=20, b=20)
    )
    return fig
