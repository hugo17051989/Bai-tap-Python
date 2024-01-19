def kiemtradanhsachgiam(a):
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            return False
    return True
    
s = input().split()
a = list(map(float,s))
if len(s)==0:
    print('Danh sach rong')
else:
    print(kiemtradanhsachgiam(a))
