import math

def phuongtrinhbacnhat(a,b):
    if a==0:
        if b==0:
            return 'vosonghiem'
        else:
            return 'vonghiem'
    else:
        return -b/a

def phuongtrinhbachai(a,b,c):
    if a == 0:
        return phuongtrinhbacnhat(b,c)
    else:
        delta = pow(b,2) - 4*a*c
        if delta < 0:
            return 'vonghiem'
        elif delta == 0:
            x = -b/(2*a)
            return x
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            return x1,x2
        
a = int(input())

if a == 1:
    b,c = map(float, input().split())
    kq = phuongtrinhbacnhat(b,c)
    if kq =='vonghiem':
        print('Phuong trinh vo nghiem')
    elif kq =='vosonghiem':
        print('Phuong trinh co vo so nghiem')
    else:
        print('Phuong trinh co mot nghiem duy nhat:\nx = {}'.format(kq))
elif a == 2:
    b,c,d = map(float, (input().split()))
    delta = pow(c,2) - 4*b*d
    kq = phuongtrinhbachai(b,c,d)
    if kq =='vonghiem':
        print('Phuong trinh vo nghiem')
    else:
        if delta == 0:
            print('Phuong trinh co nghiem kep:\nx1 = x2 = {}'.format(kq))
        else:
            print('Phuong trinh co hai nghiem phan biet la:\nx1 = {}\nx2 = {}'.format(kq[0],kq[1]))
else:
    print('Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2. Giai phuong trinh bac hai')
