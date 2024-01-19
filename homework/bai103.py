def sapxeptuple(t):
    kq = sorted(tuple(t),reverse=True)
    return tuple(kq)

try:
    a = map(float, input().split())
    print(sapxeptuple(a))
except:
    print('Dinh dang dau vao khong hop le')