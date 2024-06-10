p="0123456789543210"
for i in range(input()):
	sp,ep=raw_input().split()
	if sp<ep:
		sp=p.find(sp)
		ep=p.find(ep)+1
	else:
		sp=p.rfind(sp)
		ep=p.rfind(ep)+1
	print " ".join(list(p[sp:ep])) if sp<ep else " ".join(list(p[sp:]+p[1:ep]))