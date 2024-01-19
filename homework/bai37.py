n = int(input())

if n<0:
    print('Vui long nhap so tu nhien')
else:
    for i in range (1, n+1):
        if n%i==0:
            print(i, end=' ')

