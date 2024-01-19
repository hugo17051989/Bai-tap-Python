def tinhtong(a,b):
    kq = 0
    while a>0:
        t = a%10
        if t%2==b:
            kq=kq+t
        a=a//10
    return kq
    
def tinhtich(a):
    return tinhtong(a,0)*tinhtong(a,1)

n = int(input())

if n<0:
    print('Vui long nhap so tu nhien')
else:
    print(tinhtich(n))
            