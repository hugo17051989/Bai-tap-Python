import math

try:
    with open('C:/Python/homework/023/input.inp', 'r') as fileInp:
        data1 = fileInp.readline().strip()
        data2 = fileInp.readline()
        if data1 == '1':
            a,b = map(float, data2.split())
            if a==0:
                if b==0:
                    result = 'Phuong trinh co vo so nghiem'
                else:
                    result = 'Phuong trinh vo nghiem'
            else:
                x = -b/a            
                result = 'Phuong trinh co 1 nghiem duy nhat x= {}'.format(x)
        elif data1 == '2':
            a,b,c = map(float, data2.split())
            delta = pow(b,2)-4*a*c
            if delta<0:
                result = 'Phuong trinh vo nghiem'
            elif delta==0:
                x=-b/(2*a)
                result = 'Phuong trinh co nghiem kep x1=x2= {}'.format(x)
            else:
                x1=((-b+math.sqrt(delta))/(2*a))
                x2=((-b-math.sqrt(delta))/(2*a))
                result = 'Phuong trinh co 2 nghiem phan biet :\nx1= {}\nx2= {}'.format(x1,x2)
        else:
            result = 'Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2. Giai phuong trinh bac hai'
except FileNotFoundError:
    result = 'Khong tim thay File input'
except:
    result = 'Dinh dang dau vao khong hop le'

fileOut = open('C:/Python/homework/023/output.inp', 'wb')
fileOut.write(result.encode('utf8'))
    