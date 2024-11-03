from dane.koszt_rozbudowy import koszt_rozbudowy
from src.Gracz import Gracz
from src.Miasto import Miasto
from src.Wyspa import Wyspa


def main():
    siarka = Wyspa(23, 'siarka')
    kamienie = Wyspa(23, 'kamienie')
    siopalnia_karki = Miasto('siopalnia_karki', 308990, 20, siarka)
    rkasia = Miasto('rkasia', 308990, 20, siarka)
    kamulce = Miasto('kamulce', 308990, 20, kamienie)
    MaloKamulcy = Miasto('MaloKamulcy', 308990, 20, kamienie)
    AleLadnyKamien = Miasto('AleLadnyKamien', 308990, 20, kamienie)

    michal = Gracz([siopalnia_karki, kamulce, MaloKamulcy, AleLadnyKamien, rkasia])
    # print(produkcja(23, .2, .67, .4))
    for i in range(1, 20):
        michal.pusc_ture()
        print(michal.drewno)

if __name__ == "__main__":
    main()