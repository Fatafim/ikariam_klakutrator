from dane.koszt_rozbudowy import koszt_rozbudowy
from src.Gracz import Gracz
from src.Miasto import Miasto
from src.Wyspa import Wyspa
bonusy_stale_michal = [0.2, 0.67]
bonusy_stale_bartek = bonusy_stale_michal
bonusy = {
    'Michal': {
        'kamulce': bonusy_stale_michal,
        'MaloKamulcy': bonusy_stale_michal,
        'AleLadnyKamien': bonusy_stale_michal,
        'Niwo': bonusy_stale_michal,
        'Wiwo': bonusy_stale_michal,
        'Szryktaly': bonusy_stale_michal,
        'Szkyrtaly': bonusy_stale_michal,
        'SiopalniaKarki': bonusy_stale_michal,
        'Rkasia': bonusy_stale_michal,
    },
    'Bartek':{
        'Hlep': [0.2],
        'Jeremiasz': [0.2],
        'TrybunalKamienia': [0.2],
        'miasto': [0.2],
        'Skarpeta': bonusy_stale_bartek,
        'GoldenSzczoch': bonusy_stale_bartek,
        'Montelago': bonusy_stale_bartek,
        'D_Day': bonusy_stale_bartek
    }

}
def scenariusz(lvl_kamien, lvl_wino, lvl_krysztal, lvl_siarka):
    wino = Wyspa(lvl_wino, 'wino')
    kamienie = Wyspa(lvl_kamien, 'kamienie')
    krysztaly = Wyspa(lvl_siarka, 'krysztaly')
    siarka = Wyspa(lvl_krysztal, 'siarka')

    SiopalniaKarki = Miasto('SiopalniaKarki', 308990, 20, siarka, bonusy=bonusy['Michal'])
    Rkasia = Miasto('Rkasia', 308990, 18, siarka, bonusy=bonusy['Michal'])

    Niwo = Miasto('Niwo', 308990, 20, wino, bonusy=bonusy['Michal'])
    Wiwo = Miasto('Wiwo', 308990, 20, wino, bonusy=bonusy['Michal'])

    Szryktaly = Miasto('Szryktaly', 308990, 17, krysztaly, bonusy=bonusy['Michal'])
    Szkyrtaly = Miasto('Szkyrtaly', 308990, 17, krysztaly, bonusy=bonusy['Michal'])

    kamulce = Miasto('kamulce', 308990, 22, kamienie, bonusy=bonusy['Michal'])
    MaloKamulcy = Miasto('MaloKamulcy', 308990, 21, kamienie, bonusy=bonusy['Michal'])
    AleLadnyKamien = Miasto('AleLadnyKamien', 308990, 21, kamienie, bonusy=bonusy['Michal'])



    Hlep = Miasto('Hlep', 308990, 24, kamienie, bonusy=bonusy['Bartek'])
    Jeremiasz = Miasto('Jeremiasz', 308990, 22, kamienie, bonusy=bonusy['Bartek'])
    TrybunalKamienia = Miasto('TrybunalKamienia', 308990, 23, kamienie, bonusy=bonusy['Bartek'])
    miasto = Miasto('miasto', 308990, 20, kamienie, bonusy=bonusy['Bartek'])

    GoldenSzczoch = Miasto('GoldenSzczoch', 308990, 22, wino, bonusy=bonusy['Bartek'])
    Montelago = Miasto('Montelago', 308990, 21, wino, bonusy=bonusy['Bartek'])

    Skarpeta = Miasto('Montelago', 308990, 18, siarka, bonusy=bonusy['Bartek'])

    D_Day = Miasto('D_Day', 308990, 16, krysztaly, bonusy=bonusy['Bartek'])

    Michal = Gracz([SiopalniaKarki, kamulce, MaloKamulcy, Niwo, AleLadnyKamien, Szryktaly, Wiwo, Szkyrtaly, Rkasia])
    Bartek = Gracz([Hlep, Jeremiasz, TrybunalKamienia, miasto, GoldenSzczoch, Montelago, Skarpeta, D_Day])

    print(f"{Hlep.produkuj()=}")
    print(f"{Jeremiasz.produkuj()=}")
    print(f"{TrybunalKamienia.produkuj()=}")
    print(f"{miasto.produkuj()=}")
    print(f"{GoldenSzczoch.produkuj()=}")
    print(f"{Montelago.produkuj()=}")
    print(f"{Skarpeta.produkuj()=}")
    print(f"{D_Day.produkuj()=}")

    print("\n****************\n")

    print(f"{Michal.przelicz_drewno()=}")
    print(f"{Bartek.przelicz_drewno()=}")
    print("\n****************\n")
    result = Michal.przelicz_drewno()+Bartek.przelicz_drewno()
    print(f"Całkowite drewno: {result}")
    return result

lvl_siarka = 22
lvl_krysztal = 24
lvl_kamien = 29
lvl_wino = 26

podstawka = scenariusz(lvl_kamien, lvl_wino, lvl_krysztal, lvl_siarka)
roz_krysztal = scenariusz(lvl_kamien, lvl_wino, lvl_krysztal+1, lvl_siarka)
roz_kamien = scenariusz(lvl_kamien+1, lvl_wino, lvl_krysztal, lvl_siarka)
roz_siarka = scenariusz(lvl_kamien, lvl_wino, lvl_krysztal, lvl_siarka+1)
roz_wino = scenariusz(lvl_kamien, lvl_wino+1, lvl_krysztal, lvl_siarka)

import pandas as pd

results = pd.DataFrame({
    "Rozbudowa siarki": roz_siarka - podstawka,
    "Rozbudowa krysztal": roz_krysztal - podstawka,
    "Rozbudowa wino": roz_wino - podstawka,
    "Rozbudowa kamien": roz_kamien - podstawka,
}, index=["Zysk/h"]).T

results.loc[:, "Koszt"] = [koszt_rozbudowy[lvl_siarka-2], koszt_rozbudowy[lvl_krysztal-2], koszt_rozbudowy[lvl_wino-2], koszt_rozbudowy[lvl_kamien-2]]
results.loc[:, "Produktywnosc"] = results["Zysk/h"] / results["Koszt"]

print(results)
print("Najbardziej efektywna kosztowo jest teraz " + results[results["Produktywnosc"] == max(results["Produktywnosc"])].index[0])