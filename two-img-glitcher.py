
from PIL import Image
import numpy as np
import random 
from collections import deque

# Randomly shifts pixel rows / columns from two provided images and reassembles them into one image, 
# repeats based on how many images you want
# ASSUMES YOU HAVE TWO IMAGES OF IDENTICAL SIZE

def image_shifter(count, first, second):
    rotate = random.choice([True, False])
    im_one = np.asarray(Image.open(first + ".png"))
    im_two = np.asarray(Image.open(second + ".png"))

    randomimg = random.choice([im_one, im_two])

    # By default, function slices/moves pixels across the horizontal axis
    # 'Rotate' changes it to the vertical axis
    if rotate == True:
        im_one = np.rot90(im_one, 1, (1,0))
        im_two = np.rot90(im_two, 1, (1,0))

    # play with count/shift values as you please
    newim = []
    rowcount = random.randint(40, 200)
    rowstart = 1
    rowshift = random.randint(-30, 30)
    direction = random.choice([True, False])

    for rownum in range(0, (len(im_one))):
        randomimg = random.choice([im_one, im_two])
        temprow = deque(randomimg[rownum])
        temprow.rotate(rowshift)
        newim.append(list(temprow))
        rowstart += 1

        if rowstart == rowcount:
            rowstart = 1
            rowshift = random.randint(-30, 30)
            rowcount = random.randint(40, 200)
    
    newim = np.asarray(newim)

    if rotate == True:
        newim = np.rot90(newim, 1, (0, 1))

    Image.fromarray(newim).save(f"modified_{str(count).zfill(2)}.png")

# raw filenames, no extension, assumes they're in the same directory as this file
firstfile = input("Give me the first filename: ")
secondfile = input("Give me the second filename: ")


for num in range(1, 100):
    image_shifter(num, firstfile, secondfile)
