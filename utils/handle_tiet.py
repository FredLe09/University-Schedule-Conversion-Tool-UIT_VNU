import pandas as pd
import re


def handle_tiet(tiet: str, isStart: bool = True) -> pd.Timedelta:
    res_lst = start_time if isStart else end_time
    try:
        if re.findall(r",", tiet) == []:
            tmp = list(tiet)
        else:
            tmp = tiet.split(",")

        lst = [int(t) for t in tmp]
        return res_lst[lst[0] - 1 if lst[0] > 0 else 9]
    except Exception as e:
        print(e)
        return None


start_time = [pd.to_timedelta("07:30:00")]
for i in range(2, 14):
    tmp = start_time[-1]
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
end_time = [i + tmp for i in start_time]
