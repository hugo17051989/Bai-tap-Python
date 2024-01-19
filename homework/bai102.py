def updatetuple(x,y,k):
    t1 = list(x)[0:k]
    t2 = list(x)[k:]
    kq = t1+list(y)+t2
    return tuple(kq)
try:
    x = tuple(input().split())
    y = tuple(input().split())
    k = int(input())

    if k<0 or k > len(x):
        print('Vui long nhap k la so nguyen duong va nho hon hoac bang so phan tu cua tuple X')
    else:
        print(updatetuple(x,y,k))
except:
    print('Dinh dang dau vao khong hop le')