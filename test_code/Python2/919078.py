import datetime
while 1:
	y1,m1,d1,y2,m2,d2=map(int,raw_input().split())
	if y1==-1:break
	print (datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).days
	
	