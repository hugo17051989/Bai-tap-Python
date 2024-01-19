def giatrinhonhat(s):
    a = s.split()
    if len(a)==0:
        return print('Danh sach rong')
    else:
        kq = float(a[0])
        for i in a:
            if kq > float(i):
                kq = float(i)
    return print(kq)

s = input()
try:
    giatrinhonhat(s)
except:
    print('Dinh dang dau vao khong hop le')