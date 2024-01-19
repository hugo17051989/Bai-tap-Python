try:
    a = int(input())
    b = int(input())
    s = int(0)
    if a>b:
        print('So thu nhat lon hon so thu hai')
    else:
        for i in range(a,b+1):
            if i%5==0:
                print(i)
                s += 1
            if s>=10:
                print('In qua 10 so roi')
                break
        else:
            if s==0:
                print('Khong co so nao chia het cho 5')
            else:
                print('Da in het cac so chia het cho 5')
except:
    print('Dinh dang dau vao khong hop le')