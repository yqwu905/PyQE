# Configuration.py
# Author: Yuanqing Wu
# Last Modified: 2021/2/28
# Description: This file implement reading the output file created by pw.x.


import os
from tool import *
from Core.atomic_species import *
from Core.configuration import *


def read_final_configuration(filename):
    with open(filename, 'r') as fp:
        output = fp.readlines()
    flag = False
    unit = None
    pseudo_pot_list = []
    x_list = []
    mass_x_list = []
    atomic_species_list = []
    for i in range(len(output)):
        if output[i] == 'Begin final coordinates':
            print(output[i])
        if 'PseudoPot.' in output[i]:
            pseudo_pot_list.append(os.path.split(format_line(output[i+1]))[-1])
        if 'atomic species' in output[i] and 'valence' in output[i]:
            j = 1
            while format_line(output[i+j]) != '':
                element, mass = get_element(format_line(output[i+j]))
                x_list.append(element)
                mass_x_list.append(mass)
                j += 1
            for j in range(len(x_list)):
                atomic_species_list.append(atomic_species(x_list[j], float(mass_x_list[j]), pseudo_pot_list[j]))
        if 'Begin final coordinates' in output[i]:
            j = 1
            while 'End final coordinates' not in output[i + j]:
                if flag:
                    element, pos, if_pos = get_atomic_position(format_line(output[i + j]))
                    if element is not None:
                        for e in atomic_species_list:
                            if e.x == element:
                                config.append(atomic_position(e, pos, if_pos))
                if 'ATOMIC_POSITIONS' in output[i + j]:
                    config = configuration(get_atomic_positions_unit(format_line(output[i + j])))
                    flag = True
                j += 1
    return config
