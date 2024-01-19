a = input()
b = a
for i in a:
    if i.isalpha():
        b = b.replace(i, ' ')
ds = b.split()
ds = list(map(int, ds))
print(sum(ds))
