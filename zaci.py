#Progam na práci se seznamem studentů
#Autor: Petr Starý <staryp@jirovcovka.net>

file = open("zaci.txt","r")
data = []

#P5edpokládejme, že jméno s maximální četností a student s nejvíce jmény jsou unikátní
maximalni_pocet = 0 #Nejčastější jméno - počet
nejvice_jmen = 0 #Nejvíce křestních jmen - počet
zak_max_jmen = None #Nejvíce křestních jmen
maximalni_jmeno = None #Nejčastější jméno
krestni_jmena = [] #Ukládání všech křestních jmen

#Načtení vstupu
for line in file:
    data.append(line)


for radek in data:
    radek = radek.split()

    #Tisk křestních jmen
    print("*",end=" ")
    for i in range(len(radek)-1):
        print(radek[i],end = " ")
        krestni_jmena.append(radek[i])
    print("*", end=" ")
    #Tisk příjmení
    print(f"- {radek[-1]} -")

    #Kontrola na počet křestních jmen. Nepočítáme do počtu příjmení
    if len(radek)-1 > nejvice_jmen:
        nejvice_jmen = len(radek)-1
        zak_max_jmen = radek

#Získaní unikátních jmen pro určení počtů
unikaty = set(krestni_jmena)

for jmeno in unikaty:
    pocet = krestni_jmena.count(jmeno) #Počet výskytů jména

    if pocet > maximalni_pocet:
        maximalni_pocet = pocet
        maximlani_jmeno = jmeno

#Výpis dvou údajů
print(f"Nejčastější jméno je {maximlani_jmeno} s četností {maximalni_pocet}.")

print(f"Nejvíce křestních jmen má {' '.join(zak_max_jmen)} s {nejvice_jmen} křestními jmény.")
