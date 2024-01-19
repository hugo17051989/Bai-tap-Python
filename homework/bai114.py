def taodict(n):
    d={}
    for i in range(0,n):
        d.update({i: pow(i,2)})
    return d

n=int(input())
if n<0:
    print('Vui long nhap so nguyen duong')
else:
    print(taodict(n))