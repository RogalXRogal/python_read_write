
plik = open("dane.txt", "r")

a = int(plik.read(1))
b = int(plik.read(2))
h = int(plik.read(3))


pole = ((a + b) *h)/2

pole = str(pole)

plik2 = open("pole.txt", "w")

plik2.write(pole)
plik2.close()



plik.close()
