def tinhtongvatrungbinhcong(s):
    a = s.split()
    tong = 0
    so = 0
    for c in a:
        if c.isdigit():
            tong = tong + int(c)
            so += 1
    if so==0:
        return 0,0
    trungbinhcong = tong/so
    return tong,trungbinhcong

s = input()
a,b = tinhtongvatrungbinhcong(s)
print(a)
print(b)