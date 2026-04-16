import datetime
count = 0
year = 2025
month = 1
for day in range(1, 32):
    try:
        d = datetime.date(year, month, day)
        if d.weekday() == 6:
            count += 1
    except ValueError:
        break
print(count)
