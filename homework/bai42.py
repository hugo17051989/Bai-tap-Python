def sosanh(a,b):
    person_a = a.split()
    person_b = b.split()
    if int(person_a[1])<0 or int(person_b[1])<0:
        print('Chieu cao phai lon hon 0')
    else:
        if int(person_a[1]) < int(person_b[1]):
            print(person_b[0], 'cao hon', person_a[0])
        elif int(person_a[1]) == int(person_b[1]):
            print('Ca hai cao bang nhau.')
        else:
            print(person_a[0], 'cao hon', person_b[0])

a = input()
b = input()

sosanh(a,b)
