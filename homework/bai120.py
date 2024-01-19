def taodict():
    try:
        a= list(map(int,input().split()))
    except:
        print('Vui long nhap so nguyen')
        return None
    b = input().split()
    if len(a)!=len(b):
        print('Vui long nhap key va value bang nhau')
        return None
    kq=dict(zip(a,b))
    return kq

def sapxepkey(d):
    listkey=d.keys()
    listkey=sorted(listkey)
    kq={}
    for i in listkey:
        kq[i]=d[i]
    return kq

a = taodict()
if a is not None:
    print(a)
    print(sapxepkey(a))
else:
    print(' ')
