import plotly.graph_objects as go
import numpy as np

COLORSCALE = ["white", "white", "white", "#d80052", "white"]
FAMILY = "PT Sans"


def add_ranking(df):
    '''
    adds a rank between (1, #of entries / day) to every report
    :param df: df with a column "date_of_report" 
    :returns: a df that has a new column "rankings"
    '''

    df_new = df
    df_new["ranking"] = ""
    starting_point = 0
    for date in df.date_of_report.unique():
        number_of_entries_this_day = len(df_new[df_new.date_of_report == date])
        for i in range(0, number_of_entries_this_day):
            df_new.iloc[starting_point+i, 5] = 1 + i
        starting_point = starting_point + i + 1
    return df_new


def draw_scatterplot_per_day(df):
    df = add_ranking(df)
    figure = go.Figure(data=go.Scatter(
        x=df.date_of_report,
        y=df.ranking,
        hovertemplate="%{text}" +
        "<extra></extra>",
        text=df.written_report,
        hoverlabel=dict(
            bgcolor="#00a0dd"),
        mode='markers',
        marker=dict(
            size=40,
            color=np.random.randn(500),
            colorscale=COLORSCALE,
            opacity=0.5
        )


    ),
        layout=dict(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            color="white",
            showgrid=False),

        yaxis=dict(color="white",
                   showgrid=False)

    )

    )
    return figure
