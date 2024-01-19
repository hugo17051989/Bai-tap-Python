x = float(input())
n = int(input())
s = 1
t = 1

if n<0:
    print('Vui long nhap so tu nhien')
else:
    for i in range(1, n+1):
        t = t*i
        s = s + pow(-1,i)*(pow(x,i))/t
    print('{:.5f}'.format(s))