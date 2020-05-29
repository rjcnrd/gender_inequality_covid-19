import pandas as pd 

LIVING_CATEGORY_NAMES = {
    "0": "Other",
    "siblings_parent_other_family": "with other <br>family members",
    "friends_only": "with friends",
    "live_with_partner_only": "with my partner",
    "live_with_partner_and_children_only": "with <br>my partner<br>and children",
    "live_with_children_only": "alone with<br>my children",
}


def map_living_categories(df):
    """
    :param df: survey data of women not living alone 
    :return: a list of lists, the columns corresponding to each of the living categories 
    """
    live_with_partner_only = df[
        (df.live_friends == 0)
        & (df.live_partner == 1)
        & (df.live_parents == 0)
        & (df.live_siblings == 0)
        & (df.live_otherfamily == 0)
        & (df.live_children == 0)
        & (df.live_other == 0)
    ]

    live_with_partner_and_children_only = df[
        (df.live_friends == 0)
        & (df.live_partner == 1)
        & (df.live_parents == 0)
        & (df.live_siblings == 0)
        & (df.live_otherfamily == 0)
        & (df.live_children == 1)
        & (df.live_other == 0)
    ]

    live_with_children_only = df[
        (df.live_friends == 0)
        & (df.live_partner == 0)
        & (df.live_parents == 0)
        & (df.live_siblings == 0)
        & (df.live_otherfamily == 0)
        & (df.live_children == 1)
        & (df.live_other == 0)
    ]

    friends_only = df[
        (df.live_friends == 1)
        & (df.live_partner == 0)
        & (df.live_parents == 0)
        & (df.live_siblings == 0)
        & (df.live_otherfamily == 0)
        & (df.live_children == 0)
        & (df.live_other == 0)
    ]

    siblings_parent_other_family = df[
        (df.live_friends == 0)
        & (df.live_partner == 0)
        & (
            (df.live_parents == 1)
            | (df.live_siblings == 1)
            | (df.live_otherfamily == 1)
        )
        & (df.live_children == 0)
        & (df.live_other == 0)
    ]

    return (
        live_with_partner_only,
        live_with_partner_and_children_only,
        live_with_children_only,
        friends_only,
        siblings_parent_other_family,
    )


def sankey_preprocessing(df, living_category_names = LIVING_CATEGORY_NAMES):
    """
    :param df: survey data
    :return: a data frame containing only information about the living situation of survey participants and their household situation
    """
    # select only women
    woman = df[df.gender == "Woman"]

    # ignore women living alone
    woman_not_alone = woman[woman.live_alone == 0]

    # SELECT ROWS
    select = [
        "live_friends",
        "live_partner",
        "live_parents",
        "live_siblings",
        "live_otherfamily",
        "live_children",
        "live_other",
        "housework_amount",
    ]
    df = woman_not_alone[select]

    # initialise new column and set to 0 to avoid NA
    df.loc[:, "living_category"] = "0"

    # get row indices by living categories
    (
        live_with_partner_only,
        live_with_partner_and_children_only,
        live_with_children_only,
        friends_only,
        siblings_parent_other_family,
    ) = map_living_categories(df)

    # UPDATE LIVING CATEGORY
    for i in live_with_partner_only.index.tolist():
        df.loc[i, "living_category"] = "live_with_partner_only"

    for i in live_with_partner_and_children_only.index.tolist():
        df.loc[i, "living_category"] = "live_with_partner_and_children_only"

    for i in live_with_children_only.index.tolist():
        df.loc[i, "living_category"] = "live_with_children_only"

    for i in friends_only.index.tolist():
        df.loc[i, "living_category"] = "friends_only"

    for i in siblings_parent_other_family.index.tolist():
        df.loc[i, "living_category"] = "siblings_parent_other_family"

    # map the living_categories
    dict_housework = {
        "I take care of all the housework": 0,
        "I take care of most of the housework": 0,
        "We share it equally": 1,
        "I do less housework than others": 2,
        "I am not doing any housework": 2,
        # if someone said 0 for now its mapped to "equally"
        "0": 1,
    }

    # GROUP HOUSEWORK SITUATION INTO 3 CATEGORIES
    housework_mapped = []

    for i in df.housework_amount:
        if i in dict_housework: 
            housework_mapped.append(dict_housework[i])
        else:
            housework_mapped.append(0)
            print("key not found",i)

    df.loc[:, "housework_mapped"] = housework_mapped
    

    # rename the variables

    df["living_category_var_names"] = [
        living_category_names[i] for i in df.living_category
    ]
    return df[["housework_mapped", "living_category_var_names", "housework_amount"]]

