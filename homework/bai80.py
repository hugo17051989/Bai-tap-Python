import math

def kiemtra_songuyento(n):
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
def insonguyento(s):
    for i in s:
        if i>0:
            if kiemtra_songuyento(i)== True:
                print(i, end=" ")
        
s = input().split()
if len(s)==0:
    print('Danh sach rong')
else:
    a = list(map(int,s))
    insonguyento(a)