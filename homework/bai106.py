def kiemtrachan(s):
    if len(s)%2==0:
        s.clear()
    return s

s=set(input().split())
print(kiemtrachan(s))
