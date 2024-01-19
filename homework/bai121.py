def taodict():
    a= input().split()
    try:
        b= list(map(int,input().split()))
    except:
        print('Vui long nhap so nguyen')
        return None
    if len(a)!=len(b):
        print('Vui long nhap key va value bang nhau')
        return None
    kq=dict(zip(a,b))
    return kq

def sapxepvalue(d):
    t=d.items()
    t=sorted(t,key=lambda item:item[1])
    kq={}
    for i in t:
        kq.update(t)
    return kq

a = taodict()
if a is not None:
    print(a)
    print(sapxepvalue(a))
else:
    print(' ')