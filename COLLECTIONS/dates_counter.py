from collections import Counter
dates = ["2025-01-10", "2025-01-20", "2025-01-10", "2025-02-15"]
counter = Counter(dates)
duplicates = [date for date, count in counter.items() if count > 1]
print(duplicates)
