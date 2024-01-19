def xulychuoi(s):
    kq = ''
    chu = 0
    chu1 = ''
    so = 0
    so1 = ''
    kyhieu = 0
    kyhieu1 = ''
    for c in s:
        if c.isalnum():
            if c.isalpha():
                chu=chu+1
                chu1=chu1+c
            elif c.isnumeric():
                so=so+1
                so1=so1+c
        else:
            kyhieu=kyhieu+1
            kyhieu1=kyhieu1+c
    kq = so1+chu1+kyhieu1
    return so,chu,kyhieu,kq

s = input()
a,b,c,d = xulychuoi(s)
print(a)
print(b)
print(c)
print(d)