# Program na generoání obrázků pbm a ppm
# Autor: Petr Starý <staryp@jirovcovka.net>

def pbm(a):
    with open("arecibo10.pbm", "w") as vystup:
        #Určení rozměrů
        sirka = len(a[0]) * 10
        vyska = len(a) * 10
        vystup.write(f"P1\n{sirka} {vyska}\n")
        #Vykreslení obrázku
        for row in a:
            for _ in range(10):
                vystup.write(" ".join((char + " ") * 10 for char in row) + "\n")

def ppm(a):
    with open("arecibo.ppm", "w") as vystup:
        #Určení rozměrů
        sirka = len(a[0]) * 10
        vyska = len(a) * 10
        vystup.write(f"P3\n{sirka} {vyska}\n255\n")
        #Vykreslení výstupu podle barvy
        for row in a:
            for _ in range(10):
                for char in row:
                    if char == "0":
                        pixel = "0 0 0 "
                    elif char == "1":
                        pixel = "0 0 255 "
                    else:
                        pixel = "255 0 0 "
                    vystup.write(pixel * 10)
                vystup.write("\n")

#Načtení vstupu
with open("arecibo/obrazek.txt", "r") as vstup:
    arecibo = [radek.strip() for radek in vstup if radek.strip()]

pbm(arecibo)
ppm(arecibo)
