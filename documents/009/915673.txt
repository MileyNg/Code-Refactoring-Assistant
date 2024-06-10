ff=255
clr=["black","blue","lime","aqua","red","fuchsia","yellow","white"]
val=[[0,0,0],[0,0,ff],[0,ff,0],[0,ff,ff],[ff,0,0],[ff,0,ff],[ff,ff,0],[ff,ff,ff]]

def L(s1,s2):
	return ((s1[0]-s2[0])**2+(s1[1]-s2[1])**2+(s1[2]-s2[2])**2)**0.5
	
while 1:
	rgb=raw_input()
	if rgb=="0":break
	rgb=[int(rgb[1:3],16),int(rgb[3:5],16),int(rgb[5:],16)]
	print clr[min([[L(rgb,val[i]),i] for i in range(8)])[1]]