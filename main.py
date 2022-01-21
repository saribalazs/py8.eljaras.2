'''
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
'''
def ellenorzes():
    if num == 0:
        return "Az ön által megadott szám nulla!"
    elif num > 0:
        return "Az ön által megadott szám pozitív!"
    else:
        return "Az ön által megadott szám negatív"

num = int(input("Kérem adjon meg egy számot!"))
print(ellenorzes())