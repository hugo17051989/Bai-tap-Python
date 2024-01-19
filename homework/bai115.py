def kethoplist(a,b):
    t = zip(a,b)
    d={}
    for i in t:
       d.update({i[0]: i[1]})
    return d

a = input().split()
b = input().split()

if len(a)!=len(b):
    print('Vui long nhap key va value bang nhau')
else:
    kq=kethoplist(a,b)
    print(kq)
    for i,j in kq.items():
        print(f"{i}: {j}")