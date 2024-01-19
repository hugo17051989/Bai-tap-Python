n = int(input())
max=None
min=None

while n!=-1:
    if max==None or max<n:
        max=n
    if min ==None or min>n:
        min=n
    n=int(input())

print(max)
print(min)