l = input().split()
so = None
chuoi = None
for i in range(len(l)):
    if l[i].isnumeric():
        l[i]=int(l[i])
        if so==None or so>l[i]:
            so=l[i]
    else:
        if chuoi == None or len(chuoi)<len(l[i]):
            chuoi = l[i]

print(chuoi,so)
