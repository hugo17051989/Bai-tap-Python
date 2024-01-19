with open('C:/Python/homework/012/input.inp', 'r', encoding='utf8') as fileInp:
    data = fileInp.readlines()
    srtingjoin = ' '.join(data).replace('\n', '')
fileOut = open('C:/Python/homework/012/output.out', 'wb')
fileOut.write(srtingjoin.encode('utf8'))