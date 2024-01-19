def hoandoilist(a,b):
    nuads1=len(a)//2
    nuads2=len(b)//2
    t1=a[nuads1:]
    t2=b[nuads2:]
    a = a[:nuads1]+t2
    b = b[:nuads2]+t1
    return a,b

a = input().split()
b = input().split()

ds1,ds2 = hoandoilist(a,b)
print(*ds1)
print(*ds2)
