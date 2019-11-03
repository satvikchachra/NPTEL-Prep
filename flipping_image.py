# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:22:40 2019

@author: Satvik Chachra
"""
#Importing Library / dependencies
from PIL import Image

# opening image
img=Image.open('mirror.png')

#transposing
transpose_img=img.transpose(Image.FLIP_LEFT_RIGHT) # TAKES THE PIXEL VALUE AS MATRIX FRO COMPUTER UNDERSTANDABLE FORMAT 

#Saving Image
transpose_img.save('corrected.png') #HUMAN UNDERSTANDABLE FORMAT

# for convinece sake
print("Flipping Image, DONE")