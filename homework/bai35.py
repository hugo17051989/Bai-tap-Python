n = int(input())
chan = int(0)
le = int(0)

if n<0 :
    print('Vui long nhap so tu nhien')
else:
    while n>0:
        t = n%10
        if t%2 == 0:
            chan = chan + t
        else:
            le = le + t
        n = n//10
    print(chan*le)