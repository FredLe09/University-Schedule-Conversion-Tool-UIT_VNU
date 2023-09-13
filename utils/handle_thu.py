import pandas as pd


day_of_week_lst = ["", "", "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


def handle_thu(row: pd.Series) -> str:
    try:
        return day_of_week_lst[int(row["THỨ"])]
    except ValueError:
        print("At row: ", row["MÃ LỚP"], " ", row["THỨ"])
        return None
