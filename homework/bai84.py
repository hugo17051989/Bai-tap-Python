def timphantulonnhat(s):
    a = max(s)
    print(a)
    b = s.count(a)
    print(b)
    for i in range(len(s)):
        if s[i]==a:
            print(i,end=" ")

s = input().split()
if len(s)==0:
    print('Danh sach rong')
else:
    a = list(map(float,s))
    timphantulonnhat(a)
