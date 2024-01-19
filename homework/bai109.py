def kiemtratapcon(s1,s2):
    if s2 <= s1:
        return True
    else:
        return False

s1 = set(input().split())
s2 = set(input().split())

print(kiemtratapcon(s1,s2))