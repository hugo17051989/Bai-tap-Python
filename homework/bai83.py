def chenvitri(s,n):
    t=[]
    for i in range(0,len(s),n):
        t.extend(s[i:i+n])
        t.append('kteam')
    t.pop()
    return print(*t)

s = input().split()
if len(s)==0:
    print('Danh sach rong')
n = int(input())
if n <=0:
    print('Du lieu nhap khong hop le')
else:
    chenvitri(s,n)
