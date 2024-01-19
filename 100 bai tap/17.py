a = float(input())
b = float(input())
c = float(input())

if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b

print(a,b,c,end=' ')