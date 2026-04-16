from datetime import datetime
dates = ["2025-01-10", "2024-12-31", "2025-02-15"]
oldest = min(datetime.strptime(date, "%Y-%m-%d") for date in dates)
print(oldest.date())
