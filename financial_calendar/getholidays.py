import datetime
import dateutil.easter
import dateutil.relativedelta as rd
import holidays
# Calculate US federal holidays for a specific year
def us_federal_holidays(year):
    holidays_list = []
    
    # New Year's Day
    holidays_list.append(datetime.date(year, 1, 1))

    # Martin Luther King Jr. Day (3rd Monday in January)
    holidays_list.append(
        datetime.date(year, 1, 1) + rd.relativedelta(weekday=rd.MO(3))
    )

    # Presidents Day (3rd Monday in February)
    holidays_list.append(
        datetime.date(year, 2, 1) + rd.relativedelta(weekday=rd.MO(3))
    )

    # Memorial Day (last Monday in May)
    holidays_list.append(
        datetime.date(year, 5, 31) - rd.relativedelta(weekday=rd.MO(-1))
    )

    # Independence Day
    holidays_list.append(datetime.date(year, 7, 4))

    # Labor Day (1st Monday in September)
    holidays_list.append(
        datetime.date(year, 9, 1) + rd.relativedelta(weekday=rd.MO(1))
    )

    # Columbus Day (2nd Monday in October)
    holidays_list.append(
        datetime.date(year, 10, 1) + rd.relativedelta(weekday=rd.MO(2))
    )

    # Veterans Day
    holidays_list.append(datetime.date(year, 11, 11))

    # Thanksgiving Day (4th Thursday in November)
    holidays_list.append(
        datetime.date(year, 11, 1) + rd.relativedelta(weekday=rd.TH(4))
    )

    # Christmas Day
    holidays_list.append(datetime.date(year, 12, 25))

    return holidays_list

# Get US federal holidays for a specific year
year = 2023
us_holidays = us_federal_holidays(year)

# Print the federal holidays
for holiday in us_holidays:
    print(holiday)


def get_country_holidays(year, country_code):
    # Get the country's holiday object
    country_holidays = getattr(holidays, country_code.upper())()

    # Retrieve holidays for the specified year
    holidays_list = []
    for date, name in sorted(country_holidays.items()):
        if date.year == year:
            holidays_list.append((date, name, date.strftime("(%A)")))

    return holidays_list

# Example usage
year = 2023
country_code = 'US'
us_holidays = get_country_holidays(year, country_code)

# Print the holidays for the respective country
for date, name, day in us_holidays:
    print(date.strftime("%Y-%m-%d"), day, name)
