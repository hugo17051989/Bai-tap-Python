n=int(input())
if n == 0 or n==1:
    print('Khong phai dang 2^k')
else:
    while n%2==0:
        n=n//2
    if n==1:
        print('So dang 2^k')
    else:
        print('Khong phai dang 2^k')