def ptuchungrieng(x,y):
    a = x^y
    b = x&y
    return a,b

x = set(input().split())
y = set(input().split())

a,b = ptuchungrieng(x,y)
print(a)
print(b)