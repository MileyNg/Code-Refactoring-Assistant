for _ in range(input()):
	s = raw_input()
	cur = 0
	for __ in range(input()):
		cmd = raw_input()
		if   cmd == "forward char":
			cur = min(len(s),cur+1)
			
		elif cmd == "forward word":
			while cur < len(s) and s[cur] == " ": cur+=1
			while cur < len(s) and s[cur] != " ": cur+=1
				
		elif cmd == "backward char":
			cur = max(0,cur-1)
			
		elif cmd == "backward word":
			while cur > 0 and s[cur-1] == " ": cur-=1
			while cur > 0 and s[cur-1] != " ": cur-=1
			
		elif cmd == "delete char":
			s = s[:cur] + s[cur+1:]
			
		elif cmd == "delete word":
			temp=cur
			if temp>=len(s):
				continue
			while temp<len(s) and s[temp]==" ":
				temp+=1
			if temp>=len(s):
				continue
			while temp<len(s) and s[temp]!=" ":
				temp+=1
			s = s[:cur] + s[temp:]
		elif cmd[:6] == "insert":
			s = s[:cur] + cmd[8:-1] + s[cur:]
			cur += len(cmd[8:-1])

	print s[:cur] + "^" + s[cur:]