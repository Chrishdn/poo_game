from magicien import Magicien
from roi_sorcier import RoiSorcier
from combat import Combat

magicien = Magicien("Gandalf", 10)
roiSorcier = RoiSorcier("Le Roi Sorcier d'Angmar", 10)

Combat.demarrerCombat(magicien, roiSorcier)
