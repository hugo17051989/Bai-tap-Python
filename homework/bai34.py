n = int(input())
kq = int(0)

if n<0:
    print('Vui long nhap so tu nhien')
else:
    while n > 0:
        t = n%10
        n = n//10
        kq = (kq*10)+t
    print(kq)