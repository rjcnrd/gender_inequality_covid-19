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
    safety = pd.DataFrame(survey_df.loc[survey_df.safety_level < 3].groupby("area")["safety_level"].count())
    safety = apply_threshold_merge_postcode(safety, "safety_level", postal_code_df, map_threshold)

    safety_change = pd.DataFrame(
        survey_df.loc[survey_df.safety_change == "Worse"].groupby("area")["safety_change"].count())
    safety_change = apply_threshold_merge_postcode(safety_change, "safety_change", postal_code_df, map_threshold)

    mental_health = pd.DataFrame(survey_df.loc[survey_df.mental_scale < 3].groupby("area")["mental_scale"].count())
    mental_health = apply_threshold_merge_postcode(mental_health, "mental_scale", postal_code_df, map_threshold)

    working_situation = pd.DataFrame(
        survey_df.loc[survey_df.work_situation.isin(["No, I have been furloughed because of the lockdown",
                                                     "No, I have been made redundant because of the lockdown",
                                                     "No, I have had to stop working for other reasons related to COVID-19"])].groupby(
            "area")["work_situation"].count())
    working_situation = apply_threshold_merge_postcode(working_situation, "work_situation", postal_code_df,
                                                       map_threshold)

    all_reports = pd.DataFrame(survey_df.groupby("area")["safety_level"].count())
    all_reports = all_reports.rename(columns={"safety_level": "all_reports"})
    all_reports = apply_threshold_merge_postcode(all_reports, "all_reports", postal_code_df, map_threshold)
    all_reports = all_reports.merge(safety[["safety_level", "area"]], left_on="area", right_on="area",
                                    how="left")
    all_reports = all_reports.merge(safety_change[["safety_change", "area"]], left_on="area", right_on="area",
                                    how="left")
    all_reports = all_reports.merge(mental_health[["mental_scale", "area"]], left_on="area", right_on="area",
                                    how="left")
    all_reports = all_reports.merge(working_situation[["work_situation", "area"]], left_on="area",
                                    right_on="area", how="left")
    all_reports.safety_level = all_reports.safety_level.fillna(-1).astype(int).astype(str).replace('-1', np.nan)
    all_reports.safety_change = all_reports.safety_change.fillna(-1).astype(int).astype(str).replace('-1', np.nan)
    all_reports.mental_scale = all_reports.mental_scale.fillna(-1).astype(int).astype(str).replace('-1', np.nan)
    all_reports.work_situation = all_reports.work_situation.fillna(-1).astype(int).astype(str).replace('-1', np.nan)
    all_reports[["safety_level", "safety_change", "mental_scale", "work_situation"]] = all_reports[
        ["safety_level", "safety_change", "mental_scale", "work_situation"]].fillna("0")
    return all_reports, safety, safety_change, mental_health, working_situation


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
    all_reports_uk, safety_uk, safety_change_uk, mental_health_uk, working_situation_uk = data_processing_for_graph(
        uk_data, postal_code_df, map_threshold)

    # Countries postcodes
    internat_data = country_treatment(survey_df, countries_df, postal_code_col=postal_code_col)
    all_reports_internat, safety_internat, safety_change_internat, mental_health_internat, working_situation_internat = data_processing_for_graph(
        internat_data, countries_df, map_threshold)

    # Return the data that is not on the map
    not_in_map = survey_df.drop(index=uk_data.index)
    not_in_map = not_in_map.drop(index=internat_data.index)

    # NOW NEED TO APPEND ONE UNDER THE OTHER
    all_reports = all_reports_uk.append(all_reports_internat)
    safety = safety_uk.append(safety_internat)
    safety_change = safety_change_uk.append(safety_change_internat)
    mental_health = mental_health_uk.append(mental_health_internat)
    working_situation = working_situation_uk.append(working_situation_internat)

    return all_reports, safety, safety_change, mental_health, working_situation, not_in_map, uk_data, uk_data_county
