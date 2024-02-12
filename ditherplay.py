import os, sys, random
from pathlib import Path
from PIL import Image

def randcolor():
    return random.randint(0, 255)

def randbit():
    return random.getrandbits(1)

shouldsave = False

for arg in sys.argv:
    if arg == "-s":
        shouldsave = True

filescount = 0
fileformat = "image-%s.png"
filepath = "imgs/"
while os.path.exists(filepath + fileformat % filescount):
    filescount += 1
filename = fileformat % filescount

img = Image.new('RGB', (255, 255), "black")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        isblack = (i % 3 + j % 13 ) % 2
        if randbit():
            bit = isblack * 255 
        else:
            bit = isblack * 128

        red = ((i + j) % 17) % 2 * randbit() * 255
        green = randcolor()
        blue = (j % 23) % 2 * 255

        pixels[i, j] = (red, green, blue)


if shouldsave:
    img.save(filepath + filename)
img.show()

