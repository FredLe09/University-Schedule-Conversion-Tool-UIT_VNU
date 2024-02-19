import pandas as pd


def filter_classes(df: pd.DataFrame, classes: list[str]) -> pd.DataFrame:
    """
    Filter classes from data frame

    Args:
          df (pd.DataFrame): data frame
          classes (List[str]): list of classes

    Returns:
          pd.DataFrame: filtered data frame
    """
    res: pd.DataFrame = df.loc[df["MÃ LỚP"].isin(values=classes)]
    res.sort_values(by="MÃ LỚP")
    res.reset_index(drop=True, inplace=True)
    return res
