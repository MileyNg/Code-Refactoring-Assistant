from math import *
def check(hx,hy,fx,fy,df,w,a):
	if ((hx-fx)**2 + (hy-fy)**2)**0.5 < a and Abs(atan2(hy-fy,hx-fx)-w) < df:
		return True
	else:
		return False

def Abs(e):
	e = abs(e)
	if e > pi: e = 2*pi - e
	return e

while 1:
	H,R = map(int,raw_input().split())
	if H == 0: break
	hxy = [map(int,raw_input().split()) for i in range(H)]
	U,M,S,du,dm,ds = map(int,raw_input().split())
	du,dm,ds = du*pi/360,dm*pi/360,ds*pi/360
	dxy = [map(int,raw_input().split())+[du] for i in range(U)]
	mxy = [map(int,raw_input().split())+[dm] for i in range(M)]
	sxy = [map(int,raw_input().split())+[ds] for i in range(S)]
	fxy = dxy+mxy+sxy
	count = [0]*H
	for i in range(R):
		w,a = map(int,raw_input().split())
		w = w*pi/180
		if w > pi: w -= 2*pi
		for j in range(H):
			hx,hy = hxy[j]
			if not check(hx,hy,0,0,du,w,a):
				continue
			for fx,fy,df in fxy:
				if check(hx,hy,fx,fy,df,w,a):
					break
			else:
				count[j] += 1
	mx = max(count)
	if mx > 0:
		print " ".join(map(str,[i+1 for i in range(H) if count[i] == mx]))
	else:
		print "NA"