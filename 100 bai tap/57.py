l = list(map(int, input().split()))
kq = 0
i = 0
while i<len(l):
    if l[i]<0 and l[i]<kq:
        kq = l[i]
    i+= 1
print(kq)