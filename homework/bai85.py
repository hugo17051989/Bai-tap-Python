def xoakhoangtrang(s):
    s=s.strip()
    while '  ' in s:
        s=s.replace('  ',' ')
    return s

def ten_quoctich(a,b):
    for i in a:
        xoakhoangtrang(i)
    for i in b:
        xoakhoangtrang(i)
    x = list(zip(a,b))
    for ten, quoctich in x:
        print(ten,'-',quoctich)

a = input().split(',')
b = input().split(',')

if len(a)!=len(b):
    print('Vui long nhap hai chuoi cung kich thuoc')
elif len(a)==0 or len(b)==0:
    print('Du lieu rong')
else:
    ten_quoctich(a,b)