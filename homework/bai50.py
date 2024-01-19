import math

def kiemtra_songuyento(n):
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
def insonguyento(a,b):
    for i in range(a,b+1):
        if kiemtra_songuyento(i):
            print(i, end=' ')

a= int(input())
b= int(input())

if a<1 or b<1:
    print('Vui long nhap so tu nhien')
elif a>b:
    print('So thu nhat lon hon so thu hai')
else:
    print(insonguyento(a,b))