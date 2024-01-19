try:
    a = int(input())
    b = int(input())
    s= int(0)

    if a>b:
        print('So thu nhat lon hon so thu hai!')
    else:
        i = a
        while i <= b:
            s += i
            i += 1
        print(s)
except:
    print('Dinh dang dau vao khong hop le')