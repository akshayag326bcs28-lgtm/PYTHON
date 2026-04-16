from collections import defaultdict
from datetime import datetime
dates = ["2025-01-10", "2025-01-20", "2025-02-05", "2025-02-15", "2025-03-01"]
weekday_dict = defaultdict(list)
for datestr in dates:
    date = datetime.strptime(datestr, "%Y-%m-%d")
    weekday = date.strftime("%A")
    weekday_dict[weekday].append(datestr)
for day, dlist in weekday_dict.items():
    print(f"{day} > {len(dlist)} dates")
