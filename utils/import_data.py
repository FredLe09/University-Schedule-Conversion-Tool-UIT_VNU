import pandas as pd

DEFAULT_ROW_SKIP: int = 7


def import_data(file_path: str, sheet_name: str) -> pd.DataFrame:
    """
    Import data from an excel file.

    Args:
        file_path (str): Path to the excel file.
        sheet_name (str): Name of the sheet in the excel file.

    Returns:
        pd.DataFrame: The imported data as a pandas DataFrame.
    """
    try:
        res: pd.DataFrame = pd.read_excel(
            io=file_path,
            sheet_name=sheet_name,
            skiprows=DEFAULT_ROW_SKIP,
        )
        res.drop("Unnamed: 23", axis=1, inplace=True)
        res.set_index("STT", inplace=True)
        return res
    except Exception as e:
        raise ValueError(f"Error: {e}")
