# Configuration.py
# Author: Yuanqing Wu
# Last Modified: 2021/2/28
# Description: This file implement the class for basic structure of atomic configuration.


from Error.check import *
from tool import *


# Base class for atomic position.
class atomic_position:
    # Parameter:
    #   a: atomic_species
    #   _pos: atomic positions(tuple)
    #   if_pos: component i of the force for this atom is multiplied by if_pos(i), which must be either 0 or 1.
    def __init__(self, a, pos, if_pos=(1, 1, 1)):
        check_is_atom_species(a)
        check_pos(pos)
        check_if_pos(if_pos)
        self.a = a
        self._pos = list(pos)
        self._if_pos = list(if_pos)

    def __str__(self):
        res = self.a.x + "\t"
        for i in range(3):
            res += convert_num(self._pos[i]) + "\t"
        res += "{}\t{}\t{}".format(self._if_pos[0], self._if_pos[1], self._if_pos[2])
        return res

    def __add__(self, other):
        check_pos(other)
        new_pos = self._pos.copy()
        for i in range(3):
            new_pos[i] += other[i]
        return atomic_position(self.a, tuple(new_pos), self.if_pos)

    def __sub__(self, other):
        check_pos(other)
        new_pos = self._pos.copy()
        for i in range(3):
            new_pos[i] -= other[i]
        return atomic_position(self.a, tuple(new_pos), self.if_pos)

    def __mul__(self, other):
        check_is_real(other)
        new_pos = self._pos.copy()
        for i in range(3):
            new_pos[i] = new_pos[i] * other
        return atomic_position(self.a, tuple(new_pos), self.if_pos)

    def __truediv__(self, other):
        check_is_real(other)
        new_pos = self._pos.copy()
        for i in range(3):
            new_pos[i] = new_pos[i] / other
        return atomic_position(self.a, tuple(new_pos), self.if_pos)

    @property
    def pos(self):
        return tuple(self._pos)

    @property
    def if_pos(self):
        return tuple(self._if_pos)


class configuration:
    def __init__(self, unit='alat'):
        check_atomic_position_unit(unit)
        self.unit = unit
        self.positions = []

    def append(self, atom_pos):
        check_is_atom_position(atom_pos)
        self.positions.append(atom_pos)

    def replace(self, idx, new_atom_pos):
        check_is_atom_position(new_atom_pos)
        self.positions[idx] = new_atom_pos

    def translate(self, translate_vec):
        check_pos(translate_vec)
        for i in self.positions:
            i = i + translate_vec

    @property
    def atom_num(self):
        return len(self.positions)

    def __str__(self):
        res = str(self.positions[0])
        for i in self.positions[1:]:
            res += "\n{}".format(i)
        return res
