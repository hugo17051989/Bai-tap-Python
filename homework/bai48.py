def giaithua(a):
    if a==0:
        return 1
    return a*giaithua(a-1)
    
n = int(input())
if n<0:
    print('Vui long nhap so tu nhien')
else:
    print(giaithua(n))