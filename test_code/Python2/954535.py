while 1:
	a,b,c,d,e = map(int,raw_input().split())
	if a == 0: break
	na,nb,nc = map(int,raw_input().split())
	ans = a*na + b*nb + c*nc
	if nc >= d:
		ans = a*na + b*nb +e*nc
	else:
		nd = d; d -= nc
		t = nb if nb < d else d
		nb -= t; d -= t
		t = na if na < d else d
		na -= t; d -= t
		ans = min(ans,a*na + b*nb + e*nd)
	print ans