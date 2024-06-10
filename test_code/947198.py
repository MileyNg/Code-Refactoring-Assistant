cat = ["mew","mcecw","mcew","mecw"]
a = raw_input()
while any(i in a for i in cat):
	a = a.replace("mew","c").replace("mcecw","c").replace("mcew","c").replace("mecw","c")
print "Cat" if a == "c" else "Rabbit"