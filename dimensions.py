import os
import math

import utils


def calculate_dimensions(images_dir):
    used_numbers = set()

    for file_name in os.listdir(images_dir):
        if(file_name.endswith(".png") and utils.is_int(file_name[:-4])):
            used_numbers.add(int(file_name[:-4]))
    
    upper_bounds = 1

    while True:
        if(upper_bounds + 1 in used_numbers):
            upper_bounds += 1
        else:
            break
    
    ubs = int(math.floor(math.sqrt(upper_bounds)))

    for i in range(ubs, 1, -1):
        if(upper_bounds % i == 0):
            return (int(upper_bounds / i), i)
    
    return (upper_bounds, 1)