import datetime
while True:
    m, d = map(int, raw_input().split())
    if m == 0 and d == 0:
        break
    print ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][datetime.date(2004, m, d).weekday()]