def xoakhoangtrang(s):
    s=s.strip()
    while '  ' in s:
        s=s.replace('  ',' ')
    return s

s = input()

print(xoakhoangtrang(s))