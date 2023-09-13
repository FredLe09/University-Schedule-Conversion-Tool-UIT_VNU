import pandas as pd


def import_data(file_path: str, sheet_name: str,) -> pd.DataFrame:
    """Import data from excel file
    Args: file_path (str): path to excel file
          sheet_name (str): sheet name in excel file
    Returns: pd.DataFrame"""
    try:
        res = pd.read_excel(
            io=file_path,
            sheet_name=sheet_name,
            skiprows=7,
        )
        res.drop("Unnamed: 23", axis=1, inplace=True)
        res.set_index("STT", inplace=True)
        return res
    except Exception as e:
        print(e)
        return None
