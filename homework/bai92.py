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

def indanhsach(s):
    if s==None:
        return None
    else:
        for i in s:
            print(*i)

def matranchuyenvi(s):
    kq=[]
    if s==None:
        return None
    else:
        m = len(s[0]) #so dong moi = so cot cu
        n = len(s) #so cot moi = so dong cu
        for i in range(m):
            t=[]
            for j in range(n):
                t.append(s[j][i])
            kq.append(t)
        return kq      

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
        s = nhapdanhsach(m,n)
        t = matranchuyenvi(s)
        indanhsach(t)