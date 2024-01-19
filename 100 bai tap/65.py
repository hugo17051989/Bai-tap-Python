l = list(map(float, input().split()))

for i in range(1,len(l)-1):
    if (l[i-1]<l[i] and l[i]>l[i+1]) or (l[i-1]>l[i] and l[i]<l[i+1]):
        print('True')
        break
else:
    print('False')