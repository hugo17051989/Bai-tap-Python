a = input()
b = input()
print(a)
print(b)
vtdau = 0
vtcuoi = len(b)
while vtcuoi<=len(a):
    if a[vtdau:vtcuoi]==b:
        a=a[:vtdau]+a[vtcuoi:]
    vtdau+=1
    vtcuoi+=1
print(a)