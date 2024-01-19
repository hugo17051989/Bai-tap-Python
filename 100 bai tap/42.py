s1=1
s2=1
fibo=0
n=int(input())
if n>=2:
    while fibo<=n:
        fibo=s1+s2
        s1=s2
        s2=fibo
    print(s1)
elif n==1:
    print(1)
else:
    print('Vui long nhap so lon hon 0')

