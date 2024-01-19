def phanturieng(a,b):
    kq=[]
    for i in a:
        if i not in b:
            kq.append(i)
    for j in b:
        if j not in a:
            kq.append(j)
    return kq

a = input().split()
b = input().split()

print(*phanturieng(a,b))
