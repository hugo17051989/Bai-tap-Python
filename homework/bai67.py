def xoakhoangtrangthua(s):
    s=s.strip()
    while '  ' in s:
        s=s.replace('  ',' ')
    return s

def cangiua(s):
    a = s.split('.')
    dodai = 0
    for i in a:
        i = xoakhoangtrangthua(i)
        if dodai<len(i):
            dodai=len(i)
    for i in a:
        i = xoakhoangtrangthua(i)
        print(i.center(dodai))

s = input()
cangiua(s)
    