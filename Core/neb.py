# Configuration.py
# Author: Yuanqing Wu
# Last Modified: 2021/2/28
# Description: This file implement some class and function for NEB calculation.


from Error.check import *
from Core.configuration import *


class neb:
    def __init__(self, first_image, last_image, image_num):
        check_is_configuration(first_image)
        check_is_configuration(last_image)
        check_is_positive_int(image_num)
        check_neb_images_match(first_image, last_image)
        self.first_image = first_image
        self.last_image = last_image
        self.image_num = image_num
        self.internal_images = None

    def generate_internal_images(self):
        self.internal_images = []
        for i in range(self.image_num):
            self.internal_images.append(configuration(self.first_image.unit))
        for i in range(self.first_image.atom_num):
            for j in range(self.image_num):
                dis = (self.last_image.positions[i] - self.first_image.positions[i].pos) / (self.image_num + 1)
                self.internal_images[j].append(self.first_image.positions[i] + (dis*(j+1)).pos)
