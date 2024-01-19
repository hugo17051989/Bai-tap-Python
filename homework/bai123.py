def gomnhomtu(s):
    kq={}
    for i in s:
        if i not in kq:
            kq[i]=[i]
        else:
            kq[i].append(i)
    return kq

s = input().split()
print(gomnhomtu(s))