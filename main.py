import random

sorozat = [-3, 5, 11, -2, 4]

def kiir(szoveg, sep=" "):
    i = 0
    szamsor = ""
    while(i < len(sorozat)):
        szamsor = szamsor + sep+str((sorozat[i]))
        i += 1
    print(f'{szoveg}{szamsor}')


def veletlen():
    vel = int(random.random() * 7)+5
    sorozat[0] += vel
    kiir("Első elem módosítása után: ", "#")

def beker():
    szam = int(input('Adj meg egy páratlan hárommal osztható kétjegyű számot : '))
    while ((szam % 3 != 0) or (szam % 2 ==0) or (szam < 10)):
        szam = int(input('Adj meg egy páratlan hárommal osztható kétjegyű számot : '))
    return szam

def masodik_feladat():
    szam = beker()
    utolso = len(sorozat)-1
    sorozat[utolso] = szam
    kiir("Utolsó elem módosítása után: ", "#")

def harmadik_feladat():
    kiir("Szóközzel kiírva: ", " ")

def ketjegyu():
    i = 0
    while (sorozat[i] < 10):
        i += 1
    if (i==len(sorozat) or sorozat[i] > 9):
        print(f'Az első kétjegyű érték: {i+1}. elem: {sorozat[i]}')
    else:
        print('Nem tartalmaz kétjegyű számot')

def prim(ertek):
    k = 2
    prima = True
    if abs(ertek) == 2:
        prima = False
    while(k < ertek-1):
        if (ertek % k == 0):
           prima = False
        k += 1
    return prima

def otodik_feladat():
    i = 0
    db = 0
    while (i < len(sorozat)):
        if prim(sorozat[i]):
            db += 1
        i += 1
    if (db != 0):
        print(f'{db} darab prím szám van a sorozatban.')
    else:
        print('Nem tartalmaz prím számot a sorozat')

kiir("A tömb elemei: " , "#")
veletlen()
masodik_feladat()
harmadik_feladat()
ketjegyu()
otodik_feladat()

