def kiemtrachuoi(a,b):
    if b in a:
        print(a.count(b))
    else:
        print('Chuoi {} khong nam trong chuoi {}'.format(b,a))

a = input()
b = input()

kiemtrachuoi(a,b)