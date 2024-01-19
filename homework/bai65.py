def tudainhat(s):
    a = s.split()
    kq = ''
    for i in a:
        if (len(i) > len(kq)) or (len(i) == len(kq) and i < kq):
            kq = i
    return kq

s = input()

print(tudainhat(s))