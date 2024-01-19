try:
    n = int(input())

    if 0<n<10:
        i = int(0)
        j = int(n)
        for i in range(n):
            for j in range(n-i, 0, -1):
                print(j, end=' ')
            print()
    else:
        print("Vui long nhap gia tri tu 1 den 9")    
except:
    print('Dinh dang dau vao khong hop le')