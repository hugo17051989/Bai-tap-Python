n = int(input())

if n < 0:
    print("Vui long nhap so tu nhien")
else:
    maASCII = 65
    for i in range(n):
        khoangtrang = ' '*(2*(n-i)-1)
        print(khoangtrang, end="")
        for j in range(2*i+1):
            print(chr(maASCII), end=' ')
            maASCII+= 1
            if chr(maASCII) > 'Z':
                maASCII = 65
        print()
