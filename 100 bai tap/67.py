l = list(map(int, input().split()))

chan = []
le = []
khong = []

for i in l:
    if i==0:
        khong.append(i)
    elif i%2==0 and i!=0:
        chan.append(i)
    else:
        le.append(i)
kq=chan+khong+le
print(*kq)
