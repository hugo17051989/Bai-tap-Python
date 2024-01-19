def capnhatset(s,l):
    for i in l:
        s.add(i)
    return s

s = set(input().split())
l = input().split()
print(capnhatset(s,l))
