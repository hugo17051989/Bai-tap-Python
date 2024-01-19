def thaythenguyenam(s):
    t = 'AaEeOoIiUu'
    kq=0
    for c in t:
        kq += s.count(c)
        s=s.replace(c,'$')
    return print(kq,'\n',s)

s = input()
thaythenguyenam(s)