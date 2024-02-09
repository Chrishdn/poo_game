from personnage import Personnage

class Combat:
    @staticmethod
    def demarrerCombat(magicien, roiSorcier):
        while magicien.degats < magicien.vie and roiSorcier.degats < roiSorcier.vie:
            if Personnage.tour == 'joueur1':
                magicien.attaque(roiSorcier)
                Personnage.tour = 'joueur2'
            else:
                roiSorcier.attaque(magicien)
                Personnage.tour = 'joueur1'

        if magicien.degats >= magicien.vie:
            print(f"{roiSorcier.nom} a vaincu {magicien.nom}!")
        else:
            print(f"{magicien.nom} a vaincu {roiSorcier.nom}!")
