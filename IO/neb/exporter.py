# Author: Yuanqing Wu
# Last Modified: 2021/3/1
# Description: This file implement export neb script.


from Error.check import *


def export_neb_script(neb, setting_dict, kpoints, outfile='./neb.in'):
    check_is_neb(neb)
    check_kpoints(kpoints)
    check_setting_dict(setting_dict)
    with open(outfile, 'w') as fp:
        fp.write("BEGIN\nBEGIN_PATH_INPUT\n&PATH\n")
        for i in setting_dict['PATH'].keys():
            fp.write(f"   {i}\t = {setting_dict['PATH'][i]},\n")
        fp.write("/\nEND_PATH_INPUT\n\n")
        fp.write("BEGIN_ENGINE_INPUT\n&CONTROL\n")
        for i in setting_dict['CONTROL'].keys():
            fp.write(f"   {i}\t = {setting_dict['CONTROL'][i]},\n")
        fp.write("/\n&SYSTEM\n")
        for i in setting_dict['SYSTEM'].keys():
            fp.write(f"   {i}\t = {setting_dict['SYSTEM'][i]},\n")
        fp.write("/\n&ELECTRONS\n")
        for i in setting_dict['ELECTRONS'].keys():
            fp.write(f"   {i}\t = {setting_dict['ELECTRONS'][i]},\n")
        fp.write("/\n\nATOMIC_SPECIES\n")
        for a in neb.first_image.atom_list:
            fp.write(f"   {a}\n")
        fp.write(f"\nKPOINTS {kpoints['type']}\n")
        if kpoints['type'] in ['tpiba', 'crystal', 'tpiba_b', 'crystal_b', 'crystal_c']:
            fp.write(f"   {kpoints['nks']}\n")
            for i in kpoints['kpoints']:
                for j in i:
                    fp.write(f"   {j}")
                fp.write("\n")
        elif kpoints['type'] == 'automatic':
            for i in kpoints['kpoints']:
                fp.write(f"   {i}")
            fp.write("\n")
        fp.write("\n")
        fp.write("BEGIN_POSITIONS\n")
        fp.write("FIRST_IMAGE\n")
        fp.write(f"{neb.first_image}\n")
        for i in neb.internal_images:
            fp.write("INTERMEDIATE_IMAGE\n")
            fp.write(f"{i}\n")
        fp.write("LAST_IMAGE\n")
        fp.write(f"{neb.last_image}\n")
        fp.write("END_POSITIONS\n")
        fp.write("\n")
        fp.write("END_ENGINE_INPUT\n")
        fp.write("END\n")