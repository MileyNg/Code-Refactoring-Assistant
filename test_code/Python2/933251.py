n,T = map(int,raw_input().split())
t = eval(raw_input().replace("^","**"))*T
print t if t <= 10**9 else "TLE"