def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

n = int(input())

if n <=0:
    print('Vui long nhap so tu nhien')
else:
    print(fibo(n))