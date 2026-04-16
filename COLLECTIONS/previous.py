import datetime

date = datetime.date(2026, 3, 10)

prevmonth = date.month - 1 if date.month > 1 else 12
prevyear = date.year if date.month > 1 else date.year - 1

# Get the last day of the previous month
last_day_prev_month = (datetime.date(prevyear, prevmonth + 1, 1) - datetime.timedelta(days=1)).day

day = min(date.day, last_day_prev_month)

print(datetime.date(prevyear, prevmonth, day))
