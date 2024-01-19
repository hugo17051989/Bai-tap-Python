def daytrungbinhcong(s):
    tbc = sum(s)/len(s)
    ds1 = []
    ds2 = []
    for i in range(len(s)):
        if s[i]<tbc:
            ds1.append(s[i])
        else:
            ds2.append(s[i])
    return tbc, ds1, ds2

s = input().split()
t = list(map(float,s))
a,b,c = daytrungbinhcong(t)
print(a)
print(*b)
print(*c)
