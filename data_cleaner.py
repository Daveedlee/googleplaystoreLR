import scipy.stats as stats
import pandas as pd


def overall_cleaner(df, list_of_columns):
    """
    takes a dataframe and list of columns and returns a new dataframe only with those columns
    df = pandas data frame
    list_of_columns = a list of columns
    """
    new_df = pd.DataFrame(None)
    for i in list_of_columns:
        new_df[i] = df.loc[:,i]
    return new_df


def boxcox_trans(data, col_name, remove_col=True):
    """
    Conducts boxcox transformation without a hassle.
    data = dataframe
    col_list = a list of column names that needs to be transformed.
    remove_col = removes the column being transformed.
    """
    if remove_col:
        data[f'boxcox_{col_name}'] = stats.boxcox(data[col_name])[0]
        data.drop(col_name,axis=1,inplace=True)
    else:
        data[f'boxcox_{col_name}'] = stats.boxcox(data[col_name])[0]
    return data