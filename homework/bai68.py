def xoakytutrung(s):
    a = ''
    for c in s:
        if c not in a:
            a=a+c
    return a

def demsokytu(s):
    a = xoakytutrung(s)
    for c in a:
        if c in s:
            print("'",c,"': ",s.count(c) ,';',end=' ')

s = input()
demsokytu(s)