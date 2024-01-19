nhap = input()
check = False

try:
    a,b,c = map(float, nhap.split())
    check = True

except:
    print('Du lieu nhap khong hop le')

if check:
    if a < 0 or b < 0 or c < 0:
        print('Canh tam giac phai lon hon 0')
    elif a+b>c and a+c>b and b+c>a:
        print(a, b, c, "la 3 canh cua mot tam giac")
    else:
        print(a, b, c, "khong phai la 3 canh cua mot tam giac")
