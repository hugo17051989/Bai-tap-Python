def tinhtong(*args):
    s=0
    for i in args:
        s+=i
    return s

print('1 + 2 + 3 = {}'.format(tinhtong(1,2,3)))
print('1 + 2 + 3 + 4 + 5 = {}'.format(tinhtong(1,2,3,4,5)))

