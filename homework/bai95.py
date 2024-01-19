def insotunhien(t):
    kq=[]
    for i in range(t):
        kq.append(i)
    print(tuple(kq))

try:
    n = int(input())
    if n <0:
        print('Vui long nhap so nguyen duong')
    else:
        insotunhien(n)
except:
    print('Dinh dang dau vao khong hop le')