import calendar
from datetime import datetime 

def get_last_day(year, month, date):
    input_dt = datetime(year, month, date)
    #print("Date entered is: ", input_dt.date())
    day_index = input_dt.weekday()
    day_name = calendar.day_name[day_index]
    res = calendar.monthrange(input_dt.year, input_dt.month)
    day = res[1]
    last_day = (f"{input_dt.year}-{input_dt.month}-{day}")
    #print(f"""Last day of month is: {day_name}\n{input_dt.year}-{input_dt.month}-{day}""")
    return day_name,last_day




