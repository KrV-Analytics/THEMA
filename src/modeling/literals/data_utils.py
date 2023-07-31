
import pandas as pd 
import numpy as np


####################################################################################
# 
#  node_desription Helper functions
# 
####################################################################################



def get_minimal_std(df: pd.DataFrame, mask: np.array, density_cols=None):
    """Find the column with the minimal standard deviation
    within a subset of a Dataframe.

    Parameters
    -----------
    df: pd.Dataframe
        A cleaned dataframe.

    mask: np.array
        A boolean array indicating which indices of the dataframe
        should be included in the computation.

    Returns
    -----------
    col_label: int
        The index idenitfier for the column in the dataframe with minimal std.

    """
    if density_cols is None:
        density_cols = df.columns
    sub_df = df.iloc[mask][density_cols]
    col_label = sub_df.columns[sub_df.std(axis=0).argmin()]
    return col_label



####################################################################################
# 
#  group_identity Helper functions
# 
####################################################################################

# Filter functions that assign a value to columns => minimum is taken to be the most 
# important columns 

def std_zscore_threshold_filter(col, global_stats:dict(), std_threshold = 1, zscore_threshold = 1): 
    """
    TODO: Fill out Doc String
    """
    std = np.std(col)
    if std == 0:
        zscore = np.inf 
    else:
        zscore = (np.mean(col) - global_stats['clean']['mean'][col.name])/std

    if abs(zscore) > zscore_threshold and abs(std) < std_threshold:
        return 0 
    else:
        return 1



def get_best_std_filter(col, global_stats:dict()):
    """
    TODO: Fill out Doc String
    """
    std = np.std(col)    
    return std


def get_best_zscore_filter(col, global_stats:dict()):
    """
    TODO: Fill out Doc String
    """
    zscore = (np.mean(col) - global_stats['clean']['mean'][col.name])/np.std(col)

    return zscore


####################################################################################
# 
#  Auxillary functions
# 
####################################################################################


def error(x, mu):
    return abs((x - mu) / mu)