#coding: utf-8

a = []

for i in range(10):
	num = input()
	a.append(int(num))

a.sort(reverse=True)

for i in range(3):
	print(a[i])