n = int(input())
sochan=0
sole=0

while n>0:
    tam = n%10
    if tam%2==0:
        sochan+=1
    else:
        sole+=1
    n=n//10

print(sochan,sole)