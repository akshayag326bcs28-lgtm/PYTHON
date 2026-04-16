import datetime
year = 2028
isleap = (datetime.date(year, 3, 1) - datetime.date(year, 2, 28)).days == 2
print(isleap)
