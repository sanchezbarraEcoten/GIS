# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:11:36 2021

@author: DELL
"""

import rasterio
import numpy as np
from glob import glob
import os
import matplotlib as plt
from matplotlib import pyplot

directory = 'LST'

arrs=[]
for filename in os.listdir(directory):
    ds= rasterio.open("{}\{}".format(directory,filename))
    arr = ds.read(1)
    arrs.append(arr)
    
print("calculating the mean of the data")

##mean of rasters
average= np.mean(arrs,axis=0)    
print(average)

#plot array raster
pyplot.imshow(average)
pyplot.show()  

# Get metadata from one of the input files
ds_meta = ds.profile

#saving the new raster
with rasterio.open('LST_Av_Final', 'w', **ds_meta) as dst:
       dst.write(average.astype(rasterio.uint8), 1)
       
       






    
    
    