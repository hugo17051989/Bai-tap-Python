def listdaonguoc(s):
    a=list(s)
    kq = [a[i] for i in range(-1,-(len(a)+1),-1) ]
    return kq

s = input()
print(*listdaonguoc(s))