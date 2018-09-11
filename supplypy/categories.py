# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 08:49:47 2018

@author: j.ervin
"""
import pandas as pd
import matplotlib.pyplot as plt


def cathist(df, max_depth=10):
    """
    This function takes a DataFrame and plots a histogram for each column with
    a count of unique values less than or equal to the max_depth.
    """

    assert type(df) == pd.core.frame.DataFrame
    def
    df['frequency'] = df.index
    for col in df:
        if len(df.loc[:, col].drop_duplicates()) <= max_depth:
            piv = df.pivot_table(
                values='frequency',
                columns=col,
                aggfunc=len)
            piv.plot(kind='bar')
            plt.tick_params(axis='x', which='both', bottom=False,
                            top=False, labelbottom=False)
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.xlabel(col)
            plt.ylabel('Count of Observations')
    df.drop('frequency', 1, inplace=True)


def identifycat(df, max_depth=10):
    """
    This function counts the number of unique values in each column and
    changes the data type to category if the number of unique values is less
    than or equal to the max_depth.
    """

    for col in df:
        if len(df.loc[:, col].drop_duplicates()) <= max_depth:
            df[col] = df[col].astype('category')
    return(df)
