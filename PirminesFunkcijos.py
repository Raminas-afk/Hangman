import random

class Spejimai:

    def __init__(self):
        self.spejamas_zodis = random.choice(lengvu_zodziu_sarasas)
        self.nematomas_zodis = "−" * len(self.spejamas_zodis)
        self.bandymai = 6
        self.zodis = 1
        self.taskai = 0
        self.sunkumas = "Lengvas"

    def tikrinti_spejima(self, spejimas):
        isjungti_spejamus_mygtukus(spejimas)

        if spejimas in self.spejamas_zodis:
            self.teisingas_spejimas(spejimas)

        elif spejimas not in self.spejamas_zodis:
            self.neteisingas_spejimas(spejimas)

    def teisingas_spejimas(self, spejimas):

        for raide in range(len(self.spejamas_zodis)):
            if self.spejamas_zodis[raide] == spejimas:
                self.taskai += 10
                tasku_langas.config(text=f"Taškai: {self.taskai}")
                self.nematomas_zodis = self.nematomas_zodis[:raide] + self.spejamas_zodis[raide] + self.nematomas_zodis[
                                                                                                   raide + 1:]
                teksto_langas.config(text=f"Atspėjai! raidė {spejimas} yra šiame žodyje.")
                teksto_langas2.config(text=self.nematomas_zodis)

        if self.spejamas_zodis == self.nematomas_zodis:
            self.atspetas_zodis()

    def neteisingas_spejimas(self, spejimas):
        self.bandymai -= 1
        self.taskai -= 3
        klaidos_nuotrauka()
        teksto_langas.config(text=f"Neatspėjai! Raidės {spejimas} žodyje nėra.")
        tasku_langas.config(text=f"Taškai: {self.taskai}")
        bandymu_langas.config(text=f"Liko bandymų:{spejimai.bandymai}")
        if self.bandymai == 0:
            self.neatspetas_zodis()

    def atspetas_zodis(self):
        self.taskai += 30 + (5 * self.bandymai)
        teksto_langas.config(text="Atspėjai!")
        tasku_langas.config(text=f"Taškai: {self.taskai}")
        rodyti_pasleptus_mygtukus()
        isjungti_visus_mygtukus()
        pergales_nuotrauka()
        self.zodis += 1
        if self.zodis > 3:
            self.zodis = 1

    def neatspetas_zodis(self):
        self.taskai -= 10
        teksto_langas.config(text=f"Neatspėjai!")
        teksto_langas2.config(text=self.spejamas_zodis)
        tasku_langas.config(text=f"Taškai: {self.taskai}")
        rodyti_pasleptus_mygtukus()
        isjungti_visus_mygtukus()
        self.zodis += 1
        if self.zodis > 3:
            self.zodis = 1

