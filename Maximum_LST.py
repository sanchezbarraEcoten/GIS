# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:02:34 2021

@author: DELL
"""
from osgeo.gdalconst import *
from osgeo import gdal
import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt
 
##Iterate through the folder of rasters to create a list of rasters

directory = 'LST'
arrs=[]
for filename in os.listdir(directory):
    print(filename)
    ds = gdal.Open("{}\{}".format(directory,filename))
    arr = np.array(ds.GetRasterBand(1).ReadAsArray())  
    print(arr.shape)
    arrs.append(arr)
    #del ds
  
##Get maximum of the rasters creating only one    
mx=arrs[0].copy()
for m in arrs:
    #print("hola")
   mx= np.maximum(mx,m)
   print(mx)
        


#mx2= np.maximum(np.maximum(arrs[0],arrs[1]),arrs[2])   
#print(mx2)    
   
plt.figure()
plt.imshow(mx)



##output maximum
ds_Trans= ds.GetGeoTransform()
ds_proj= ds.GetProjection()



print("Exporting file...")
driver=ds.GetDriver()
outdata = driver.Create("LST_Max.tif", mx.shape[1], mx.shape[0], 1, gdal.GDT_Float64) #Create new GeoTiff
outdata.SetGeoTransform(ds_Trans)
outdata.SetProjection(ds_proj)
bandout= outdata.GetRasterBand(1)
#bandout.SetNoDataValue(NaN_Value)
bandout.WriteArray(mx.astype(np.float64))
bandout.FlushCache()
outdata= None
bandout=None











