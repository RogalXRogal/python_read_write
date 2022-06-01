
plik = open("dane.txt", "r").read()
lines = plik.split("\n")

tablica = []

for line in lines:
    tablica.append(int(line))

tablica.sort(reverse = True)


plik2 = open("wynik.txt", "w")

for element in tablica:
    plik2.write(str(element) + "\n")

plik2.close()