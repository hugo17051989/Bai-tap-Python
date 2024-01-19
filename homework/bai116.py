def taodict():
    a= input().split()
    b= input().split()
    if len(a)!=len(b):
        print('Vui long nhap key va value bang nhau')
        return None
    kq=dict(zip(a,b))
    return kq

def capnhatdict(a,b):
    if len(a)<len(b):
        b.update(a)
        return b
    a.update(b)
    return a

a=taodict()
b=taodict()
if a is not None and b is not None:
    kq = capnhatdict(a,b)
    print(kq)