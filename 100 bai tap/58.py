l = list(map(int, input().split()))
x = int(input())
kq = None
for i in l:
    if kq == None or abs(kq - x)<abs(i-x):
        kq = i
print(kq)