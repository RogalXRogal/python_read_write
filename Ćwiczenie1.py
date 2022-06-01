
plik = open("promienie.txt")

a = plik.read(1)
b = plik.read(2)

a = int(a)
b = int(b)

pole1 = 3.14 * a * a 
pole2 = 3.14 * b * b

if pole1 < pole2:
    plik2 = open("wyniki.txt", "w")
    pole1 = str(pole1)
    plik2.write(pole1)
    plik2.write("\n")
    pole2 = str(pole2)
    plik2.write(pole2)
    plik2.close()

else:
    plik2 = open("wyniki.txt", "w")
    pole1 = str(pole2)
    plik2.write(pole2)
    plik2.write("\n")
    pole2 = str(pole1)
    plik2.write(pole1)
    plik2.close()


plik.close()