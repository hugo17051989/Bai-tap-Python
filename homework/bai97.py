def minmax(t):
    print(max(t))
    print(min(t))
    print(len(t))

t = input().split()
try:
    a = tuple(map(float, t))
    if len(t)==0:
        print('Danh sach rong')
    else:
        minmax(t)
except:
    print('Dinh dang dau vao khong hop le')