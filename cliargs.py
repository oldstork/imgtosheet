import sys
import os

import utils

USAGE = "Usage:\nimgtosheet <directory with images> <output file>"

def parse():
    if(len(sys.argv) != 3):
        print(USAGE)
        sys.exit(1)
    
    if(os.path.isdir(os.path.relpath(sys.argv[1], os.getcwd()))):
        for file_name in os.listdir(os.path.relpath(sys.argv[1], os.getcwd())):
            if(file_name.endswith(".png") and utils.is_int(file_name[:-4]) and int(file_name[:-4]) == 1):
                return os.path.relpath(sys.argv[1], os.getcwd())

        print("No suitable images found in directory.")
        print(USAGE)
        sys.exit(1)
    else:
        print("\"" + sys.argv[1] + "\"" + " is not a directory.")
        print(USAGE)
        sys.exit(1)