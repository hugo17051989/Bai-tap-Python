def tong(a,b):
    return a+b
def hieu(a,b):
    return a-b
def tich(a,b):
    return a*b
def thuong(a,b):
    if b==0:
        return 'chiacho0'
    return a/b
def may_tinh(a,b,c):
    if c == '+':
        return tong(a,b)
    elif c == '-':
        return hieu(a,b)
    elif c == 'x':
        return tich(a,b)
    elif c == ':':
        return thuong(a,b)
    else:
        return 'khonghople'

nhap = input().split()
a = float(nhap[0])
b = float(nhap[2])
c = nhap[1]
kq = may_tinh(a,b,c)
if kq=='chiacho0':
    print('So chia phai lon hon 0')
elif kq == 'khonghople':
    print('Du lieu nhap khong hop le')
else:    
    print('{} {} {} = {}'.format(a,c,b,kq))

    