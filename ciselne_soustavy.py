#Převody číselných soustav
#Autor: Petr Starý <staryp@jirovcovka.net>

def prevod_cisla(zaklad: int, cislo: int):
    znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if zaklad < 2 or zaklad > 62:
        print("Základ soustavy musí být mezi 2 a 62.")
        exit(0)

    if cislo == 0:
        return "0"

    # Uchování si znaménka
    znamenko = "" if cislo > 0 else "-"
    cislo = abs(cislo)
    vysledek = ""

    # Získávání zbytků
    while cislo > 0:
        vysledek = znaky[cislo % zaklad] + vysledek
        cislo //= zaklad

    return znamenko + vysledek


# Načtení vstupních dat
f = open("vstup.dat", "r")
zaklad = int(f.readline().strip())
cislo = int(f.readline().strip())

# Výpočet a výpis výstupu
vysledek = prevod_cisla(zaklad, cislo)
print(vysledek)
