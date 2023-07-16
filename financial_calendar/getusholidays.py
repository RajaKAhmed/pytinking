import datetime
import dateutil.relativedelta as rd

# Calculate US federal holidays for a specific year
def us_federal_holidays(year):
    holidays_list = []

    # New Year's Day
    holidays_list.append((datetime.date(year, 1, 1), "New Year's Day"))

    # Martin Luther King Jr. Day (3rd Monday in January)
    holidays_list.append((
        datetime.date(year, 1, 1) + rd.relativedelta(weekday=rd.MO(3)),
        "Martin Luther King Jr. Day"
    ))

    # Presidents Day (3rd Monday in February)
    holidays_list.append((
        datetime.date(year, 2, 1) + rd.relativedelta(weekday=rd.MO(3)),
        "Presidents Day"
    ))

    # Memorial Day (last Monday in May)
    holidays_list.append((
        datetime.date(year, 5, 31) - rd.relativedelta(weekday=rd.MO(-1)),
        "Memorial Day"
    ))

    # Independence Day
    holidays_list.append((datetime.date(year, 7, 4), "Independence Day"))

    # Labor Day (1st Monday in September)
    holidays_list.append((
        datetime.date(year, 9, 1) + rd.relativedelta(weekday=rd.MO(1)),
        "Labor Day"
    ))

    # Columbus Day (2nd Monday in October)
    holidays_list.append((
        datetime.date(year, 10, 1) + rd.relativedelta(weekday=rd.MO(2)),
        "Columbus Day"
    ))

    # Veterans Day
    holidays_list.append((datetime.date(year, 11, 11), "Veterans Day"))

    # Thanksgiving Day (4th Thursday in November)
    holidays_list.append((
        datetime.date(year, 11, 1) + rd.relativedelta(weekday=rd.TH(4)),
        "Thanksgiving Day"
    ))

    # Christmas Day
    holidays_list.append((datetime.date(year, 12, 25), "Christmas Day"))

    return holidays_list

# Get US federal holidays for a specific year
year = 2023
us_holidays = us_federal_holidays(year)

# Add Juneteenth
us_holidays.append((datetime.date(year, 6, 19), "Juneteenth"))

# Print the federal holidays with the day
for date, name in sorted(us_holidays):
    print(date.strftime("%Y-%m-%d"), name, date.strftime("(%A)"))
