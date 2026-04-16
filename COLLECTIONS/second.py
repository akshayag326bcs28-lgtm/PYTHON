import datetime
dt1 = datetime.datetime(2026, 3, 10, 10, 0, 0)
dt2 = datetime.datetime(2026, 3, 10, 12, 30, 0)
diff = dt2 - dt1
print(diff.total_seconds())
