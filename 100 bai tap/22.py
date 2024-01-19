toan =float(input())
van =float(input())
anh =float(input())

if (0<=toan<=10 and 0<=van<=10 and 0<=anh<=10):
    dtb=(toan+van+anh)/3
    if dtb>=8 and (toan>=8 or van >=8) and (toan>6.5 and van>=6.5 and anh>=6.5):
        print('Hoc sinh gioi')
    elif dtb>=6.5 and (toan>=6.5 or van>=6.5) and anh >=5:
        print('Hoc sinh kha')
    elif dtb>=5 and (toan>=5 or van>=5) and anh >=3.5:
        print('Hoc sinh trung binh')
    elif dtb>=3.5 and (toan>=3.5 or van>=3.5) and anh>=2:
        print('Hoc sinh yeu')
    else:
        print('Hoc sinh kem')
else:
    print('Nhap diem trong khoang 0 den 10')