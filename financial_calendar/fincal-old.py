import calendar
from datetime import datetime 

input_dt = datetime(2024, 2, 7)
print("Date entered is: ", input_dt.date())

day_index = input_dt.weekday()
day_name = calendar.day_name[day_index]

res = calendar.monthrange(input_dt.year, input_dt.month)
day = res[1]
print(f"""Last day of month is: {day_name}\n{input_dt.year}-{input_dt.month}-{day}""")


