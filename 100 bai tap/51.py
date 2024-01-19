a = int(input())
b = str(a)
i = len(b) - 3
while i>0:
    b=b[:i]+'.'+b[i:]
    i=i-3
print(b)