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


def check_is_int(value):
    if type(value) is not int:
        raise Exception(f"Invalid variable type: int needed, but {type(value).__name__} was given.")


def check_is_positive_int(value):
    check_is_int(value)
    if value <= 0:
        raise Exception(f"Invalid variable value: should larger than 0, but {value} was given.")


def check_is_atom_species(a):
    if type(a).__name__ != 'atomic_species':
        raise Exception(f"Invalid variable type: atomic_species needed, but {type(a).__name__} was given.")


def check_is_atom_position(a):
    if type(a).__name__ != 'atomic_position':
        raise Exception(f"Invalid variable type: atomic_position needed, but {type(a).__name__} was given.")


def check_is_dict(dict):
    if type(dict).__name__ != 'dict':
        raise Exception(f"Invalid variable type: dict needed, but {type(dict).__name__} was given.")


def check_is_configuration(config):
    if type(config).__name__ != 'configuration':
        raise Exception(f"Invalid variable type: configuration needed, but {type(config).__name__} was given.")


def check_neb_images_match(first_image, last_image):
    if first_image.atom_num != last_image.atom_num:
        raise Exception(f"Unable to create NEB object, because first image has {first_image.atom_num} atoms, but "
                        f"last image has {last_image.atom_num}")
    for i in range(first_image.atom_num):
        if first_image.positions[i].a != last_image.positions[i].a:
            raise Exception(f"Unable to create NEB object, because two atoms with same index in first image and last "
                            f"image has different atom species. One is:\n{first_image.positions[i].a}, one is:\n"
                            f"{last_image.positions[i].a}")


def check_is_neb(neb):
    if type(neb).__name__ != 'neb':
        raise Exception(f"Invalid variable type: neb needed, but {type(neb).__name__} was given.")


def check_setting_dict(s):
    check_is_dict(s)
    keywords = ['PATH', 'CONTROL', 'SYSTEM', 'ELECTRONS']
    for keyword in keywords:
        if not s.__contains__(keyword):
            raise Exception(f"Keyword {keyword} not found for Quantum ESPRESSO input setting.")


def check_kpoints(k):
    check_is_dict(k)
    if not k.__contains__('type'):
        raise Exception(f"Kpoints type not specified.")
    if k['type'] in ['tpiba', 'crystal', 'tpiba_b', 'crystal_b', 'crystal_c']:
        if not k.__contains__('nks'):
            raise Exception(f"Kpoints' type is {k['type']}, nks was needed, but not specified.")
        check_is_positive_int(k['nks'])
        if not k.__contains__('kpoints'):
            raise Exception("Special kpoints was not specified.")
        if len(k['kpoints']) != k['nks']:
            raise Exception(f"nks and special kpoints nums don't match, nks was {k['nks']}, but num of kpoints was"
                            f" {len(k['kpoints'])}")
        for i in k['kpoints']:
            if len(i) != 4:
                raise Exception(f"Each group should has 4 kpoints, but {len(i)} was given.")
            for j in i:
                check_is_real(j)
    elif k['type'] == 'automatic':
        if not k.__contains__('kpoints'):
            raise Exception("Special kpoints was not specified.")
        if len(k['kpoints']) != 6:
            raise Exception(f"Invalid kpoints num, should be 6, but {len(k['points'])} was given.")
        for i in k['kpoints']:
            check_is_int(i)
    elif k['type'] == 'gamma':
        pass
    else:
        raise Exception(f"Unknown kpoints type {k['type']}")
