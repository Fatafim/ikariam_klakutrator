from icecream import ic

from dane.koszt_rozbudowy import koszt_rozbudowy
from src.produkcja import produkcja, produkcja_bez_bonusów
def kamien(lvl):
    kamulce = produkcja(lvl, 0.2, 0.67, 0.44)
    MaloKamulcy = produkcja(lvl, 0.2, 0.67, 0.42)
    AleLadnyKamien = produkcja(lvl, 0.2, 0.67, 0.42)

    razem = kamulce+AleLadnyKamien+MaloKamulcy
    # ic(kamulce, MaloKamulcy, AleLadnyKamien, razem)

    Miasto = produkcja(lvl, 0.2, 0.67, 0.44)
    TrybunalKamienia = produkcja(lvl, 0.2, 0.67, 0.46)
    Jeremiasz = produkcja(lvl, 0.2, 0.67, 0.4)
    Hlep = produkcja(lvl, 0.2, 0.67, 0.46)
    razem_2 = Miasto + TrybunalKamienia + Jeremiasz + Hlep
    # ic(Miasto, TrybunalKamienia, Jeremiasz, Hlep, razem_2)
    # print("cala wyspa kamienia: ", razem+razem_2)
    return razem + razem_2

def wino(lvl):
    Niwo = produkcja(lvl, 0.2, 0.67, 0.4)
    Wiwo = produkcja(lvl, 0.2, 0.67, 0.38)

    Golden = produkcja(lvl, 0.2, 0.67, 0.36)
    Montelago = produkcja(lvl, 0.2, 0.67, 0.36)

    # ic(Niwo, Wiwo, Niwo+Wiwo)
    # ic(Golden, Montelago, Golden+Montelago)

    return Niwo+Wiwo+Golden+Montelago

#  kamien bez rozbudowy wino bez rozbudowy

k1 = kamien(28)
w1 = wino(25)

#  kamien z rozbudowa wino z rozbudowa
k2 = kamien(29)
w2 = wino(26)

print(f"Kamien: {k1}, wino: {w1}")
print(f"Obecna produkcja łącznie na winie i kamieniu (łącznie obie wyspy): {k1+w1}")
print(f"Rozbudowa tylko kamienia (łącznie obie wyspy): {k2+w1}")
print(f"Rozbudowa tylko wina (łącznie obie wyspy): {k1+w2}")

zk = k2-k1
zw = w2-w1
print(f"Zysk z rozbudowy tylko kamienia: {zk}")
print(f"Zysk z rozbudowy tylko wina: {zw}")
print(f"Różnica: {zk-zw}")

print("\n****************\n")

print("Koszt rozbudowy na 29lvl", koszt_rozbudowy[29-2])
print("Koszt rozbudowy na 26lvl", koszt_rozbudowy[26-2])
print(f"Różnica: {koszt_rozbudowy[29-2]-koszt_rozbudowy[26-2]}")

print("\n****************\n")

print(f"Produktywność:")
pk = zk/koszt_rozbudowy[29-2]
pw = zw/koszt_rozbudowy[26-2]
print(f"Rozbudowa kamienia: {pk}")
print(f"Rozbudowa wina: {pw}")

print("\nBardziej opłaca się: ")
print("Kamień" if pk > pw else "Wino")