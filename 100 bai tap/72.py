l = input().split()
vtmax= None
for i in l:
    for j in range(len(i)):
        if vtmax==None or i[j].isupper() and vtmax<i.index(i[j]):
            vtmax = i.index(i[j])
            kq=l.index(i)
print(kq)
