print('Nhap so thap phan :')
giatri = input()
isParseDone = False
try:
    sotp = int(giatri)
    isParseDone = True
except:
    print('Dinh dang dau vao khong hop le')
if isParseDone:        
    print('So thap phan %d trong he bat phan la %o' % (sotp, sotp))