def kieuchu(s):
    if len(s)==0:
        s= ''
    elif 65<ord(s[0])<90:
        s= s.upper()
    elif 97<ord(s[0])<122:
        s= s.lower()
    else: 
        s = s
    return s

s = input()

print(kieuchu(s))