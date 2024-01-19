try:
    with open('C:/Python/homework/011/input.inp', 'r', encoding='utf8') as fileInp:
        ten = fileInp.readline().rstrip('\n')
        tuoihientai = int(fileInp.readline())
    with open('C:/Python/homework/011/output.inp', 'wb') as fileOut:
        string = '20 năm nữa, tuổi của {} hiện tại là {}.'.format(ten, tuoihientai+20)
        fileOut.write(string.encode('utf8'))
except FileNotFoundError:
    print('Không tìm thấy file')
except FileExistsError:
    print('Exist Error')
except:
    print('Dinh dang file khong hop le')