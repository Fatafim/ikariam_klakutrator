import random

from dane.koszt_rozbudowy import koszt_rozbudowy
from src.produkcja import czas_rozbudowy


class Wyspa:
    def __init__(self, lvl_tartaka, id, ):
        self.lvl_tartaka = lvl_tartaka
        self.id = id
        self.koszt_rozbudowy = koszt_rozbudowy[self.lvl_tartaka-1]
        self.w_rozbudowie = False
        self.pozostaly_czas = None
        self.miasta = []

    def rozbuduj_tartak(self):
        self.w_rozbudowie = True
        self.pozostaly_czas = czas_rozbudowy(self.lvl_tartaka-1)

    def buduj_tartak(self):
        if self.w_rozbudowie:
            self.pozostaly_czas -= 1
            if self.pozostaly_czas == 0:
                self.w_rozbudowie = False
                self.lvl_tartaka += 1
                self.koszt_rozbudowy = koszt_rozbudowy[self.lvl_tartaka - 1]

    def podejmij_decyzje(self):
        if random.choice([True, False]):
            self.rozbuduj_tartak()

    def pusc_ture(self):
        # self.podejmij_decyzje()
        self.buduj_tartak()

    def przypisz_miasto(self, miasto):
        self.miasta.append(miasto)

    def calkowita_produkcja(self):
        drewno = 0
        for miasto in self.miasta:
            drewno += miasto.produkuj()
        return drewno