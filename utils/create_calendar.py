from icalendar import Calendar, Event
from typing import List


def create_calendar(lst_event: List[Event]) -> Calendar:
    """Create calendar
    Args: lst_event (List[Event]): list of events
    Returns: Calendar
    
    Create calendar from list of events"""
    cal = Calendar()
    cal.add("prodid", "-//FREDLE09//EN")
    cal.add("version", "2.0")

    for e in lst_event:
        cal.add_component(e)

    return cal
