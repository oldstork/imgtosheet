import sys

import cliargs
import dimensions
import concat


if(__name__ == "__main__"):
    images_dir = cliargs.parse()
    dx, dy = dimensions.calculate_dimensions(images_dir)
    spritesheet = concat.concat(images_dir, dx, dy)
    spritesheet.save(sys.argv[2], "PNG")
else:
    print("Importing imgtosheet is not allowed.")
    sys.exit(1)