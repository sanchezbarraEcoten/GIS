# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:54:06 2021

@author: DELL
"""

import numpy as np
print("Code Running")



#%%
def at_satellite_brightness_temperature(input_raster_dir, input_MTL_dir, output_dir):
	mtl_reader = open(input_MTL_dir, "r") 
	for line in mtl_reader: 
		if "RADIANCE_MULT_BAND_10" in line:
			ML = float(line.split("= ",1)[1])
		if "RADIANCE_ADD_BAND_10" in line:
			AL = float(line.split("= ",1)[1])
		if "K1_CONSTANT_BAND_10" in line:
			K1 = float(line.split("= ",1)[1])
		if "K2_CONSTANT_BAND_10" in line:
			K2 = float(line.split("= ",1)[1])
	band10_reader = rasterio.open(input_raster_dir)
	DN = band10_reader.read(1).astype('float64')
	L = ( ML * DN ) + AL 
	BT = ( K2 /( np.log( ( K1 / L ) + 1 ) ) ) - 273.15
	ASBT = rasterio.open(output_dir,'w', driver = 'Gtiff', width = band10_reader.width, height = band10_reader.height, count = 1, crs= band10_reader.crs, transform = band10_reader.transform, dtype = 'float64')  #creating and storing .TIF files for At satellite Brightness temperature
	ASBT.write(BT,1)
	ASBT.close()
#%%


# import required module
import os
import rasterio
i=1
# assign directory
directory = 'Experimental data'
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f1 = os.path.join(directory, filename)
    for filename2 in os.listdir(directory):
        f2 = os.path.join(directory, filename2)
        if f1[23:-14] == f2[23:-14]:
            if f1.endswith(".TIF"):
                input_raster_dir=f1
                
            elif f2.endswith(".txt"):
                input_MTL_dir=f2
                
                print("For the iteration: "+str(i)+", these are my variables: "+"\nTiff: "+input_raster_dir+"\ntxt: "+input_MTL_dir+"\n")
                output_dir=r""+"Land_Surface_Temperature_"  + f1[23:-14] + ".tif"
                
               
            ##Call the function
               # print(input_raster_dir)
                #print(input_MTL_dir)
                at_satellite_brightness_temperature(input_raster_dir, input_MTL_dir, output_dir)
                i+=1
        else:
            pass
            





