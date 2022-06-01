
plik = open("dane.txt", "r").read()

tablica = []

lines = plik.split("\n")

for line in lines:
    tablica.append(int(line))
    
a = tablica[0]
b = tablica[1]
c = tablica[2]
d = tablica[3]
e = tablica[4]

a = a % 10
b = b % 10
c = c % 10
d = d % 10
e = e % 10

print(a, b, c, d, e)




plik2 = open("wyniki.txt", "w")

if a == 0 or a == 3 or a == 8 or a == 9:
    plik2.write(str(a))
    plik2.write("\n")

if b == 0 or b == 3 or b == 8 or b == 9:
    plik2.write(str(b))
    plik2.write("\n")

if c == 0 or c == 3 or c == 8 or c == 9:
    plik2.write(str(c))
    plik2.write("\n")

if d == 0 or d == 3 or d == 8 or d == 9:
    plik2.write(str(d))
    plik2.write("\n")

if e == 0 or e == 3 or e == 8 or e == 9:
    plik2.write(str(e))
    plik2.write("\n")
    plik2.close()
 





