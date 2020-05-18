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
        "https://raw.githubusercontent.com/rjcnrd/domestic_violence_covid-19/master/data/data_map_all_reports.csv")
    safety_df = pd.read_csv(
        "https://raw.githubusercontent.com/rjcnrd/domestic_violence_covid-19/master/data/data_map_safety_scale.csv")
    safety_change_df = pd.read_csv(
        "https://raw.githubusercontent.com/rjcnrd/domestic_violence_covid-19/master/data/data_map_safety_change.csv")
    mental_health_df = pd.read_csv(
        "https://raw.githubusercontent.com/rjcnrd/domestic_violence_covid-19/master/data/data_map_mental_health.csv")
    working_situation_df = pd.read_csv(
        "https://raw.githubusercontent.com/rjcnrd/domestic_violence_covid-19/master/data/data_map_working_situation.csv")

    # Text for hover
    all_reports_df["safety_text"] = np.where(all_reports_df["safety_level"] == 0, "",
                                             all_reports_df["safety_level"].map(
                                                 "<br><i>{}</i> report to feel unsafe".format))
    all_reports_df["safety_change_text"] = np.where(all_reports_df["safety_change"] == 0, "",
                                                    all_reports_df["safety_change"].map(
                                                        "<br><i>{}</i> report feeling less safe".format))
    all_reports_df["mental_scale_text"] = np.where(all_reports_df["mental_scale"] == 0, "",
                                                   all_reports_df["mental_scale"].map(
                                                       "<br><i>{}</i> report low mental health".format))
    all_reports_df["work_situation_text"] = np.where(all_reports_df["work_situation"] == 0, "",
                                                     all_reports_df["work_situation"].map(
                                                         "<br><i>{}</i> report that they had to stop working".format))

    # All reports
    fig = go.Figure(
        data=go.Scattermapbox(
            lat=all_reports_df.latitude,
            lon=all_reports_df.longitude,
            mode='markers',
            hovertemplate="<b>%{marker.size:,} reports from %{text}</b>" +
                          "%{customdata[0]}" +
                          "%{customdata[1]}" +
                          "%{customdata[2]}" +
                          "%{customdata[3]}" +
                          "<extra></extra>",
            text=all_reports_df.area_name,
            hoverlabel=dict(bgcolor='#eceded',
                            bordercolor='#eceded',
                            font=dict(color="rgb(68, 68, 68)", size=11)),
            customdata=np.stack((all_reports_df["safety_text"], all_reports_df["safety_change_text"],
                                 all_reports_df["mental_scale_text"], all_reports_df["work_situation_text"]), axis=-1),
            marker=go.scattermapbox.Marker(
                sizeref=big_bubble_size,
                size=all_reports_df.all_reports,
                sizemode="area",
                # size of the dots
                color='#d80052'  # dots are pink
            )))
    # Safety
    fig.add_trace(
        go.Scattermapbox(
            visible=False,
            lat=safety_df.latitude,
            lon=safety_df.longitude,
            mode='markers',
            hovertemplate="<b>%{text}</b><br>" + "%{marker.size:,} report to feel unsafe during the lockdown" + "<extra></extra>",
            text=safety_df.area_name,
            hoverlabel=dict(bgcolor='#eceded',
                            bordercolor='#eceded',
                            font=dict(color="rgb(68, 68, 68)", size=11)),
            marker=go.scattermapbox.Marker(
                sizeref=small_bubble_size,
                size=safety_df.safety_level,
                sizemode="area",
                # size of the dots
                color='red'
            )))

    # Safety Change
    fig.add_trace(
        go.Scattermapbox(
            visible=False,
            lat=safety_change_df.latitude,
            lon=safety_change_df.longitude,
            mode='markers',
            hovertemplate="<b>%{text}</b><br>" + "%{marker.size:,} report to feel less safe during the lockdown" + "<extra></extra>",
            text=safety_change_df.area_name,
            hoverlabel=dict(bgcolor='#eceded',
                            bordercolor='#eceded',
                            font=dict(color="rgb(68, 68, 68)", size=11)),
            marker=go.scattermapbox.Marker(
                sizeref=small_bubble_size,
                size=safety_change_df.safety_change,
                sizemode="area",
                # size of the dots
                color='DarkRed'
            )))

    # Mental Health
    fig.add_trace(
        go.Scattermapbox(
            visible=False,
            lat=mental_health_df.latitude,
            lon=mental_health_df.longitude,
            mode='markers',
            hovertemplate="<b>%{text}</b><br>" + "%{marker.size:,} report to have a low mental health during the lockdown" + "<extra></extra>",
            text=mental_health_df.area_name,
            hoverlabel=dict(bgcolor='#eceded',
                            bordercolor='#eceded',
                            font=dict(color="rgb(68, 68, 68)", size=11)),
            marker=go.scattermapbox.Marker(
                sizeref=small_bubble_size,
                size=mental_health_df.mental_scale,
                sizemode="area",
                # size of the dots
                color='orange'
            )))

    # Working situation
    fig.add_trace(
        go.Scattermapbox(
            visible=False,
            lat=working_situation_df.latitude,
            lon=working_situation_df.longitude,
            mode='markers',
            hovertemplate="<b>%{text}</b><br>" + "%{marker.size:,} report that they had to stop working during the lockdown" + "<extra></extra>",
            text=working_situation_df.area_name,
            hoverlabel=dict(bgcolor='#eceded',
                            bordercolor='#eceded',
                            font=dict(color="rgb(68, 68, 68)", size=11)),
            marker=go.scattermapbox.Marker(
                sizeref=small_bubble_size,
                size=working_situation_df.work_situation,
                sizemode="area",
                # size of the dots
                color='Indigo'
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
                    ),
        updatemenus=[dict(
            xanchor="right",
            x=1,  # place of the menu
            borderwidth=0.1,
            buttons=list([
                dict(label="All reports",
                     method="update",
                     args=[{"visible": [True, False, False, False, False]}]),
                dict(label="Low Safety",
                     method="update",
                     args=[{"visible": [False, True, False, False, False]}]),
                dict(label="Safety Change for Worse",
                     method="update",
                     args=[{"visible": [False, False, True, False, False]}]),
                dict(label="Low Mental Health Rating",
                     method="update",
                     args=[{"visible": [False, False, False, True, False]}]),
                dict(label="Critical Working Situation",
                     method="update",
                     args=[{"visible": [False, False, False, False, True]}])
            ]),
        )])

    return fig
