a = input()
b = input()    
person_a = a.split()
person_b = b.split()
check = False

try:
    height_a = int(person_a[1])
    height_b = int(person_b[1])
    check = True

except:
    print('Du lieu nhap khong hop le')

if check:
    if height_a <= 0 or height_b <= 0:
        print("Chieu cao phai lon hon 0")
    elif height_a < height_b:
        print(person_b[0], 'cao hon', person_a[0])
    elif height_a == height_b:
        print('Ca hai cao bang nhau.')
    else:
        print(person_a[0], 'cao hon', person_b[0])