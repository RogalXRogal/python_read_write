plik = open("dane.txt", "r").read()

tablica =[]

lines = plik.split("\n")

for line in lines:
    a = tablica.append(line)

def suma_10(liczba):
    while liczba > 10:
        wynik = 0
        for znak in str(liczba):
            wynik+=int(znak)
        liczba = wynik
    return liczba

def suma_100(liczba):
    while liczba > 100:
        wynik = 0
        for znak in str(liczba):
            wynik+=int(znak)
        liczba = wynik
    return liczba

plik2 = open("wynik.txt", "w")

a = tablica[0]
b = tablica[1]
c = tablica[2]
d = tablica[3]

a = suma_10(int(a))
b = suma_10(int(b))
c = suma_10(int(c))
d = suma_10(int(d))


plik2.write(str(a))
plik2.write("\n")
plik2.write(str(b))
plik2.write("\n")
plik2.write(str(c))
plik2.write("\n")
plik2.write(str(d))





plik2.close()