from personnage import Personnage
from utils import random_int

class RoiSorcier(Personnage):
    FORCE_FRAPPE_1 = 5
    FORCE_FRAPPE_2 = 20

    def __init__(self, nom, force):
        super().__init__(nom, force)

    def attaque(self, adversaire):
        attaque_type = random_int(1, 2)
        if attaque_type == 1:
            print(f"{self.nom} frappe avec son épée {adversaire.nom}.")
            adversaire.recoitDegat(self.FORCE_FRAPPE_1)
        else:
            print(f"{self.nom} attaque avec son Nazgûl {adversaire.nom}.")
            adversaire.recoitDegat(self.FORCE_FRAPPE_2)
        self.gagneExperience()
