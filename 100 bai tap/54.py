l = list(map(int, input().split()))
a = int(input())
b = int(input())
if a<b<len(l):
    gtmin = None
    for i in l[a:b]:
        if gtmin==None or gtmin>i:
            gtmin=i
    print(gtmin)
else:
    print('Vui long nhap a<b<chieu dai list')