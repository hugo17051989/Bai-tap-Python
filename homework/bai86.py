def nhandanhsach(a,b):
    for i in range(1, len(a)+1):
        tich = a[i-1]*b[-i]
        print(tich,end=' ')

a = input().split()
b = input().split()

if len(a)!=len(b):
    print ('Vui long nhap hai chuoi co cung kich thuoc')
else:
    a = list(map(float, a))
    b = list(map(float, b))
    nhandanhsach(a,b)
    