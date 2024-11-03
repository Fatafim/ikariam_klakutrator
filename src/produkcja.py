import math

from dane.workers import workers

def produkcja_podstawowa(lvl):
    # print(workers[lvl-1])
    return workers[lvl-1] * 1.35


def produkcja_dodatkowa(lvl):
    # z technokracją
    return round((round(workers[lvl-1], 0) / 2) * (0.25*1.35*1.2), 2)


def produkcja_bez_bonusów(lvl):
    return produkcja_podstawowa(lvl) + produkcja_dodatkowa(lvl)


def produkcja(lvl, *args):
    # print("Bonusy:")
    # print(args)
    # print([produkcja_bez_bonusów(lvl) * i for i in args])
    # print("Suma: ")
    # print(sum([produkcja_bez_bonusów(lvl) * i for i in args]))
    return produkcja_bez_bonusów(lvl) + sum([produkcja_bez_bonusów(lvl) * i for i in args])


def czas_rozbudowy(lvl):
    return math.ceil(((7200 * (1.1 ** lvl)) - 7200) / 3600)