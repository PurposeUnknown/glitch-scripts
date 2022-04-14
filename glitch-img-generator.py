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
filename = input("Give me a filename: ")
glitch_number = input("Give me a number: ")
use_glitchart = input("Use Glitchart? Y/N: ")
use_rotation = input("Glitch rotation? Y/N: ")
os.chdir(directory)

artglitcher = False
rotation = None

for i in range(1, int(glitch_number)):

    img = Image.open(f'{filename}.png')
    color = random.choice([True, False])

    if use_glitchart.lower() == "y":
        artglitcher = random.choice([True, False])

    if use_rotation.lower() == "y":
        rotation = random.randint(0, 359)
        img.rotate(rotation)

    if artglitcher == True:
        img = glitchart.png(img, min_amount=1, max_amount=2)

    img = glitcher.glitch_image(img, round(random.uniform(1.2, 3.5), 1), color_offset=color)

    if rotation != None:
        img.rotate(-(rotation))

    img.save(f'{i}-{filename}.png')
