
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[146]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
from IPython.display import display
import numpy as np

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[148]:

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df = df.sort(['ID', 'Date'])
df


# In[175]:

# Pre-process the data
df['year'] = df['Date'].apply(lambda x: x[:4])
df['Month_day'] = df['Date'].apply(lambda x: x[5:])
df = df[df['Month_day'] != '02-29']


df_min = df[(df['Element'] == 'TMIN')]
df_max = df[(df['Element'] == 'TMAX')]

df_alltemp_min = df[(df['Element'] == 'TMIN') & (df['Year'] != '2015')]
df_alltemp_max = df[(df['Element'] == 'TMAX') & (df['Year'] != '2015')]

temp_min = df_alltemp_min.groupby('Month-Day')['Data_Value'].agg({'temp_min_mean': np.mean})
temp_max = df_alltemp_max.groupby('Month-Day')['Data_Value'].agg({'temp_max_mean': np.mean})

temp_min15tmp = df_min[df_min['Year'] == '2015']
temp_max15tmp = df_max[df_max['Year'] == '2015']

temp_min15 = temp_min15tmp.groupby('Month-Day')['Data_Value'].agg({'temp_min_15_mean': np.mean})
temp_max15 = temp_max15tmp.groupby('Month-Day')['Data_Value'].agg({'temp_max_15_mean': np.mean})

#Reset Index
temp_min = temp_min.reset_index()
temp_max = temp_max.reset_index()

temp_min15 = temp_min15.reset_index()
temp_max15 = temp_max15.reset_index()

# find_index
recbroken_min = (temp_min_15[temp_min15['temp_min_15_mean'] < temp_min['temp_min_mean']]).index.tolist()
recbroken_max = (temp_max_15[temp_max15['temp_max_15_mean'] > temp_max['temp_max_mean']]).index.tolist()


fig,ax = plt.subplots(figsize=(15,7))

ax.plot(temp_min['temp_min_mean'], 'y', alpha = 0.75, label = 'Record Low')
ax.plot(temp_max['temp_max_mean'], 'r', alpha = 0.5, label = 'Record High')


ax.scatter(broken_min, temp_min15['temp_min_15_mean'].iloc[broken_min], s = 1, c = 'k', label = 'Broken Min')
ax.scatter(broken_max, temp_max15['temp_max_15_mean'].iloc[broken_max], s = 1, c = 'b', label = 'Broken Max')

plt.xlabel('Month')
plt.ylabel('Temperature (Tenths of Degrees C)')
plt.title('Extreme Temperatures of 2015 against 2005-2014\n near Michigan,Ann Arbor')

plt.gca().fill_between(range(len(temp_min)), 
                       temp_min['temp_min_mean'], temp_max['temp_max_mean'], 
                       facecolor='grey', 
                       alpha=0.2)

plt.gca().axis([-5, 370, -400, 400])
plt.legend(frameon = False)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

a = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
b = [i+15 for i in a]

Month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(b, Month_name)



# In[174]:

import os
os.getcwd()
os.chdir('C:\Users\anadi')
fig.savefig("Weatherplot.png")


# In[ ]:



