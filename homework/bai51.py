def sohoanthien(n):
    s = 0
    for i in range(1,n):
        if n%i == 0:
            s = s+i
    if s==n:
        return True
    return False

def insohoanthien(n):
    for i in range(1,n+1):
        if sohoanthien(i):
            print(i, end=" ")

n = int(input())
if n <0:
    print('Vui long nhap so tu nhien')
else:
    insohoanthien(n)