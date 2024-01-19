l = input().split()
for i in range(len(l)):
    if l[i].isnumeric():
        l[i]=int(l[i])
if len(l)%2==0:
    kq = True
    for i in range(len(l)-1):
        if not ((type(l[i]) is str and type(l[i+1]) is int) or (type(l[i]) is int and type(l[i+1]) is str)):
            kq = False
            break
    if kq:
        k=[]
        for i in range(0, len(l),2):
            k.append(l[i]*l[i+1])
        print(*k)
    else:
        print('Khong tao duoc k')
else:
    print('Khong tao duoc list k')
