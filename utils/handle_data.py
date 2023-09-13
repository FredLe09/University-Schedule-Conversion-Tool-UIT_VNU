import pandas as pd
from datetime import timedelta

def handle_data(row: pd.Series) -> dict:
    start_day = row['NBD']
    weekday_mapping = {
        'MON': 0,
        'TUE': 1,
        'WED': 2,
        'THU': 3,
        'FRI': 4,
        'SAT': 5,
        'SUN': 6,
    }

    days_ahead = (weekday_mapping.get(row['THỨ'], None) -
                  start_day.weekday()) % 7
    next_day = start_day + timedelta(days=days_ahead)

    end_day = row['NKT']

    return {
        'title': ' - '.join([row['MÃ LỚP'], row['TÊN MÔN HỌC']]),
        'start_datetime': next_day + row['TGBD'],
        'end_datetime': next_day + row['TGKT'],
        'freq_week': row['CÁCH TUẦN'],
        'repeat_until': end_day + pd.DateOffset(days=1),
        'target_day': row['THỨ'],
        'location': row['PHÒNG HỌC'],
        'description': f'TÊN GIẢNG VIÊN: {row["TÊN GIẢNG VIÊN"]}\n' + \
            f'MÃ LỚP: {row["MÃ LỚP"]}\n' + \
            f'TÊN MÔN HỌC: {row["TÊN MÔN HỌC"]}\n' + \
            f'PHÒNG HỌC: {row["PHÒNG HỌC"]}\n' + \
            f'CÁCH TUẦN: {row["CÁCH TUẦN"]}\n' + \
            f'NGÀY BẮT ĐẦU: {row["NBD"]}\n' + \
            f'NGÀY KẾT THÚC: {row["NKT"]}\n'
            
    }