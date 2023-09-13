import utils.__index__ as utils
import pandas as pd


def main(file: str) -> None:
    raw_filepath = f"./data/{file}"
    sheet_name_LT = "TKB LT"
    sheet_name_TH = "TKB TH"

    try:
        df_1 = utils.import_data(raw_filepath, sheet_name_LT)
        df_2 = utils.import_data(raw_filepath, sheet_name_TH)
        df = pd.concat([df_1, df_2])
    except Exception as e:
        print(e)
        return

    class_filepath = "./data/list_classes.txt"
    with open(class_filepath, "r") as f:
        classes = f.read().splitlines()

    df = utils.filter_classes(df, classes)
    df = utils.clean_data_frames(df)

    def handle_datetime(df: pd.DataFrame) -> pd.DataFrame:
        """Handle datetime
        Args: df (pd.DataFrame): data frame
        Returns: pd.DataFrame

        Convert datetime to date, handle TIẾT, THỨ columns"""
        res = df.copy()
        res["TGBD"] = res["TIẾT"].apply(utils.handle_tiet)
        res["TGKT"] = res["TIẾT"].apply(utils.handle_tiet, isStart=False)
        res.drop("TIẾT", axis=1, inplace=True)

        res["THỨ"] = res.apply(utils.handle_thu, axis=1)
        return res

    df = handle_datetime(df)
    df = df[pd.notnull(df["THỨ"])]

    lst = df.apply(utils.handle_data, axis=1).tolist()

    cal = utils.create_calendar(
        [utils.create_event(**e) for e in lst],
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
