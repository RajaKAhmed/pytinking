import pandas as pd
import calendar

def get_fiscal_quarters(year):
    start_month = 1  # Start of fiscal year, assuming April
    end_month = 2  # End of fiscal year, assuming March

    fiscal_start_date = pd.Timestamp(year, start_month, 1)
    fiscal_end_date = pd.Timestamp(year + 1, end_month, 1) - pd.DateOffset(days=1)

    quarters = pd.date_range(fiscal_start_date, fiscal_end_date, freq='QS')
    fiscal_quarters = [f"{q.quarter}Q{q.year}" for q in quarters]

    return fiscal_quarters


def get_quarter_dates(year):
    fiscal_quarters = get_fiscal_quarters(year)
    quarter_dates = []

    for quarter in fiscal_quarters:
        q_start = pd.Timestamp(int(quarter.split('Q')[1]), int(quarter.split('Q')[0]) * 3 - 2, 1)
        q_end = pd.Timestamp(int(quarter.split('Q')[1]), int(quarter.split('Q')[0]) * 3, calendar.monthrange(int(quarter.split('Q')[1]), int(quarter.split('Q')[0]) * 3)[1])
        num_days = (q_end - q_start).days + 1
        quarter_dates.append((quarter, q_start.date(), q_end.date(), num_days, q_start.day_name(), q_end.day_name()))

    return quarter_dates


# Example usage
year = 2023
quarter_dates = get_quarter_dates(year)

for quarter, start_date, end_date, num_days, start_day, end_day in quarter_dates:
    print(f"Quarter: {quarter}")
    print(f"Start Date: {start_date} ({start_day})")
    print(f"End Date: {end_date} ({end_day})")
    print(f"Number of Days: {num_days}")
    print()
