def trungbinhconglist(s):
    a= s.split()
    tong = 0
    if len(a)==0:
        return print('Danh sach rong')
    else:
        for i in a:
            tong = tong + float(i)
    return print(tong/len(a))

s = input()
trungbinhconglist(s)