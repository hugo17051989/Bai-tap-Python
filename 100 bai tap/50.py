a = input()
kiemtradodai = len(a)>6
kiemtradacbiet = False
kiemtrathuong = False
kiemtrainhoa = False
kiemtraso = False

for i in a:
    if i.isdigit():
        kiemtraso = True
    elif i.islower():
        kiemtrathuong = True
    elif i.isupper():
        kiemtrainhoa = True
    else:
        kiemtradacbiet = True

if kiemtradodai and kiemtradacbiet and kiemtraso and kiemtrathuong and kiemtrainhoa:
    print('Day la chuoi mat khau manh')
else:
    print('Day la mat khau khong manh')
