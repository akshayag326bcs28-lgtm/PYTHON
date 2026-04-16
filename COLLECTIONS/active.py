from datetime import datetime, timedelta
logins = [

("user1", "2026-03-10 10:00"),
("user2", "2026-03-11 12:00"),
("user1", "2026-03-11 15:00"),
("user3", "2026-03-09 09:00"),
]
now = datetime.strptime("2026-03-11 16:00", "%Y-%m-%d %H:%M")
activeusers = {user for user, ts in logins if now - datetime.strptime(ts, "%Y-%m-%d %H:%M") <= timedelta(days=1)}
print(activeusers)
