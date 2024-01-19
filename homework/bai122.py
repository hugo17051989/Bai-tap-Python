def taodict():
    a= input().split()
    b= input().split()
    if len(a)!=len(b):
        print('Vui long nhap key va value bang nhau')
        return None
    kq=dict(zip(a,b))
    return kq

def thaythedict(s,d):
    kq=[]
    for i in s:
        if i in d.keys():
            kq.append(d.get(i))
        else:
            kq.append(i)
    return kq

s = input().split()
d = taodict()
if d is not None:
    print(d)
    print(*thaythedict(s,d))
else:
    print(' ')