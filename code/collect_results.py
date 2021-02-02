#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:43:09 2020

@author: guille
"""

import pandas as pd
import glob
import numpy as np

obs = 'im'

fnames = glob.glob('design/%s/*_results.csv' % obs)


# %% reading all data files and putting in one pandas' DataFrame
data = []

for f in fnames:
    
    df = pd.read_csv(f)
    
    data.append(df)
    
DF = pd.concat(data)


# %% reindexing the stimulus values

quality_vector = [0, 5, 10, 20, 40, 60, 80, 100] # 'quality' factor unit for JPG compression

degradation_vector = 100 - np.array(quality_vector)
print(degradation_vector)

# we define the stimulus variable as degradation =  100 - quality
mapping = {'stimuli/einstein_%d.jpg' % x : (len(quality_vector)-i) for i, x in enumerate(quality_vector)}

print(mapping)


# %%
def replacestimval(val):
    return mapping[val]

DF['S1'] = DF['S1'].apply(replacestimval)
DF['S2'] = DF['S2'].apply(replacestimval)
DF['S3'] = DF['S3'].apply(replacestimval)


DF[['resp', 'S1', 'S2', 'S3']].to_csv('%s_results.csv' % obs, index=False)


#  EOF
