from abc import ABC, abstractmethod

class Personnage(ABC):
    tour = 'joueur1'

    def __init__(self, nom, force):
        self._nom = nom
        self._vie = 100
        self._force = force
        self._experience = 0
        self._degats = 0

    @property
    def nom(self):
        return self._nom

    @property
    def vie(self):
        return self._vie

    @property
    def force(self):
        return self._force + self._experience  # La force augmente avec l'expérience

    @property
    def experience(self):
        return self._experience

    @property
    def degats(self):
        return self._degats

    @abstractmethod
    def attaque(self, adversaire):
        pass

    def recoitDegat(self, degats):
        self._degats += degats
        if self._degats > self._vie:
            self._degats = self._vie  # Pour éviter des dégâts négatifs

    def gagneExperience(self):
        self._experience += 1
