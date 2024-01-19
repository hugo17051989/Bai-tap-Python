print('Nhap gia tri :')
a = input()
b = a.split()
check = False
try:
    c = map(int, b)
    tong = sum(c)
    check = True
except:
    print('Du lieu nhap khong hop le')

if check:
    print('Tong cua day so : ', tong)