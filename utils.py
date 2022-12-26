import requests
from datetime import date, datetime, timedelta
import time

def timedate(hours_delta = 5, time_delta = 0):
    today = date.today()
    now = datetime.now() - timedelta(hours=hours_delta)
    if now.hour + hours_delta > 23:
        today = today - timedelta(days=1)
    page_date = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    time.sleep(time_delta)
    now = datetime.now()
    page_date_modified = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    time.sleep(time_delta)
    now = datetime.now()
    page_date_modified_gmt = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    return page_date, page_date_modified, page_date_modified_gmt