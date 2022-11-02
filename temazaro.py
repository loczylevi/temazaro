#                                    - Témazáró dolgozat [10_211102] -


"""
{1} Készíts egy programot, ami bekér egy szót és egy egész számot, majd
a bekért szót kiírja egymás mellé, szóközzel elválasztva annyiszor,
amennyi a szám volt! [5p]
"""
print("1. feladat:")

szo_bekeres = input("   írj be egy szót: ")
szam = int(input("   írj be egy számot: "))

[print(f"{szo_bekeres}",end=" ") for szo in range(szam)]


"""{2} Készíts egy programot, ami bekér 3 egész
számot majd ezek alapján meghatározza,
hogy szerkeszthető-e olyan háromszög,
aminek ezek a számok az oldalhosszai! [10p]"""

"""
- Ha a háromszög a szerkeszthető volt, akkor
határozd meg Héron képletének segítségével
a háromszög területét! [10p]"""


print("""2. feladat:
   Add meg a háromszög három oldalának hosszát cm-ben:""")
a = int(input("   a = "))
b = int(input("   b = "))
c = int(input("   c = "))


if a > b + c or b > a + c or c > a + b:
    print("   Ilyen háromszög nem szerkeszthető!")
else:
    s = (a + b + c) / 2
    t = (s * (s - a) * ( s - b) * (s - c)) ** 0.5
    print(f"   A háromszög területe: {t} cm^2")    


"""
{3} Készíts egy programot,
ami bekér egy nevet, egy maximálisan elérhető
pontszámot, és egy elért pontszámot! [5p]
- Ha az elért pontszám magasabb, mint a maximális
pontszám, akkor a program kiértékelés ne
folytatódjon, és írjunk
ki hibaüzenetet! [5p]
"""
osztalyzat = ""
print("3. feladat:")

print("   Add meg a tanuló következő adatait:")

nev = input("   név: ")
max_pont = int(input("   maximális pontszám: "))
elert = int(input("   elért pontszám: "))

if elert > max_pont:
    print("   Hibás adatokat adhattál meg, az elért pontszám nem lehet nagyobb, mint a maximális!")
else:
    szazalek = (elert / max_pont) * 100
    if szazalek < 51:
        osztalyzat = "elégtelen"
    elif 51 < szazalek < 65:
        osztalyzat = "elégséges"
    elif 65 < szazalek < 77:
        osztalyzat = "közepes"
    elif 77 < szazalek < 90:
        osztalyzat = "jó"
    elif szazalek > 90:
        osztalyzat = "jeles"
        
print(f"   {nev} {szazalek}%-ot ért el a dolgozaton, osztályzata: {osztalyzat}")

        
    
"""
{4} Írj egy programot, ami generál egymás után 5-ször 2 db,
kétjegyű véletlen egész számot. [5p]
- Minden iterációban írja ki a két szám összegét és különbségnek
abszolút értékét. [10p]
- Minden iterációban adj lehetőséget a felhasználónak megtippelni
, hogy mi volt az eredeti két szám (ügyelj rá, hogy
akkor is jó eredményt adjon, ha a két számot nem a generálás
sorrendjében adta meg a felhasználó!) [15p]
- A végén a program írja ki, hogy a felhasználónak hányszor
sikerült eltalálnia, hogy mi volt az eredeti két szám. [10p]
"""
print("4. feladat:")
import random
szamlalo = 1
helyes = 0
for kor in range(5):
    print(f"   {szamlalo}. kör:")
    a = random.randint(0,99)
    b = random.randint(0,99)
    ossz = abs(a + b)
    kivonas = abs(a - b)
    print(f"      a két szám összege {ossz}, különbsége {kivonas}. Mi lehet ez a két szám?")
    bekeres1 = int(input("        egyik szám: "))
    bekeres2 = int(input("        másik szám: "))
    if bekeres1 == a or bekeres1 == b and bekeres2 == a or bekeres2 == b:
        helyes += 1
        print("      Helyes!")
    else:
        print(f"      Sajnos nem, a válasz {a} és {b}")
    szamlalo += 1

print(f"   Végeztünk, helyes találataid száma: {helyes}")
        
    

