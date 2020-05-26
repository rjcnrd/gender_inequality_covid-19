import pandas as pd
import numpy as np
import warnings


warnings.filterwarnings("ignore", 'This pattern has match groups')
pd.options.mode.chained_assignment = None  # default='warn'


def postal_code_treatment(survey_data, postal_code_col="postal_code"):
    """
    :param survey_data: survey data
    :param postal_code_col: the name of the postal code column in the survey data
    :return: the survey data frame with the rows that start with a letter and contain a number. + Append to this data frame a column with the 2 first letters of the postal code : this is the name of the area and will be used in the join with the postal code data frame.
    """
    # Deletes the spacing at the beginning
    survey_data[postal_code_col] = survey_data[postal_code_col].str.lstrip()
    survey_data[postal_code_col] = survey_data[postal_code_col].str.upper()

    # Start with a letter and Contains a number
    data_to_display = survey_data.loc[survey_data[postal_code_col].str.contains('(^[A-Z])(.*\d+)', na=False)]
    data_to_display["area"] = data_to_display[postal_code_col].str.extract('^(\D*)')
    data_to_display["area"] = data_to_display["area"].str.rstrip()
    return data_to_display


def country_treatment(survey_data, countries_df, postal_code_col="postal_code"):
    """
    :param survey_data: survey data
    :param countries_df: latitude and longitude of the international countries
    :param postal_code_col: the name of the postal code column in the survey data
    :return: the survey data frame with the rows where the postal code is simply the name of the country (with or without spacing). + Append to this data frame a column the name of the country : this is the name of the area and will be used in the join with the country data frame
    """
    # Deletes the spacing at the beginning
    survey_data.loc[:, postal_code_col] = survey_data.loc[:, postal_code_col].str.lstrip()
    survey_data.loc[:, postal_code_col] = survey_data.loc[:, postal_code_col].str.upper()
    survey_data.loc[:, postal_code_col] = survey_data.loc[:, postal_code_col].str.lstrip()

    # Start with a letter and Contains a number
    data_to_display = survey_data.loc[survey_data.loc[:, postal_code_col].isin(countries_df.country_name)]
    data_to_display = data_to_display.reset_index().merge(countries_df[["area", "country_name"]], how="left",
                                                          right_on="country_name", left_on=postal_code_col).drop(
        columns=["country_name"]).set_index('index')
    return data_to_display


def apply_threshold_merge_postcode(survey_df, column, postal_code_df, map_threshold):
    """
    :param survey_df: survey data. Using the postal code
    :param column: the column on which to do the filtering
    :param postal_code_df: data frame that includes the postal codes, the latitude and the longitude
    :param map_threshold: a number giving the threshold after which we can plot a marker on the map
    :return: a data frame with a filter on the threshold and a merge with postal code
    """
    df = survey_df[survey_df[column] > map_threshold]
    df = df.merge(postal_code_df, left_index=True, right_on="area", how="left")
    return df


def data_processing_for_graph(survey_df, postal_code_df, map_threshold):
    """
    :param survey_df: data from the survey
    :param map_threshold: a number giving the threshold after which we can plot a marker on the map
    :param postal_code_df: data frame that includes the postal codes, the latitude and the longitude
    :return: 5 dataframe with one row per postal code as index, with latitude, longitude and number of incidents
    """

    all_reports = pd.DataFrame(survey_df.groupby("area")["safety_level"].count())
    all_reports = all_reports.rename(columns={"safety_level": "all_reports"})
    all_reports = apply_threshold_merge_postcode(all_reports, "all_reports", postal_code_df, map_threshold)

    return all_reports


def merge_local_internat_dataframe(survey_df, postal_code_df, countries_df, postal_code_col, map_threshold):
    """
    :param postal_code_col: string with the name of the postal code column
    :param countries_df: latitude and longitude of the international countries
    :param map_threshold: a number giving the threshold after which we can plot a marker on the map
    :param survey_df: dummy data
    :param postal_code_df: postal code data frame
    :return: merge the output of the data_processing_for_graph for UK postcodes and for the international. Output is given to the map function + Returns the data that is not in the data frame
    """
    # UK postcodes
    uk_data = postal_code_treatment(survey_df, postal_code_col=postal_code_col)

    # Include the ones that provide directly the name of the county
    postal_code_df["upper"] = postal_code_df["area_name"].str.upper()
    uk_data_county = survey_df.reset_index().merge(postal_code_df, left_on="location", right_on="upper").drop(
        columns=["area_name", "latitude", "longitude", "upper"]).set_index('index')
    uk_data = uk_data.append(uk_data_county)

    # Do the processing for the UK data
    all_reports_uk = data_processing_for_graph(uk_data, postal_code_df, map_threshold)

    # Countries postcodes
    internat_data = country_treatment(survey_df, countries_df, postal_code_col=postal_code_col)
    all_reports_internat= data_processing_for_graph(internat_data, countries_df, map_threshold)

    # Return the data that is not on the map
    not_in_map = survey_df.drop(index=uk_data.index)
    not_in_map = not_in_map.drop(index=internat_data.index)

    # NOW NEED TO APPEND ONE UNDER THE OTHER
    all_reports = all_reports_uk.append(all_reports_internat)

    return all_reports, not_in_map, uk_data, uk_data_county
