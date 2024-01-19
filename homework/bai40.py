import math

a = int(input())
b = int(input())

if a<0 or b<0 :
    print('Vui long nhap so tu nhien')
elif a>b:
    print('So thu nhat lon hon so thu hai')
else:
    for i in range(a,b+1):
        if i>1:
            for j in range(2, int(math.sqrt(i))+1):
                if i%j==0:
                    break
            else:
                print(i, end=' ')