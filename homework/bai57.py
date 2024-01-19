def thaythechuoi(s):
    n = len(s)
    t = s[-3:]
    kq = ''
    if n>=3 and t == 'ing':
        kq=s[0:-3]+'ly'
    else:
        kq=s+'ing'
    return kq

s = input()

print(thaythechuoi(s))