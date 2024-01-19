a = input()
b = input()
person_a = a.split()
person_b = b.split()
if int(person_a[1]) < int(person_b[1]):
    print(person_b[0], 'cao hon', person_a[0])
elif int(person_a[1]) == int(person_b[1]):
    print('Ca hai cao bang nhau.')
else:
    print(person_a[0], 'cao hon', person_b[0])