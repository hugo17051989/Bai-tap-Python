def giatriset(s):
    gtmax = max(s)
    gtmin = min(s)
    tong = sum(s)
    return gtmin, gtmax, tong

try:
    a = map(float, input().split())
    a = set(a)
    if len(a)==0:
        print('Danh sach rong')
    else:
        x,y,z = giatriset(a)
        print(x)
        print(y)
        print(z)
except:
    print("Dinh dang dau vao khong hop le")
