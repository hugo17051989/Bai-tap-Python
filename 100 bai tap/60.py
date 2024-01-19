l = list(map(int, input().split()))
kq = True
for i in range(len(l)-1):
    if l[i]>=l[i+1]:
        kq = False
print(kq)