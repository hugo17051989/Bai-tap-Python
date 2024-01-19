def insotunhien(n):
    tuplecon = tuple(n for _ in range(n))
    kq = (n, tuplecon)
    return kq

try:
    n=int(input())
    if n < 0:
        print('Vui long nhap so nguyen duong')
    else:
        print(insotunhien(n))
except:
    print('Dinh dang dau vao khong hop le')