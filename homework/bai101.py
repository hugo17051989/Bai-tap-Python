def tongptutuple(t):
    kq = tuple(sum(i) for i in t)
    return kq
try:
    n = int(input())
    listX=[]

    for _ in range(n):
        listcon = map(int, input().split())
        listX.append(tuple(listcon))
    tupleX=tuple(listX)
    print(tupleX)
    kq = tongptutuple(tupleX)
    print(kq)
except:
    print("Dinh dang dau vao khong hop le")
