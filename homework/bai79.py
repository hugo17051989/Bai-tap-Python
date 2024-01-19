def sapxep(s):
    for i in range(len(s)):
        gtmin = i
        for j in range(i+1, len(s)):
            if s[gtmin]>s[j]:
                gtmin = j
        s[i], s[gtmin] = s[gtmin], s[i]
    return s

s = input().split()
if len(s) == 0:
    print('Danh sach rong')
else:
    a = list(map(float, s))
    print(*sapxep(a))