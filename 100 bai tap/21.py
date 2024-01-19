ngay = int(input())
thang = int(input())

if thang <=8:
    sothang30ngay=(thang-1)//2
    sothang31ngay=thang//2
else:
    sothang30ngay=thang//2-1
    sothang31ngay=(thang+1)//2

kq=ngay + sothang30ngay*30 + sothang31ngay*31 - 1
if thang>2:
    kq=kq-2
print(kq)