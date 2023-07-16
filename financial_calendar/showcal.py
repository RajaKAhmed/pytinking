import calendar
from datetime import datetime

def show_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
   
    # Print the calendar
    #print(calendar.month_name[month], year)
    month_name = calendar.month_name[month]
    result = f"\t\t\t{month_name} {year}\n"
    result += (f"\tMo\tTu\tWe\tTh\tFr\tSa\tSu\n")
    for week in cal:
        week_str ="\t|".join(str(wday) if wday != 0 else "  " for wday in week)
        result += (f"\t{week_str}\n")
    return result    
           

