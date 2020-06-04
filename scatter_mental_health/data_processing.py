import pandas as pd
import numpy as np
import textwrap

nb_ratings = 6
space_between_rating = 1
space_between_gender = 2


def data_gender_rating(survey_df, do_percentage=True, mental_health_col="mental_scale", include_other=True,
                       include_man=True):
    """
    :param mental_health_col: name of the mental health column
    :param do_percentage: do a percentage. If false : does the absolute number
    :param include_man: include "man"
    :param include_other: Include "other" gender
    :param survey_df: the survey data. We need the columns gender and mental_health
    :return: a pandas data frame, with 2 indexes : first the gender ("Man", "Woman", "Other", then the mental health grading (from 0 to 5).
    One column "percentage" with the the percentage of people in each mental health category, by gender
    """
    df = pd.DataFrame(survey_df.groupby(["gender", mental_health_col])["age"].count())
    # drop the people that dont answer about the gender
    df = df.drop(0)
    if do_percentage:
        df = df / pd.DataFrame(survey_df.groupby(["gender"])["age"].count())
        df = df.rename(columns={"age": "percentage"})
        df["percentage"] = df["percentage"].round(2) * 100
    else:
        df = df.rename(columns={"age": "number"})
    if not include_other:
        df = df.drop("Non-binary / other")
    if not include_man:
        df = df.drop("Man")
    return df


def location_scatterplot(survey_df, num_by_col=5, include_other=True, include_man=True, do_percentage=True):
    """
    :param do_percentage:
    :param include_man:
    :param include_other:
    :param survey_df:
    :param num_by_col: The number of points by row in each column of mental health rating. Default value is 5
    :return: The location (x,y) for all the points in the graph
    """
    percentage_cat = data_gender_rating(survey_df, include_other=include_other, include_man=include_man,
                                        do_percentage=do_percentage)
    # Columns of our new data frame
    columns = ["gender", "mental_health", "order", "x", "y"]
    # Number of genders
    number_gender = len(percentage_cat.groupby(level=0))
    # The order of genders in the scatter plot
    if number_gender == 3:
        order = {"Woman": 0, "Non-binary / other": 1, "Man": 2}
    elif number_gender == 2:
        order = {"Woman": 0, "Man": 1}
    else:
        order = {"Woman": 0}
    # Create an empty dataframe
    point_location = pd.DataFrame(columns=columns)
    for index, percentage in percentage_cat.iterrows():
        for number in range(int(percentage.values)):
            y_location = number // num_by_col
            x_location = number % num_by_col
            point_location = point_location.append({"gender": index[0],
                                                    "mental_health": index[1],
                                                    "order": order[index[0]],
                                                    "x": x_location,
                                                    "y": y_location}, ignore_index=True)
    # The place in the mental health column + Adding a shift for the mental health + Adding a shift for the gender
    point_location["x"] = point_location["x"] + point_location["mental_health"] * (num_by_col + space_between_rating) + \
                          point_location["order"] * (
                                  (num_by_col + space_between_rating) * nb_ratings + space_between_gender)
    return point_location


def testimonial_treatment(testimonial_df, maximum_total_length, maximum_line_length, minimum_total_length):
    """
    :param testimonial_df: the testimonial data in the other of appearance. Columns should be "gender", "mental_scale","testimonial"
    :param maximum_total_length: Maximum length of testimonial
    :param maximum_line_length: Maximum length of the line on hover
    :param minimum_total_length: Minimum length of testimonial
    :return: the testimonial data with column "testimonials_short", "display_testimonial"
    """
    testimonials_short = []
    for text in testimonial_df["selected_testimonial"]:
        if isinstance(text, int):
            testimonials_short.append(0)
        elif len(text) < minimum_total_length:
            testimonials_short.append(0)
        else:
            if maximum_total_length is not None:
                text = textwrap.shorten(text, width=maximum_total_length)
            # ADDING BREAKS FOR HOVER PLOT !
            text_shortened_wrapped = "<br>".join(textwrap.wrap(text, width=maximum_line_length))
            testimonials_short.append(text_shortened_wrapped)
    testimonial_df["testimonials_short"] = testimonials_short
    testimonial_df["display_testimonial"] = np.where(testimonial_df["testimonials_short"] == 0, 0, 1)
    return testimonial_df


def merge_testimonials(location_data, testimonial_data, include_other=True, include_man = True):
    """
    :param location_data: the result of the function location scatter plot
    :param testimonial_data: the testimonial data in the other of appearance. Columns should be "gender", "mental_scale","testimonial", "testimonials_short", "display_testimonial"
    :param include_other: should it include the gender "other"
    :return: df with 7 columns : result of the location data + column "testimonial", "display_testimonial"
    """
    if not include_other:
        testimonial_data = testimonial_data.loc[testimonial_data.gender != 0]
    if not include_man:
        testimonial_data = testimonial_data.loc[testimonial_data.gender != "Man"]
    testimonial_data = testimonial_data.sort_values(["gender", "mental_scale"]).reset_index(drop=True)
    data = location_data.merge(testimonial_data[["testimonials_short", "display_testimonial"]], right_index=True,
                               left_index=True)
    return data
