def demsotu(s):
    kq = 0
    a = s.split()
    for c in a:
        checkso=False
        checkkytu=False
        for i in c:
            if i.isalpha():
                checkkytu = True
            if i.isdigit():
                checkso = True
        if checkkytu and checkso:
            kq +=1
    return kq

s = input()
print(demsotu(s))