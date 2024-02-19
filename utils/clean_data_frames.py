import pandas as pd


def clean_data_frames(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean data frame

    Args:
        df (pd.DataFrame): data frame

    Returns:
        pd.DataFrame: Cleaned data frame

    Remove unnecessary columns, convert data types
    """
    res: pd.DataFrame = df[
        [
            "MÃ MH",
            "MÃ LỚP",
            "TÊN MÔN HỌC",
            "TÊN GIẢNG VIÊN",
            "THỨ",
            "TIẾT",
            "CÁCH TUẦN",
            "PHÒNG HỌC",
            "NBD",
            "NKT",
        ]
    ]

    res.loc[:, "NBD"] = pd.to_datetime(res["NBD"], format="%Y-%m-%d")
    res.loc[:, "NKT"] = pd.to_datetime(res["NKT"], format="%Y-%m-%d")
    return res
