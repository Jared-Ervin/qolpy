import pandas as pd
from matplotlib import pyplot as plt


def category_to_hist(df, max_values=10):
    """
    This function takes a DataFrame and plots a histogram for each column with
    # a count of unique values less than or equal to the max_depth. By default,
    columns with 10 or less unique values will be plotted.

    Arguments:
        df {DataFrame} -- A pandas DataFrame

    Keyword Arguments:
        max_values {int} -- The treshold for calssifying a column as
        a category. (default: {10})
    """

    assert type(df) == pd.core.frame.DataFrame

    df["frequency"] = df.index
    for col in df:
        if len(df.loc[:, col].drop_duplicates()) <= max_values:
            piv = df.pivot_table(values="frequency", columns=col, aggfunc=len)
            piv.plot(kind="bar")
            plt.tick_params(
                axis="x", which="both", bottom=False, top=False, labelbottom=False
            )
            plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
            plt.xlabel(col)
            plt.ylabel("Count of Observations")
    df.drop("frequency", 1, inplace=True)


def convert_to_category(df, max_values=10):
    """
    This function counts the number of unique values in each column and
    changes the data type to category if the number of unique values is less
    than or equal to the max_depth. By default,columns with 10 or less
    unique values will be converted to data type category.

     Arguments:
    df {DataFrame} -- A pandas DataFrame

    Keyword Arguments:
        max_values {int} -- The treshold for calssifying a column as
        a category. (default: {10})
    """

    for col in df:
        if len(df.loc[:, col].drop_duplicates()) <= max_values:
            df[col] = df[col].astype("category")
    return df
