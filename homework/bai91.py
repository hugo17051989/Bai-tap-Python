def nhapdanhsach(m,n):
    ds=[]
    for i in range(1,m+1):
        t = input().split()
        if len(t)!=n:
            print('Danh sach hai chieu nhap khong dung kich thuoc khai bao')
            return None
        else:
            ds.append(t)
    return ds

def phantudainhat(s):
    dodai=[]
    if s==None:
        return None
    else:
        for i in s:
            dodai.append(len(i))
        ptumax=max(dodai)
        t = dodai.index(ptumax)
        return s[t]

def phantudainhatmoihang(s):
    kq=[]
    if s==None:
        return None
    else:
        for i in s:
            kq.append(phantudainhat(i))
        return print(*kq)

check = False
try:
    m,n = map(int, input().split())
    check = True
except:
    print("Dinh dang dau vao khong hop le")
if check:
    if m<0 or n<0:
        print('Vui long nhap so nguyen duong')
    else:
        ds = nhapdanhsach(m,n)
        phantudainhatmoihang(ds)
