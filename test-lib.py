from financial_calendar import showcal
from financial_calendar import getlastday
from financial_calendar import lastfriday
from financial_calendar import lastmonday
from financial_calendar import fiscalquarters
import sys

arguments = sys.argv

if len(arguments) < 4:
    print("Please provide the necessary arguments.")
    print("Usage: python script.py <year> <month> <day>")
    sys.exit(1)

year = int(arguments[1])
month = int(arguments[2])
day = int(arguments[3])

x = showcal.show_calendar(year, month)
print(x)
last_friday_dt = lastfriday.last_friday(year, month, day)
fiscal_qtrs = fiscalquarters.get_fiscal_quarters(year)

last_monday_dt = lastmonday.last_monday(year, month, day)
day, date = getlastday.get_last_day(year, month, day)
print(f"""The following date: {date} falls on {day}\n
      Last friday of the month is on {last_friday_dt}\n
      Last Monday of the month is on {last_monday_dt}\n
      Here are fiscal quarters {fiscal_qtrs}\n
      Here are fiscal dates\n\n""")
qtr_dates = fiscalquarters.get_quarter_dates(year)
for quarter, start_date, end_date, num_days, start_day, end_day in qtr_dates:
    print(f"Quarter: {quarter}")
    print(f"Start Date: {start_date} ({start_day})")
    print(f"End Date: {end_date} ({end_day})")
    print(f"Number of Days: {num_days}")
    print()