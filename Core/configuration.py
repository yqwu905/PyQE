# Configuration.py
# Author: Yuanqing Wu
# Last Modified: 2021/2/28
# Description: This file implement the class for basic structure of atomic configuration.


from Error import check
from tool import *


# Base class for atomic position.
class atomic_position:
    # Parameter:
    #   a: atomic_species
    #   pos: atomic positions(tuple)
    #   if_pos: component i of the force for this atom is multiplied by if_pos(i), which must be either 0 or 1.
    def __init__(self, a, pos, if_pos=(1, 1, 1)):
        check.check_is_atom_species(a)
        check.check_pos(pos)
        check.check_if_pos(if_pos)
        self.a = a
        self.pos = list(pos)
        self.if_pos = list(if_pos)

    def __str__(self):
        res = self.a.x + "\t"
        for i in range(3):
            res += convert_num(self.pos[i]) + "\t"
        res += "{}\t{}\t{}".format(self.if_pos[0], self.if_pos[1], self.if_pos[2])
        return res

    def __add__(self, other):
        check.check_pos(other)
        for i in range(3):
            self.pos[i] += other[i]

    def __sub__(self, other):
        check.check_pos(other)
        for i in range(3):
            self.pos[i] -= other[i]

    def __mul__(self, other):
        check.check_is_real(other)
        for i in range(3):
            self.pos[i] = self.pos[i] * other

    def __truediv__(self, other):
        check.check_is_real(other)
        for i in range(3):
            self.pos[i] = self.pos[i] / other


class configuration:
    def __init__(self, unit='alat'):
        check.check_atomic_position_unit(unit)
        self.unit = unit
        self.positions = []

    def append(self, atom_pos):
        check.check_is_atom_position(atom_pos)
        self.positions.append(atom_pos)

    def replace(self, idx, new_atom_pos):
        check.check_is_atom_position(new_atom_pos)
        self.positions[idx] = new_atom_pos

    def translate(self, translate_vec):
        check.check_pos(translate_vec)
        for i in self.positions:
            i = i + translate_vec

    def __str__(self):
        res = str(self.positions[0])
        for i in self.positions[1:]:
            res += "\n{}".format(i)
        return res
