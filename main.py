import pandas as pd
from icalendar import Calendar
import utils.__index__ as utils


def main(file: str) -> None:
    raw_filepath: str = f"./data/{file}"
    sheet_names: list[str] = ["TKB LT", "TKB TH"]

    try:
        df: pd.DataFrame = pd.concat(
            [utils.import_data(raw_filepath, sheet_name) for sheet_name in sheet_names]
        )
    except Exception as e:
        raise ValueError(f"Error: {e}")

    class_filepath = "./data/list_classes.txt"
    with open(class_filepath, "r") as f:
        classes: list[str] = f.read().splitlines()

    df = utils.filter_classes(df, classes)
    df = utils.clean_data_frames(df)

    def handle_datetime(df: pd.DataFrame) -> pd.DataFrame:
        """Handle datetime
        Args: df (pd.DataFrame): data frame
        Returns: pd.DataFrame

        Convert datetime to date, handle TIẾT, THỨ columns"""
        res: pd.DataFrame = df.copy()
        print(res["TIẾT"].dtype)
        res["TGBD"] = res["TIẾT"].apply(utils.handle_tiet)
        res["TGKT"] = res["TIẾT"].apply(utils.handle_tiet, isStart=False)
        res.drop("TIẾT", axis=1, inplace=True)

        res["THỨ"] = res.apply(utils.handle_thu, axis=1)
        return res

    df: pd.DataFrame = handle_datetime(df)
    df = df[pd.notnull(df["THỨ"])]

    lst: list[dict] = df.apply(utils.handle_data, axis=1).tolist()

    cal: Calendar = utils.create_calendar(
        lst_event=[utils.create_event(**e) for e in lst],
    )

    res_filepath = "./tkb.ics"
    with open(res_filepath, "wb") as f:
        f.write(cal.to_ical())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Enter your xlsx file path (in data folder: 'tkb.xlsx'): ",
    )
    parser.add_argument("--file", type=str, help="File name")

    args = parser.parse_args()
    file_path = args.file
    if not file_path:
        print("File name is not specified!")
        print("Default value: 'tkb.xlsx'")
        file_path = "tkb.xlsx"

    main(file=file_path)
