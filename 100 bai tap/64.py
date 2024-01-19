l = list(map(float, input().split()))

for i in range(len(l)-1):
    if (l[i]+l[i+1])%2!=1:
        print('Day khong phai day chan le')
        break
else:
    print('Day la day chan le')