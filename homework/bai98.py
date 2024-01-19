def timgiatri(t,n):
    a = enumerate(t)
    kq = ()
    for i,j in a:
        if j == n:
            kq = kq + (i,)
    return kq

a = input().split()
n = input()
t = tuple(a)

print(timgiatri(t,n))