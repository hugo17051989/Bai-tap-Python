n = input()
inhoa=0
inthuong=0
so=0
for i in n:
    if i.isupper():
        inhoa+=1
    if i.islower():
        inthuong+=1
    if i.isdigit():
        so+=1
print(inhoa,inthuong,so)