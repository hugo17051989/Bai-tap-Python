def nhapdanhsach(m,n):
    ds=[]
    for i in range(1,m+1):
        t = input().split()
        if len(t)!=n:
            print('Danh sach hai chieu nhap khong dung kich thuoc khai bao')
            return None
        ds.append(t)
    return ds

def phantuchunghang(s):
    t=set(s[0])
    kq = t.intersection(*[i for i in s])
    return kq


m,n= map(int,input().split())


if m<=0 or n<=0:
    print('Vui long nhap m,n la so nguyen duong')
else:
    ds=nhapdanhsach(m,n)
    if ds is not None:
        a=phantuchunghang(ds)
        print(a)