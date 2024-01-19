def danxenchuoi (s1,s2):
    s2=s2[::-1]
    kq = ''
    c = max(len(s1),len(s2))
    for i in range(c):
        if i<len(s1):
            kq = kq +s1[i]
        if i <len(s2):
            kq = kq +s2[i]
    return kq

s1 = input()
s2 = input()

print(danxenchuoi(s1,s2))