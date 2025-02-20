from datetime import datetime, timedelta

def subtract_five_days():
    return datetime.now() - timedelta(days=5)

def print_dates():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday, today, tomorrow

def drop_microseconds(dt):
    return dt.replace(microsecond=0)

def date_difference_in_seconds(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()

# Function calls and outputs
print("Date five days ago:", subtract_five_days())

yesterday, today, tomorrow = print_dates()
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

current_datetime = datetime.now()
print("Datetime without microseconds:", drop_microseconds(current_datetime))

date1 = datetime(2024, 2, 15, 12, 0, 0)
date2 = datetime(2024, 2, 20, 12, 0, 0)
print("Difference in seconds:", date_difference_in_seconds(date1, date2))
