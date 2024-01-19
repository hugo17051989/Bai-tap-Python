nhap = input().split()
so1 = float(nhap[0])
so2 = float(nhap[2])
pheptinh = nhap[1]
if pheptinh == '+':
    print(so1, pheptinh, so2, '=', so1+so2)
elif pheptinh == '-':
    print(so1, pheptinh, so2, '=', so1-so2)
elif pheptinh == 'x':
    print(so1, pheptinh, so2, '=', so1*so2)
elif pheptinh == ':' and so2 == 0:
    print('So chia phai khac 0')
else:
    print(so1, pheptinh, so2, '=', so1/so2)

    
    
