# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:55:35 2021

@author: DELL
"""


###shapes with geopandas

#%% Polygon with X(Lon) and Y(Lat)

import shapefile

 w = shapefile.Writer('poly2D') #Put the name of the shape
 w.autoBalance = 1
 w.field('name', 'C')


#The coordinates must to be ordered in a counterclockwise direction. If you want to create two or more polygons in the same shape,add the coordinates in the rigth way and change the parameters field and record(). 

 w.poly([
        [[-115.859,29.286], [-112.827,30.57], [-110.151,25.435], [-113.51,23.66],[-115.859,29.286]]#, Put The coordinates of the polygon1
        #[[long,lat],[long,lat],[long,lat],[long,lat]], #Hole 1
         #[[long,lat], [long,lat], [long,lat]]  # polygon 2
        ])
 w.record('polygon1')

 w.close()
 
 
#Adding the projection to the shape, this is a geographic projection, if you need another projection you should change it here 

with open("poly2D", "w") as text_file:
    epsg = 'GEOGCS ["WGS 84",'   
    epsg += 'DATUM["WGS_1984",'
    epsg += 'SPHEROID ["WGS 84" ,6378137,298.257223563]]' 
    epsg += ',PRIMEM["Greenwich",0],'
    epsg += 'UNIT["degree",0.0174532925199433]]'        
    
    print(epsg, file=text_file)
#%%  3D Polygon with X(Lon), Y(Lat) and Z(Ele)
#Note:  If you omit the third Z-coordinate it will default to 0.
# You can add Measurement(m) values, Measured shape types are shapes that include a measurement value at each vertex

w = shapefile.Writer('poly3D')
>>> w.field('name', 'C')

w.polyz([
			[[-115.859,29.286,18],[-112.827,30.57,20],[-110.151,25.435,22],[-113.51,23.66],[-115.859,29.286]], # line with some omitted Z-values
			#[[3,2],[2,6]], # line without any Z-values
			#[[3,2,15,0],[2,6,13,3],[1,9,14,2]] # line with both Z- and M-values
  		 ])

w.record('polyz')

w.close()

#Adding the projection to the shape, this is a geographic projection, if you need another projection you should change it here 

with open("poly3D.prj", "w") as text_file:
    epsg = 'GEOGCS ["WGS 84",'   
    epsg += 'DATUM["WGS_1984",'
    epsg += 'SPHEROID ["WGS 84" ,6378137,298.257223563]]' 
    epsg += ',PRIMEM["Greenwich",0],'
    epsg += 'UNIT["degree",0.0174532925199433]]'        
    
    print(epsg, file=text_file)