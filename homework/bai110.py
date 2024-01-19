def demsokytu(s):
    t = set(s)
    for i in t:
        print("'{}': {};".format(i, s.count(i)),end=' ')

s = input()
demsokytu(s)