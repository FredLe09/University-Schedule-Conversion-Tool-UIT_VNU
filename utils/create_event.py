from icalendar import Event
import pandas as pd


def create_event(
    start_datetime: pd.Timestamp,
    end_datetime: pd.Timestamp,
    title: str,
    location: str,
    freq_week: int,
    repeat_until: pd.Timestamp,
    target_day: str,
    description: str,
) -> Event:
    """Create event
    Args: start_datetime (pd.Timestamp): start datetime
          end_datetime (pd.Timestamp): end datetime
          title (str): title
          location (str): location
          freq_week (int): frequency week
          repeat_until (pd.Timestamp): repeat until
          target_day (str): target day
          description (str): description
    Returns: Event
    
    Create event from given arguments"""
    e = Event()
    e.add("dtstart", start_datetime)
    e.add("dtend", end_datetime)
    e.add("summary", title)
    e.add("location", location)
    e.add("description", description)

    rule = {
        "freq": "weekly",  # Lặp lại hàng tuần
        "interval": freq_week,  # Số tuần lặp lại
        "byday": target_day[:2],  # Thứ nào trong tuần
        "until": repeat_until,  # Cho tới này thì dừng lại
    }
    e.add("rrule", rule)

    return e
