#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import geopandas as gpd
import json
import csv
import os





# # Country Code

# In[58]:


namefile = 'data/countries.csv'

ndf = pd.read_csv(namefile)
ndf.head()


# In[59]:


ndf.rename(columns={'alpha-2':'alpha_2','alpha-3':'alpha_3'},inplace=True)
ndf.info()


# In[43]:


mgr_country_geo = pd.merge(left=ndf, right=gdf, left_on='alpha_3', right_on='alpha-3')
#mgr_country_geo.info()
mgr_country_geo
mgr_country_geo.to_csv('mgr_country_geo.csv')

mgr_country_geo_covid19 = pd.merge(left=mgr_country_geo, right=cdf, left_on='alpha_3', right_on='ISO_3_CODE')
mgr_country_geo_covid19.info()


# In[4]:


ndf[ndf['alpha_2'] == 'US']


# # geographical data 
# 
# This part of the code is where I assigned the geographical data to a polygon so that I can put them in my map.

# In[5]:





# In[6]:





# In[7]:





# In[8]:





# # Covid-19 data
# 
# this is taking the covid-19 data and merging it with the geographical data

# In[42]:


datafile = 'data/C19 - WHO - May 24, 2020.csv'
#loading in the csv file that contains the data
cdf = pd.read_csv(datafile)
cdf.head()


# In[14]:





# In[54]:


# Write file out
fo = open("mortality_leaf.txt","w")

count = 0 # count number of polygons


for i, row in mgr_country_geo_covid19.iterrows():
   
 
   
    CumulativeCase=(row['CumCase'])
    CumulativeDeath=(row['CumDeath'])
    Geom =(row['geometry'])

    if (int(CumulativeCase) > 0):
        marker = "L.polygon(" + str(Geom) + ",{color:'red',fillColor:'#f03',fillOpacity: " + str(CumulativeDeath/CumulativeCase) + "}).addTo(map).bindPopup ('" + str(CumulativeCase) + "')"
        #marker = "L.circle([" + lat + "," + lon + "],{color:'red',fillColor:'#f03',fillOpacity:0.5,radius:" + str(recoverradius) + "}).addTo(map).bindPopup('" + country.replace("'", "") + " : " + recover + "')"

        fo.write(marker + "\n")
        count = count + 1

print(str(count) + " markers written out")
fo.close()                 
#print(info)
                


 


# In[55]:


fo = open("cases.txt","w")

count = 0 # count number of polygons

max_c19 = mgr_country_geo_covid19['CumCase'].max()

for i, row in mgr_country_geo_covid19.iterrows():
   
 
   
    CumulativeCase=(row['CumCase'])
    CumulativeDeath=(row['CumDeath'])
    Geom =(row['geometry'])

    if (int(CumulativeCase) > 0):
        marker = "L.polygon(" + str(Geom) + ",{color:'blue',fillColor:'#f03',fillOpacity: " + str(CumulativeCase/max_c19) + "}).addTo(map).bindPopup ('" + str(CumulativeCase) + "')"
        #marker = "L.circle([" + lat + "," + lon + "],{color:'red',fillColor:'#f03',fillOpacity:0.5,radius:" + str(recoverradius) + "}).addTo(map).bindPopup('" + country.replace("'", "") + " : " + recover + "')"

        fo.write(marker + "\n")
        count = count + 1

print(str(count) + " markers written out")
fo.close()                 
#print(info)
                


# In[56]:


fo = open("deaths.txt","w")

count = 0 # count number of polygons

max_c19d = mgr_country_geo_covid19['CumDeath'].max()
print(max_c19d)
for i, row in mgr_country_geo_covid19.iterrows():
   
 
   
    CumulativeCase=(row['CumCase'])
    CumulativeDeath=(row['CumDeath'])
    Geom =(row['geometry'])

    if (int(CumulativeCase) > 0):
        marker = "L.polygon(" + str(Geom) + ",{color:'blue',fillColor:'#f03',fillOpacity: " + str(CumulativeDeath/max_c19d) + "}).addTo(map).bindPopup ('" + str(CumulativeDeath) + "')"
        #marker = "L.circle([" + lat + "," + lon + "],{color:'red',fillColor:'#f03',fillOpacity:0.5,radius:" + str(recoverradius) + "}).addTo(map).bindPopup('" + country.replace("'", "") + " : " + recover + "')"

        fo.write(marker + "\n")
        count = count + 1

print(str(count) + " markers written out")
fo.close()                 
#print(info)


# In[ ]:




