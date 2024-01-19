def inlist(n):
    listso=[]
    listbinhphuong=[]
    for i in range(n):
        listso.append(i)
        listbinhphuong.append(pow(i,2))
    return listso, listbinhphuong

n = int(input())

if n<0:
    print('Vui long nhap so tu nhien')
else:
    a,b=inlist(n)
    print(*a)
    print(*b)