import pandas as pd
import plotly.graph_objects as go
import numpy as np

nb_ratings = 6
space_between_rating = 1
space_between_gender = 2


def draw_scatterbarplot(data, num_by_col=5):
    """
    :param num_by_col: The number of points by row in each column of mental health rating. Default value is 5
    :return: the scatterbarplot
    """
    # prepared_data = data_gender_rating(survey_df, include_other=include_other)
    # location_df = location_scatterplot(prepared_data, num_by_col)

    # The data with testimonial
    data_testimonial = data.loc[data.display_testimonial == 1]
    # The data without the testimonial
    data_without_testimonial = data.loc[data.display_testimonial == 0]

    number_gender = len(data.gender.unique())

    # Position of the grading of mental health
    start_position1 = np.median(range(num_by_col))
    start_position2 = (num_by_col + space_between_rating) * nb_ratings + space_between_gender + start_position1
    start_position3 = ((num_by_col + space_between_rating) * nb_ratings + space_between_gender) * 2 + start_position1
    mental_health_position_x = [start_position1 + x * (num_by_col + space_between_rating) for x in
                                range(nb_ratings)] + [start_position2 + x * (num_by_col + space_between_rating) for x in
                                                      range(nb_ratings)]
    if number_gender == 3:
        mental_health_position_x = mental_health_position_x + [start_position3 + x * (num_by_col + space_between_rating)
                                                               for x in range(nb_ratings)]
    mental_health_position_y = [-2] * number_gender * nb_ratings
    mental_health_label = [int(x) for x in list(range(nb_ratings)) * number_gender]

    # Position of the gender label
    gender_position_x = [(num_by_col + 1) * nb_ratings / 2 - 1,
                         (num_by_col + 1) * nb_ratings + space_between_gender + (num_by_col + 1) * nb_ratings / 2 - 1]

    if number_gender == 3:
        gender_position_x = gender_position_x + [
            ((num_by_col + 1) * nb_ratings + space_between_gender) * 2 + (num_by_col + 1) * nb_ratings / 2 - 1]
    gender_position_y = [-5] * 3
    if number_gender == 2:
        gender_text_label = ["Woman", "Man"]
    else:
        gender_text_label = ["Woman", "Other", "Man"]

    # Position of the small lines between the gradings
    small_line_position = [start_position1 + x * (num_by_col + space_between_rating) for x in range(nb_ratings - 1)] + [
        start_position2 + x * (num_by_col + space_between_rating) for x in range(nb_ratings - 1)]
    if number_gender == 3:
        small_line_position = small_line_position + [start_position3 + x * (num_by_col + space_between_rating) for x in
                                                     range(nb_ratings - 1)]
    # Position of the big line between the genders
    big_line_position = [nb_ratings * (num_by_col + 1)]
    if number_gender == 3:
        big_line_position = big_line_position + [nb_ratings * (num_by_col + 1) * 2 + space_between_gender]

    fig = go.Figure()

    # Graph: without the testimonials (no hover, no color)
    fig.add_trace(go.Scatter(x=data_without_testimonial.x,
                             y=data_without_testimonial.y,
                             mode='markers',
                             marker=dict(color="black"),
                             hovertemplate=None,
                             hoverinfo='skip'))

    # Graph: the testimonials (hover, color)
    fig.add_trace(go.Scatter(x=data_testimonial.x,
                             y=data_testimonial.y,
                             mode='markers',
                             marker=dict(color="#FFAECA"),
                             text=data_testimonial.testimonials_short,
                             hovertemplate="%{text}" + "<extra></extra>"))

    # Mental health grade
    fig.add_trace(go.Scatter(
        x=mental_health_position_x,
        y=mental_health_position_y,
        mode="text",
        text=mental_health_label,
        hoverinfo="skip",
        textfont=dict(color="black")
    ))
    # Gender text
    fig.add_trace(go.Scatter(
        x=gender_position_x,
        y=gender_position_y,
        mode="text",
        text=gender_text_label,
        hoverinfo="skip",
        textfont=dict(color="black")
    ))

    # Small line
    for x in small_line_position:
        fig.add_trace(go.Scatter(
            x=[x + np.median(range(num_by_col)) + space_between_rating,
               x + np.median(range(num_by_col)) + space_between_rating],
            y=[0, -3],
            mode="lines", marker=dict(color="black"),
            hoverinfo="skip"
        ))
    # Big Line
    for x in big_line_position:
        fig.add_trace(go.Scatter(
            x=[x, x],
            y=[-3, 4],
            mode="lines",
            marker=dict(color="black"),
            hoverinfo="skip"
        ))

    fig.update_layout(showlegend=False,
                      paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')

    fig.update_xaxes(showticklabels=False, visible=False)
    fig.update_yaxes(showticklabels=False, visible=False, scaleanchor="x", scaleratio=1)
    return fig
