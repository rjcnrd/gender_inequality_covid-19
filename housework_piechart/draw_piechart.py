import pandas as pd
import plotly.graph_objects as go


def create_piechart_df(sankey_df):
    '''
    function takes in sankey_df and returns labels and values
    for pie chart on domestic work
    '''
    labels = ['I am not doing any housework','I do less housework than others', 'We share it equally',
       'I take care of most of the housework','I take care of all the housework']
    
    values = (len(sankey_df[sankey_df.housework_amount == labels[0]]),
    len(sankey_df[sankey_df.housework_amount == labels[1]]),
    len(sankey_df[sankey_df.housework_amount == labels[2]]),
    len(sankey_df[sankey_df.housework_amount == labels[3]]),
    len(sankey_df[sankey_df.housework_amount == labels[4]]) )
    return labels,values

def piechart(sankey_df):
    labels_piechart,values_piechart = create_piechart_df(sankey_df)
    colorscale = ["#e25c8d","#FFAECA","#f2f2f2","#BFB0FF","#9F8CF3"]

    # pull is given as a fraction of the pie radius
    fig = go.Figure(data=[go.Pie(
        labels=labels_piechart, 
        values=values_piechart, 
        pull=[0, 0, 0,0.2, 0.2],
        sort = False,
    )])

    fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend_orientation="h",
            height = 500

        )

    fig.update_traces(textfont_size=10,
                       hoverinfo='skip',
                      marker=dict(colors=colorscale, line=dict(color='black', width=2)))

    return fig 