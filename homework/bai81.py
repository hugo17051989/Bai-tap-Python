def listptduynhat(s):
    for i in s:
        if s.count(i)==1:
            print(i, end=' ')

s=input().split()
if len(s)==0:
    print('Danh sach rong')
else:
    listptduynhat(s)
