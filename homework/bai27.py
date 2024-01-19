try:    
    n = int(input())

    if 0<n<10:
        for i in range(1,10):
            s = n*i
            print('{} x {} = {}'.format(n,i,s))
    else:
        print('Chi tinh duoc bang cuu chuong 1 den 9 thoi!')
except:
    print('Dinh dang dau vao khong hop le!')