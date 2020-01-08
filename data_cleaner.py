import scipy.stats as stats


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