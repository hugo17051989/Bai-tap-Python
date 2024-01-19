def xoaptuset(s):
    t = s.copy()
    for i in s :
        if i.isdigit():
            t.remove(i)
    return t

a = set(input().split())
print(xoaptuset(a))