# Configuration.py
# Author: Yuanqing Wu
# Last Modified: 2021/2/28
# Description: This file implement some useful tools.


def convert_num(num):
    e_num = int("{:.9e}".format(num).split('e')[-1])
    return "{:.9e}".format(num).replace('+', '').split('e')[0] + 'd' + str(e_num)


# Remove all blank and \n in string.
def format_line(line):
    new_line = ''
    segment = ''
    flag = False
    for i in line:
        if not flag and i != ' ':
            flag = True
        if flag:
            segment += i
            if i != ' ' and i != '\n':
                new_line += segment
                segment = ''
    return new_line


def get_element(string):
    str_list = string.split(' ')
    while '' in str_list:
        str_list.remove('')
    return str_list[0], str_list[2]


def get_atomic_positions_unit(string):
    str_list = string.split(' ')
    while '' in str_list:
        str_list.remove('')
    return str_list[-1].replace('(', '').replace(')', '')


def get_atomic_position(string):
    str_list = string.split(' ')
    while '' in str_list:
        str_list.remove('')
    if len(str_list) == 4:
        return str_list[0], (float(str_list[1]), float(str_list[2]), float(str_list[3])), (1, 1, 1)
    elif len(str_list) == 7:
        return str_list[0], (float(str_list[1]), float(str_list[2]), float(str_list[3])), \
               (float(str_list[4]), float(str_list[5]), float(str_list[6]))
    else:
        return None, None, None
