def noiptutuple(t):
    a = ''.join(t)
    a=int(a)
    print(a)

t = input().split()
a = tuple(t)
b= all(i.isdigit() for i in a)
if b:
    noiptutuple(a)
else:
    print('Dinh dang dau vao khong hop le')
