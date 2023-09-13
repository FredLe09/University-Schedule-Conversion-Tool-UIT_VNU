import pandas as pd
from typing import List


def filter_classes(df: pd.DataFrame, classes: List[str]) -> pd.DataFrame:
    """Filter classes from data frame
    Args: df (pd.DataFrame): data frame
          classes (List[str]): list of classes
    Returns: pd.DataFrame"""
    res = df.loc[df["MÃ LỚP"].isin(classes)]
    res.sort_values("MÃ LỚP")
    res.reset_index(drop=True, inplace=True)
    return res
