try:
    n = int(input())

    if 0<n<10:
        i = int(0)
        j = int(1)
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=' ')
            print()
    else:
        print("Vui long nhap gia tri tu 1 den 9")    
except:
    print('Dinh dang dau vao khong hop le')