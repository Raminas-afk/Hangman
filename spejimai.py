import random
from zodziai import lengvu_zodziu_sarasas
import FunkcijosSuTkinter as fst
import logging

logging.basicConfig(filename='logai.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', encoding = 'utf-8')

class Spejimai:

    def __init__(self):
        self.spejamas_zodis = random.choice(lengvu_zodziu_sarasas)
        self.nematomas_zodis = "−" * len(self.spejamas_zodis)
        self.bandymai = 6
        self.zodis = 1
        self.taskai = 0
        self.sunkumas = "Lengvas"

    def tikrinti_spejima(self, spejimas):
        fst.isjungti_spejamus_mygtukus(spejimas)
        if spejimas in self.spejamas_zodis:
            self.atspeta_raide(spejimas)
        else:
            self.neatspeta_raide(spejimas)

    def atspeta_raide(self, spejimas):
        self.taskai += 10
        fst.atnaujinti_tasku_langa()
        fst.atnaujinti_nematoma_zody(spejimas)
        fst.atnaujinti_pranesimu_langa(spejimas)
        logging.info(f'Teisingas spėjimas "{spejimas}". Taškai: {self.taskai}')
        if self.spejamas_zodis == self.nematomas_zodis:
            self.atspetas_zodis(spejimas)

    def neatspeta_raide(self, spejimas):
        self.bandymai -= 1
        self.taskai -= 3
        fst.atnaujinti_tasku_langa()
        fst.atnaujinti_bandymu_langa()
        fst.atnaujinti_pranesimu_langa(spejimas)
        fst.atnaujinti_kartuviu_nuotrauka()
        logging.info(f'Neteisingas spėjimas "{spejimas}". Taškai: {self.taskai}')
        if self.bandymai == 0:
            self.neatspetas_zodis(spejimas)

    def atspetas_zodis(self, spejimas):
        self.taskai += 30 + (5 * self.bandymai)
        fst.atnaujinti_pranesimu_langa(spejimas)
        fst.atnaujinti_tasku_langa()
        fst.rodyti_pasleptus_mygtukus()
        fst.isjungti_visus_mygtukus()
        fst.pergales_nuotrauka()
        logging.info(f'Atspėtas pilnas žodis -  {self.spejamas_zodis} ({self.zodis}/3). Taškai: {self.taskai}')
        self.zodis += 1
        if self.zodis > 3:
            self.zodis = 1

    def neatspetas_zodis(self, spejimas):
        self.taskai -= 10
        fst.atnaujinti_pranesimu_langa(spejimas)
        fst.atnaujinti_nematoma_zody(spejimas)
        fst.atnaujinti_tasku_langa()
        fst.rodyti_pasleptus_mygtukus()
        fst.isjungti_visus_mygtukus()
        logging.info(f'Neatspėtas pilnas žodis - {self.spejamas_zodis} ({self.zodis}/3). Taškai: {self.taskai}')
        self.zodis += 1
        if self.zodis > 3:
            self.zodis = 1
