a,b,c = map(int,raw_input().split())

def sort(x,y):
    if x > y:
        x,y = y,x
    return x,y

a,b = sort(a,b)
b,c = sort(b,c)
a,b = sort(a,b)

print a ,b ,c