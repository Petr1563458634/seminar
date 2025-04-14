#Program na analýzu hry
#Autor: Petr Starý <staryp@jirovcovka.net>

filename = "data.csv"
pocet_kol = 0
# Uložení dvojic pro maximum/průměr a jméno
maximum = [0, None]
prumer = [0, None]

vysledky = {}

with open(filename, "r", encoding="UTF-8") as soubor:
    for line in soubor:
        line = line.strip() # zbavuji se konce řádku \n
        jmeno, cislo = line.split(";") # rozděluji řádek podle ;
        cislo = float(cislo)  # převedení řetězce na číslo typu float

        pocet_kol += 1
        if jmeno not in vysledky.keys():
            vysledky[jmeno] = [cislo, 1] #Uchování výhry a počtu kol, kde hráč vyhrál
        else:
            vysledky[jmeno] = [vysledky[jmeno][0] + cislo, vysledky[jmeno][1] + 1]

    # vypis slovníku
    print("\n Jméno              Body            Vyhraných kol")
    for jmeno,vysledek in vysledky.items():
        body, vyhry = vysledek[0], vysledek[1]
        print(f"{jmeno:20} {body:10.2f} {vyhry:12}")

        # Update maxima, popřípadě průměru
        if body > maximum[0]:
            maximum = [body, jmeno]
        if body/vyhry > prumer[0]:
            prumer = [body/vyhry, jmeno]
    print("Počet hráčů: ", len(vysledky))

    print(f"Počet odehrných kol byl {pocet_kol}.")
    print(f"Nejvíce bodů, {maximum[0]:.2f}, získal {maximum[1]}.")
    print(f"Průměrně na počet vyhraných kol získal nejvíce {prumer[1]}, a to {prumer[0]:.2f}.")
