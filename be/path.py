import sys
import os

def appendPath():
    sys.path.append(os.path.join(sys.path[0], "./modules/"))
