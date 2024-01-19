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

def taolisttudict(d):
    print(d)
    listkq=[]
    listkey=d.keys()
    kq = '-'.join(listkey)
    print(kq)
    print(sum(d.values()))

a = taodict()
if a is not None:
    taolisttudict(a)
else:
    print('')
