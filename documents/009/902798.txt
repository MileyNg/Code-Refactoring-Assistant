import datetime
WEEKDAY = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
while 1:
    a, b = map(int, raw_input().split())
    if a == b == 0:
        break
    print WEEKDAY[datetime.date(2004, a, b).weekday()]