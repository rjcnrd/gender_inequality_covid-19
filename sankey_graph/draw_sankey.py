import pandas as pd
import plotly.graph_objects as go


def sankey_graph(sankey_df):

    living_dim = go.parcats.Dimension(
        values=sankey_df.living_category_var_names,
        categoryorder="category ascending",
        label="I am living with... ",
    )
    household_dim = go.parcats.Dimension(
        values=sankey_df.housework_mapped,
        label="I take care of ...",
        categoryarray=[0, 1, 2],
        ticktext=[
            "all or most<br>of the <br>housework",
            "as much<br>housework<br>as others",
            "less then others <br>or none of  <br>the housework",
        ],
    )

    color = sankey_df.housework_mapped
    colorscale = ["#9F8CF3", "#f2f2f2", "#FFAECA"]

    fig = go.Figure(
        data=[
            go.Parcats(
                dimensions=[living_dim, household_dim],
                line={"color": color, "colorscale": colorscale},
                hoveron="color",
                hovertemplate="%{bandcolorcount} Women" + "<extra></extra>",
            )
        ]
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        height=500,  # height of the graph
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=60, r=60, t=20, b=20),
    )

    return fig
