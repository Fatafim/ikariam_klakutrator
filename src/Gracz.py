
class Gracz:
    def __init__(self, miasta: list):
        self.miasta = miasta
        self.drewno = 0
        self.przelicz_drewno()

        self.wyspy = set([i.wyspa for i in self.miasta])


    def pusc_ture(self):
        for wyspa in self.wyspy:
            for miasto in wyspa:
                miasto.pusc_ture()

        self.przelicz_drewno()

    def przelicz_drewno(self):
        drewno = 0
        for miasto in self.miasta:
            drewno += miasto.produkuj()
        return drewno
