def xoachuoichanle(s):
    kq=''
    if len(s)%2==0:
        for i in range(len(s)):
            if i%2==1:
                kq = kq+s[i]
    else:
        for i in range(len(s)):
            if i%2==0:
                kq = kq+s[i]
    return kq

s = input()

print(xoachuoichanle(s))