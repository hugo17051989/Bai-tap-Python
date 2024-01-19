a = list(map(int,input().split()))
gtmax = None
for i in a:
    if gtmax==None or gtmax<i:
        gtmax=i
print(gtmax)