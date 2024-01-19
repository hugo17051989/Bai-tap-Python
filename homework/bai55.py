def daochuoicon(s,a,b):
    n=s[a:b+1]
    s1=n[::-1]
    return print(s1)

a=input()
b,c=map(int, input().split())

if b<0 or c<0:
    print('Vui long nhap so tu nhien')
elif b>len(a) or c>len(a):
    print('a,b lon hon do dai chuoi')
elif b>c:
    print('Vui long nhap a<=b')
else:
    daochuoicon(a,b,c)
