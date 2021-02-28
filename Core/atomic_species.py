# Configuration.py
# Author: Yuanqing Wu
# Last Modified: 2021/2/28
# Description: This file implement the class for basic structure of atomic species.


from tool import convert_num
from Error import check


class atomic_species:
    class_flag = 1

    # Parameter:
    #   x:label of the atom.
    #   mass_x:mass of the atomic species
    #   pseudo_pot_x:File containing PP for this species
    def __init__(self, x, mass_x, pseudo_pot_x):
        check.check_is_real(mass_x)
        self.x = x
        self.mass_x = mass_x
        self.pseudo_pot_x = pseudo_pot_x

    def __str__(self):
        return "{} {} {}".format(self.x, convert_num(self.mass_x), self.pseudo_pot_x)
