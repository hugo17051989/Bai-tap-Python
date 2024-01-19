def demsokytu(s):
    chuoiktrunglap=''
    for i in s:
        if i not in chuoiktrunglap:
            chuoiktrunglap+=i
    kq={}
    for i in chuoiktrunglap:
        kq.update({i: s.count(i)})
    return kq

s=input()
print(demsokytu(s))
