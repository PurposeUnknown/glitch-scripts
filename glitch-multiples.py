import os
import random
from time import time
from PIL import Image
import numpy as np
from glitch_this import ImageGlitcher
import glitchart


glitcher = ImageGlitcher()
dir_start = os.getcwd()
directory = dir_start + "/" + input("Give me a folder: ") + "/"
use_glitchart = input("Use Glitchart? Y/N: ")
use_rotation = input("Glitch rotation? Y/N: ")
os.chdir(directory)

filecount = 0
artglitcher = False
rotation = None

for file in os.scandir(directory):
    filecount += 1
    img = Image.open(f'{file.name}')
    color = random.choice([True, False])

    if use_glitchart.lower() == "y":
        artglitcher = random.choice([True, False])

    if use_rotation.lower() == "y":
        rotation = 90
        img.rotate(rotation, expand=True)

    if artglitcher == True:
        img = glitchart.png(img, min_amount=1, max_amount=2)

    img = glitcher.glitch_image(img, round(random.uniform(1.0, 3.5),1), color_offset=color, gif=False)
        
    if rotation != None:
        img.rotate(90)

    img.save(f'{file.name}')
