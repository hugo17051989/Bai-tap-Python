import math

dulieu = input()
check = False

try:
    a,b,c = map(float, dulieu.split())
    check = True

    if check:    
        delta = pow(b,2) - 4*a*c
        if a == 0: 
            if b!= 0:
                print('Phuong trinh co 1 nghiem duy nhat : x=', -c/b)
            elif b==0 and c!=0:
                print('Phuong trinh vo nghiem')
            else:
                print("Phuong trinh co vo so nghiem")    
        elif delta < 0:
            print('Phuong trinh vo nghiem')
        elif delta == 0:
            print('Phuong trinh co nghiem kep : \nx1=x2 =', -b/(2*a))
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("Phuong trinh co 2 nghiem phan biet : \nx1={} \nx2={}".format(x1,x2))
        
except:
    print("Dinh dang dau vao khong hop le")