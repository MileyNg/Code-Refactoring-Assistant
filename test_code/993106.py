while True:
 sum=0
 str=raw_input()
 if str=="0":break
 for i in range(0,len(str)):
  sum+=int(str[i])
 print sum