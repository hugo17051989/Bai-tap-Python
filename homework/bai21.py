dulieu = input()
a,b,c = map(float, dulieu.split())
if a+b>c and a+c>b and b+c>a:
    if a*a + b*b == c*c or a*a +c*c == b*b or b*b + c*c == a*a:
        print('{}, {}, {} la ba canh cua mot tam giac vuong'.format(a,b,c))
    elif a==b and b==c:
        print('{}, {}, {} la ba canh cua mot tam giac deu'.format(a,b,c))
    elif a==b or b==c or a==c:
        print('{}, {}, {} la ba canh cua mot tam giac can'.format(a,b,c))
    elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
        print('{}, {}, {} la ba canh cua mot tam giac tu'.format(a,b,c))
    else:
        print('{}, {}, {} la ba canh cua mot tam giac nhon'.format(a,b,c))
else:
    print('{}, {}, {} khong phai la ba canh cua mot tam giac'.format(a,b,c))