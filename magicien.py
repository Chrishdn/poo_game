from personnage import Personnage
from utils import random_int

class Magicien(Personnage):
    FORCE_FRAPPE_1 = 10
    FORCE_FRAPPE_2 = 15

    def __init__(self, nom, force):
        super().__init__(nom, force)

    def attaque(self, adversaire):
        attaque_type = random_int(1, 2)
        if attaque_type == 1:
            print(f"{self.nom} lance un sort sur {adversaire.nom}.")
            adversaire.recoitDegat(self.FORCE_FRAPPE_1)
        else:
            print(f"{self.nom} lance un rayon de lumière sombre sur {adversaire.nom}.")
            adversaire.recoitDegat(self.FORCE_FRAPPE_2)
        self.gagneExperience()
