def xoakytutrung(s):
    a = ''
    for c in s:
        if c not in a:
            a=a+c
    return a

s = input()

print(xoakytutrung(s))