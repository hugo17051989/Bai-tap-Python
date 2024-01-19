l = list(map(float, input().split()))
kq = None
for i in range(len(l)-2):
    if (l[i+1]-l[i])!=(l[i+2]-l[i+1]):
        print('Day khong phai cap so cong')
        print(kq)
        break
else:
    kq = l[1]-l[0]
    print('Day la cap so cong')
    print(kq)