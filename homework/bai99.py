def demkytu0(t):
    a = t.count('0')
    kq = []
    for i in t:
        b=i.count('0')
        kq.append(b)
    return print((a,sum(kq)))

t = tuple(input().split())
demkytu0(t)