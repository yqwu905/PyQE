# Configuration.py
# Author: Yuanqing Wu
# Last Modified: 2021/2/28
# Description: This file implement check and raise errors.


def check_atomic_position_unit(value):
    if value not in ['alat', 'bohr', 'angstrom', 'crystal', 'crystal_sg']:
        raise Exception(f"Undefined atomic position type {value} was given.")


def check_pos(value):
    if type(value) is not tuple:
        raise Exception(f"Invalid variable type: tuple was needed, but {type(value).__name__} was given.")
    if len(value) != 3:
        raise Exception(f"Invalid tuple length: should be 3, but was {len(value)}")


def check_if_pos(value):
    if type(value) is not tuple:
        raise Exception(f"Invalid variable type: tuple was needed, but {type(value).__name__} was given.")
    if len(value) != 3:
        raise Exception(f"Invalid tuple length: should be 3, but was {len(value)}")
    for i in range(3):
        if value[i] not in [0, 1]:
            raise Exception(f"Invalid value for if_pos[{i}]: should be 0 or 1, but {value[i]} was given.")


def check_is_real(value):
    if type(value) is not int and type(value) is not float:
        raise Exception(f"Invalid variable type: float needed, but {type(value).__name__} was given.")


def check_is_atom_species(a):
    if type(a).__name__ != 'atomic_species':
        raise Exception(f"Invalid variable type: atomic_species needed, but {type(a).__name__} was given.")


def check_is_atom_position(a):
    if type(a).__name__ != 'atomic_position':
        raise Exception(f"Invalid variable type: atomic_position needed, but {type(a).__name__} was given.")
