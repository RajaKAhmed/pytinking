import calendar
import sys
import os

# Access command-line arguments
arguments = sys.argv

# Check the number of arguments
if len(arguments) < 3:
    print("Please provide the necessary arguments.")
    print("Usage: python script.py <year> <month>")
    sys.exit(1)

# Extract the argument values
year = int(arguments[1])
month = int(arguments[2])

# Generate the calendar string
cal = calendar.monthcalendar(year, month)

# Print the calendar
print(calendar.month_name[month], year)
print(f"\tMo\tTu\tWe\tTh\tFr\tSa\tSu")
for week in cal:
    week_str ="\t|".join(str(day) if day != 0 else "  " for day in week)
    print(f"\t{week_str}")