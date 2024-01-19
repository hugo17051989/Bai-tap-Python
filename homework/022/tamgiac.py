try:
    with open('C:/Python/homework/022/input.inp', 'r') as fileInp:
        data = fileInp.readline()
        a,b,c = map(float, data.split())
        if a<0 or b<0 or c<0:
            result = 'Canh tam giac phai lon hon 0'
        elif a+b>c and a+c>b and b+c>a:
            if a*a + b*b == c*c or a*a +c*c == b*b or b*b + c*c == a*a:
                result='{}, {}, {} la ba canh cua mot tam giac vuong'.format(a,b,c)
            elif a==b and b==c:
                result='{}, {}, {} la ba canh cua mot tam giac deu'.format(a,b,c)
            elif a==b or b==c or a==c:
                result='{}, {}, {} la ba canh cua mot tam giac can'.format(a,b,c)
            elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
                result='{}, {}, {} la ba canh cua mot tam giac tu'.format(a,b,c)
            else:
                result='{}, {}, {} la ba canh cua mot tam giac nhon'.format(a,b,c)
        else:
            result='{}, {}, {} khong phai la ba canh cua mot tam giac'.format(a,b,c)
except FileNotFoundError:
    result = 'Không tìm thấy file'
except:
    result = 'Dinh dang file khong hop le'
fileOut = open('C:/Python/homework/022/output.out', 'wb')    
fileOut.write(result.encode('utf-8'))