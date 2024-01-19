l = list(map(int, input().split()))
kq = -1
i = 0
while i<len(l):
    if kq<l[i]:
        kq=l[i]
        break
    i+=1
print(kq)