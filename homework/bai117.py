def taodict():
    a= input().split()
    b= input().split()
    if len(a)!=len(b):
        print('Vui long nhap key va value bang nhau')
        return None
    kq=dict(zip(a,b))
    return kq

def xoaphantutrung(d):
    gtvalue=list()
    tam=d.copy()
    for i,j in d.items():
        if j in gtvalue:
            tam.pop(i)
        else:
            gtvalue.append(j)
    return tam

a=taodict()
if a is not None:
    kq = xoaphantutrung(a)
    print(kq)
else:
    print(' ')