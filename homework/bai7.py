giatri1 = input()
giatri2 = input()
check = False
try:
    soA = float(giatri1)
    soB = int(giatri2)
    check = True
except:
    print('Dinh dang dau vao khong hop le')

if check: 
    print('{0:.{1}f}'.format(soA, soB))