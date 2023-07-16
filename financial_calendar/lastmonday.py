import calendar

def last_monday(year, month, day):
    _, last_day = calendar.monthrange(year, month)
    last_monday = None

    for day in range(last_day, 0, -1):
        weekday = calendar.weekday(year, month, day)
        if weekday == calendar.MONDAY:
            last_monday = day
            break

    return last_monday