import os
import PIL
from PIL import Image

import utils


def concat(images_dir, dx, dy):
    filename_lookup = {}

    for file_name in os.listdir(images_dir):
        if(file_name.endswith(".png") and utils.is_int(file_name[:-4])):
            filename_lookup[int(file_name[:-4])] = os.path.join(images_dir, file_name)
    
    first = Image.open(filename_lookup[1])
    width = first.size[0]
    height = first.size[1]

    spritesheet = Image.new("RGBA", (width * dx, height * dy))
    
    for x in range(1, dx + 1):
        for y in range(0, dy):
            image_to_add = Image.open(filename_lookup[(y * dx) + x])
            spritesheet.paste(image_to_add, ((x - 1) * width, y * height))
    
    return spritesheet