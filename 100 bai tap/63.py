l = list(map(float, input().split()))
kq=-1

if 0<=len(l)<=2:
    print(kq)
else:
    for i in range(1,len(l)-1):
        if l[i]==l[i-1]*l[i+1]:
            kq=l[i]
            break
    print(kq)