def gioithieu(ten, tuoi):
    print('Xin chao! Toi ten la {}, toi {} tuoi.'.format(ten, tuoi))

ten = str(input())
tuoi = int(input())

if tuoi < 1:
    print('Vui long nhap tuoi la so nguyen duong')
else:
    gioithieu(ten, tuoi)