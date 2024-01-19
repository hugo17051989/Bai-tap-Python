try:
    with open('C:/Python/homework/013/input.inp', 'r', encoding='utf8') as fileInp:
        data = fileInp.readlines()
        srtingjoin = ' '.join(data).replace('\n', '')
        danhsach = srtingjoin.split()
        srtingjoin = ' '.join(danhsach)
    fileOut = open('C:/Python/homework/013/output.out', 'wb')
    fileOut.write(srtingjoin.encode('utf8'))
except:
    print('Lỗi đọc/ghi file')