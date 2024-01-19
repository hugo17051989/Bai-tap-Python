def nhanbandanhsach(s,n):
    solanlap = n//len(s)
    print(*s*solanlap+s[0:n-(solanlap*len(s))])

s = input().split()
if len(s)==0:
    print('Danh sach rong')
else:
    n = int(input())
    nhanbandanhsach(s,n)