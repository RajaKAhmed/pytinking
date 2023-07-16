import calendar

def last_friday(year, month, day):
    _, last_day = calendar.monthrange(year, month)
    last_friday = None

    for day in range(last_day, 0, -1):
        weekday = calendar.weekday(year, month, day)
        if weekday == calendar.FRIDAY:
            last_friday = day
            break

    return last_friday