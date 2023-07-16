import holidays

def get_country_holidays(year, country_code):
    # Retrieve holidays for the specified year and country code
    country_holidays = holidays.CountryHoliday(country_code, years=year)

    # Retrieve holidays for the specified year
    holidays_list = []
    for date, name in sorted(country_holidays.items()):
        holidays_list.append((date, name, date.strftime("(%A)")))

    return holidays_list

# Example usage
year = 2023
country_code = 'IN'
us_holidays = get_country_holidays(year, country_code)

# Print the holidays for the respective country
for date, name, day in us_holidays:
    print(date.strftime("%Y-%m-%d"), day, name)
