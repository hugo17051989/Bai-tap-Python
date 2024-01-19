l = list(map(int, input().split()))
kt = True
for i in l:
    if l[0]!=l[i]:
        kt=False
print(kt)