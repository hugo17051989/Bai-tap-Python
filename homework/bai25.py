check = False
try:
    a = int(input())
    b = int(input())
    check = True

except:
    print('Dinh dang dau vao khong hop le')

    if check:
        s = int(0)
        if a>b:
            print('So thu nhat lon hon so thu hai')
        else:
            for i in range(a,b+1):
                s += i
            else:
                print(s)    