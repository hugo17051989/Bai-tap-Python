def phanturieng(s1,s2):
    a = s1-s2
    b = s2-s1
    return a,b

s1 = set(input().split())
s2 = set(input().split())

a,b = phanturieng(s1,s2)
print(a)
print(b)

