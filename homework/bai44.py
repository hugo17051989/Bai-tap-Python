def tinhtong(n):
    int(n)
    s = 0
    if n<0:
        print('Vui long nhap so tu nhien')
    elif n:
        return n + tinhtong(n-1)
    return 0