p="0123456789543210"
for i in range(input()):
	sp,ep=raw_input().split()
	(sp,ep)=(p.find(sp),p.find(ep)+1) if sp<ep else (p.rfind(sp),p.rfind(ep)+1)
	print " ".join(p[sp:ep]) if sp<ep else " ".join(p[sp:]+p[1:ep])