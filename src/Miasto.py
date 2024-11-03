import inspect

from src.produkcja import produkcja


class Miasto:
    def __init__(self, id, drewno, lvl_lesniczowki, wyspa, bonusy: dict):
        self.id = id
        self.drewno = drewno
        self.lvl_lesniczowki = lvl_lesniczowki
        self.wyspa = wyspa
        self.bonusy = bonusy[id]

        self.wyspa.przypisz_miasto(self)


    def pusc_ture(self):
        self.produkuj()

    def produkuj(self):
        wyprodukowano = produkcja(self.wyspa.lvl_tartaka, self.lvl_lesniczowki*2/100, *self.bonusy)
        self.drewno += wyprodukowano
        return wyprodukowano