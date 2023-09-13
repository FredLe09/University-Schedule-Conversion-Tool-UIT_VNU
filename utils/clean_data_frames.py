import pandas as pd


def clean_data_frames(df: pd.DataFrame) -> pd.DataFrame:
    """Clean data frame
    Args: df (pd.DataFrame): data frame
    Returns: pd.DataFrame

    Remove unnecessary columns, convert data types
    """
    res = df[
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

    res.NBD = res.NBD.apply(pd.to_datetime, format="%Y-%m-%d")
    res.NKT = res.NKT.apply(pd.to_datetime, format="%Y-%m-%d")
    return res
