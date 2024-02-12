import os, sys, random
from pathlib import Path
from PIL import Image, ImagePalette
import numpy as np

def randcolor():
    return random.randint(0, 255)

def randbit():
    return random.getrandbits(1)

shouldsave = False

if len(sys.argv) < 2:
    print("please supply a filename")
    exit()

filename = sys.argv[1]

for arg in sys.argv:
    if arg == "-s":
        shouldsave = True


colormap = [
    255, 174, 59,  # melon
    228, 93, 80,   # crimson
    94, 200, 229,  # aqua
    0, 169, 92,    # green
    64, 112, 96,   # hunter green
    255, 255, 255, # white
    0, 0, 0        # black
]

colormap = np.array(colormap, dtype=np.uint8)
palette = ImagePalette.ImagePalette(mode="RGB", palette=colormap.tobytes())

with Image.open(filename) as img_in:
    palette_img = Image.new("P", img_in.size)
    palette_img.putpalette(palette)
    img_out = img_in.quantize(palette=palette_img, 
                              method=Image.Quantize.FASTOCTREE)

img_out.save("test.gif")

