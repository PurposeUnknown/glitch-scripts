from matplotlib import image, pyplot
from PIL import Image
import numpy as np
import os
import random 
from collections import deque

def image_shifter(count, filename):
    rotate = random.choice([True, False])
    im = np.asarray(Image.open(filename + ".png"))
    if rotate == True:
        im = np.rot90(im, 1, (1,0))

    newim = []
    rowcount = random.randint(20, 50)
    rowstart = 1
    rowshift = random.randint(-20, 20)
    direction = random.choice([True, False])
    #if direction == True:
    #    rowshift = -rowshift
    for row in im:
        temprow = deque(row)
        temprow.rotate(rowshift)
        newim.append(temprow)
        rowstart += 1

        if rowstart == rowcount:
            rowstart = 1
            rowshift = random.randint(-20, 20)
            #if direction == True:
            #    rowshift = -rowshift
            rowcount = random.randint(20, 50)
    
    newim = np.asarray(newim)
    if rotate == True:
        newim = np.rot90(newim, 1, (0,1))
    #filename = filename.split('.')[0]
    #filename = filename.split('_')[0] + f"_{str(count).zfill(2)}"
    Image.fromarray(newim).save(filename + f"_{str(count).zfill(2)}_{str(direction)}.png")
    #return filename

file = input("Give me a filename: ")

for num in range(1, 100):
    #file = image_shifter(num, file)
    image_shifter(num, file)
