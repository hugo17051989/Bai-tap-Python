n = int(input())

if n<0:
    print('Vui long nhap so tu nhien')
else:
    s = 0
    for i in range(1,n):
        if n%i == 0:
            s = s+i
    if s==n:
        print('{} la so hoan thien'.format(n))
    else:        
        print('{} khong phai so hoan thien'.format(n))
