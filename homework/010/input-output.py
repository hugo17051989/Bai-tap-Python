with open('C:/Python/homework/010/input.inp', 'r') as fileInp:
    ten = fileInp.readline().rstrip('\n')
    tuoihientai = int(fileInp.readline())
with open('C:/Python/homework/010/output.inp', 'w') as fileOut:
    fileOut.write('20 nam nua, tuoi cua {} hien tai la {}.'.format(ten, tuoihientai+20))