l = list(map(float, input().split()))
dem = 0

for i in range(1,len(l)):
    for j in range(i):
        if l[i]<l[j]:
            break
    else:
        dem += 1
print(dem)