n = int(input())

if n < 0:
    print('Vui long nhap so tu nhien')
elif n==1 or n==2:
    print(1)
else:
    i1=1
    i2=1
    for i in range(3,n+1):
        s = i1+i2
        i1=i2
        i2=s
    print(s)