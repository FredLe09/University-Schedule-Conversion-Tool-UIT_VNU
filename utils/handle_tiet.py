import pandas as pd
import re
from typing import Optional


def handle_tiet(tiet: str, isStart: bool = True) -> Optional[pd.Timedelta]:
    """
    Converts a string representation of a time interval to a pandas Timedelta object.

    Args:
        tiet (str): The string representation of the time interval.
        isStart (bool, optional): Indicates whether the time interval is a start time or an end time. Defaults to True.

    Returns:
        pd.Timedelta: The converted time interval as a pandas Timedelta object.
    """
    if tiet == "*":
        return None

    tmp: list[str]
    tiet = str(tiet)
    if re.findall(r",", tiet) == []:
        tmp = list(tiet)
    else:
        tmp = tiet.split(",")

    lst: list[int] = [int(t) for t in tmp]
    if isStart:
        return start_time[lst[0] - 1 if lst[0] > 0 else 9]
    else:
        return end_time[lst[-1] - 1 if lst[-1] > 0 else 9]


start_time: list[pd.Timedelta] = [pd.to_timedelta("07:30:00")]
for i in range(2, 14):
    tmp: pd.Timedelta = start_time[-1]
    if i in [4, 9]:
        tmp += pd.to_timedelta("01:00:00")
    elif i == 6:
        tmp += pd.to_timedelta("02:15:00")
    elif i == 10:
        tmp += pd.to_timedelta("01:30:00")
    else:
        tmp += pd.to_timedelta("00:45:00")

    start_time.append(tmp)

tmp = pd.to_timedelta("00:45:00")
end_time: list[pd.Timedelta] = [i + tmp for i in start_time]
