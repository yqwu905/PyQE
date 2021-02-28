# Configuration.py
# Author: Yuanqing Wu
# Last Modified: 2021/2/28
# Description: This file implement some useful tools.


def convert_num(num):
    e_num = int("{:.9e}".format(num).split('e')[-1])
    return "{:.9e}".format(num).replace('+', '').split('e')[0] + 'd' + str(e_num)