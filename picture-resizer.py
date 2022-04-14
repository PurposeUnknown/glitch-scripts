from PIL import Image
import os, sys

path = input("Give me a directory: ")
dirs = os.listdir(path)
os.chdir(path)
width = 0
height = 0

for item in dirs:
    if os.path.isfile(path+item):
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        imResize = im.resize((f"{width}", f"{height}"), Image.ANTIALIAS)
        imResize.save(f'IRL_{item}')
