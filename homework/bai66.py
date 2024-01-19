def xoakhoangtrangthua(s):
    s=s.strip()
    while '  ' in s:
        s=s.replace('  ',' ')
    return s

def xulychuoi(s):
    a = s.split('.')
    for i in a:
        i = xoakhoangtrangthua(i)
        print(i.title())

s = input()
xulychuoi(s)