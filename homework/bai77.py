def timphantule(s):
    a = s.split()
    if len(a)==0:
        return print('Danh sach rong')
    else:
        for i in a:
            if float(i) % 2 == 1:
                print(i, end=' ')

s = input()
timphantule(s)

