#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:02:23 2020

@author: guille
"""

import numpy as np
from PIL import Image
from scipy import ndimage
import random

from utils import show_im, im_stats, show_2ims, show_horizontal_cut, normalize_to_range


# reading image with PIL module, converting to mode 'L' (grayscale)
#original = Image.open('original_reduced.png').convert('L')
original = Image.open('picasso.png').convert('L')

# converting it to a numpy array. numpy arrays are easier to manipulate 
im_original = np.array(original)


# %% generate different compression levels

quality_vector = [0, 5, 10, 20, 40, 60, 80, 100]

print(len(quality_vector))

for quality in quality_vector:
    
    # we save the image in very bad quality as JPG. JPEG Artifacts clearly appear. 
    #Image.fromarray(im_original).convert('L').save('stimuli/einstein_%d.jpg' % quality, 'jpeg', 
    #                                      quality=quality)
                                          
    Image.fromarray(im_original).convert('L').save('stimuli/picasso_%d.jpg' % quality, 'jpeg', 
                                          quality=quality)

