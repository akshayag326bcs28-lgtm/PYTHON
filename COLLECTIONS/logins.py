from collections import Counter
from datetime import datetime

logins = [
    "2026-03-10 10:00",
    "2026-03-10 12:00",
    "2026-03-11 09:30",
    "2026-03-11 11:45",
    "2026-03-11 14:00"
]

# Extract hour from each timestamp
hours = [datetime.strptime(ts, "%Y-%m-%d %H:%M").hour for ts in logins]

# Count frequency of each hour
counter = Counter(hours)

# Get the most common hour and its count
most_common_hour, count = counter.most_common(1)[0]

print(f"{most_common_hour} AM -> {count} logins")
