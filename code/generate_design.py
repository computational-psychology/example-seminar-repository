#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:11:54 2020

@author: guille
"""

import itertools
import pandas as pd
import numpy as np
import random

quality_vector = [0, 5, 10, 20, 40, 60, 80, 100] # 'quality' factor unit for JPG compression

totalNblock = 5


def shuffle_triad(t):
    
    # randomly chooses if triad is increasing or decreasing
    if random.randint(0,1)==1:
        t1 = t[0]
        t2 = t[1]
        t3 = t[2]
    else:
        t1 = t[2]
        t2 = t[1]
        t3 = t[0]
        
    return (t1, t2, t3)

# unique triads
trials = list(itertools.combinations(quality_vector, 3))

# iterates across all blocks
for nblock in range(totalNblock):

    # each block has a full set of unique triads
    designmlds = []    
    for t in trials:

        t1, t2, t3 = shuffle_triad(t)
        
        fname1 = 'stimuli/einstein_%d.jpg' % t1
        fname2 = 'stimuli/einstein_%d.jpg' % t2
        fname3 = 'stimuli/einstein_%d.jpg' % t3
        
        designmlds.append([fname1, fname2, fname3])
        

    # creates dataframe with all trials
    df = pd.DataFrame(designmlds, columns=['S1', 'S2' ,'S3'])
    
    # shuffles order
    df = df.reindex(np.random.permutation(df.index))
    df.reset_index(drop=True, inplace=True)
    
    #df.index.name = 'Trial'
    
    # save in design folder, under block number
    df.to_csv('design/block_%d.csv' % nblock, index=False)
    

# EOF