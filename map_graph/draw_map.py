import pandas as pd
import os
import plotly.graph_objects as go
import numpy as np
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MAPBOX_STYLE_URL = os.getenv("MAPBOX_STYLE_URL")
FAMILY = "PT Sans"


def map_graph(big_bubble_size=2, small_bubble_size=0.01):
    """
    :param big_bubble_size: size of the reference bubble in the map. For the first layer. The bigger the bubble_size, the smaller the bubble
    :param small_bubble_size: size of the reference bubble in the map. For the other layer. The bigger the bubble_size, the smaller the bubble
    :return: map of UK with the number of aggressions
    """
    # all_reports_df, safety_df, safety_change_df, mental_health_df, working_situation_df = merge_local_internat_dataframe(
    # survey_df, postal_code_df, countries_df, map_threshold)
    all_reports_df = pd.read_csv(
        "https://raw.githubusercontent.com/rjcnrd/gender_inequality_covid-19/master/data/data_map_all_reports.csv")

    # Text for hover
    all_reports_df["overall_text"] = np.where(all_reports_df["all_reports"] == 1,
                                              all_reports_df["all_reports"].map("<b>{} report from ".format) +
                                              all_reports_df["area_name"].map("{} </b>".format),
                                              all_reports_df["all_reports"].map("<b>{} reports from ".format) +
                                              all_reports_df["area_name"].map("{} </b>".format))

    # All reports
    fig = go.Figure(
        data=go.Scattermapbox(
            lat=all_reports_df.latitude,
            lon=all_reports_df.longitude,
            mode='markers',
            hovertemplate="%{text}" +
                          "<extra></extra>",
            hoverlabel=dict(bgcolor='#eceded',
                            bordercolor='#eceded',
                            font=dict(color="rgb(68, 68, 68)", size=11)),
            text=all_reports_df["overall_text"],
            marker=go.scattermapbox.Marker(
                sizeref=big_bubble_size,
                size=all_reports_df.all_reports,
                sizemode="area",
                # size of the dots
                color='#d80052'  # dots are pink
            )))

    fig.update_layout(  # mapbox_style="carto-positron",  # Chooses the type of map in the background
        paper_bgcolor='rgba(0,0,0,0)',
        height=580,  # height of the graph
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=30, t=20, b=20),
        mapbox=dict(accesstoken=MAPBOX_TOKEN,
                    style=MAPBOX_STYLE_URL,
                    center=go.layout.mapbox.Center(lat=54.237933, lon=-2.36967),
                    zoom=4.5  # add a zoom of size of great britain
                    ))

    return fig
