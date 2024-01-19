thang = int(input())
nam = int(input())

if thang in [1,3,5,7,8,10,12]:
    print('Thang {} co 31 ngay'.format(thang))
if thang in [4,6,9,11]:
    print('Thang {} co 30 ngay'.format(thang))
if thang==2 and nam%4==0:
    print('Thang 2 nhuan co 29 ngay')
if thang ==2 and nam%4!=0:
    print('Thang 2 co 28 ngay')