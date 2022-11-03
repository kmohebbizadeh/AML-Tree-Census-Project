#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:05:09 2022

@author: hanjio
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
df2015 = pd.read_csv("2015_Street_Tree_Census_-_Tree_Data.csv")

#%% check missing values
#plots for data cleaning
from catscatter import catscatter
#1. health vs status
health_status = df2015[['health', 'status']].fillna("nan")

group1 = pd.DataFrame(health_status.groupby(['health', 'status']).size().reset_index())
group1.columns = ["health", "status", "counts"]

#plot it
catscatter(group1,'status', 'health', 'counts',
           color = ["green","grey","orange"], 
           ratio = 0.005,
           save = True,
           save_name = "missing_value: health vs status")
plt.show()
plt.rcParams.update(plt.rcParamsDefault)

#%% check missing values

#2. NA plot
col_na_all = df2015.isnull().sum() / len(df2015)

col_na = col_na_all[col_na_all != 0]

# change to all columns
#col_na = col_na_all

fig = plt.figure(figsize = (10, 5))
ax = sns.barplot(x = col_na.index, y = col_na.values * 100, color = 'b')
ax.set_ylim(0, 0.05 * 100)
ax.set(xlabel = 'features', 
       ylabel='% of missing values', 
       title='% of missing values in each column')
ax.yaxis.set_major_formatter(mtick.PercentFormatter()) # change the y-axis to␣percentage
ax.tick_params(axis = 'x', rotation = 45) # rotate the feature names 45 degree

plt.savefig('missing_value_percentage.png')
plt.show()

#%% create new 
kept = ['tree_dbh', 'curb_loc', 'health', 
        'spc_common', 'steward', 'guards', 'sidewalk', 'user_type', 
        'root_stone', 'root_grate', 'root_other', 
        'trunk_wire', 'trnk_light', 'trnk_other',
        'brch_light', 'brch_shoe', 'brch_other', 
        'st_senate', 'st_assem', 'borocode', 'cncldist', 'nta_name', 
        'community board', 'zip_city', 'latitude', 'longitude']
df = df2015[kept].dropna()

#%% pie chart of y
#1 mosaic plots between health and categorical features
#%% 2 box plots between health and continous feature: tree_dbh
ax = sns.boxplot(data = df, x = "tree_dbh", y = "health")
ax.set_xscale('log')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.set_title("distribution of log tree diameter in different health conditions")

plt.savefig('health vs tree_dbh.png')

#%% 2 catscatter for other plot
categoricals = [x for x in kept if x not in ['tree_dbh', 'latitude', 'longitude', 'health']]

for feature in categoricals:
    group = pd.DataFrame(df.groupby(['health', feature]).size().reset_index())
    group.columns = ["health", feature, "counts"]

    #plot it
    catscatter(group, feature, 'health', 'counts',
               color = ["green","grey","orange"], 
               ratio = 0.005,
               save = True,
               save_name = f"health vs {feature}")
    plt.show()

plt.rcParams.update(plt.rcParamsDefault)

#%% 2 map for latitude and longitude
from shapely.geometry import Point, Polygon
import geopandas as gpd
#import geoplot
from geopandas import GeoDataFrame

# create geo dataframe
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = GeoDataFrame(df[['health', 'longitude', 'latitude']], geometry=geometry)
#%%
## source:
# https://geopandas.org/en/stable/docs/user_guide/geocoding.html

# get map of NY
ny_map = gpd.read_file(gpd.datasets.get_path('nybb'))
# plot
alpha = 0.1
markersize = 10
fig,ax=plt.subplots(figsize=(15,15))
ny_map.to_crs("EPSG:4326").plot(ax=ax,alpha=0.4,color="grey")
gdf[gdf['health']=="Good"].plot(ax=ax,markersize=markersize, alpha=alpha,color="green", label="good")
gdf[gdf['health']=="Fair"].plot(ax=ax,markersize=markersize, alpha=alpha,color="yellow", label="Fair")
gdf[gdf['health']=="Poor"].plot(ax=ax,markersize=markersize, alpha=alpha,color="tomato", label="Poor")
plt.legend()

plt.savefig('map_health_conditions.png')
plt.show()
#%% 3 pie chart of health (imbalance)
#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:5]
counts = df[['health']].groupby('health').size()
#create pie chart
plt.pie(counts.values, labels = counts.index, colors = colors, autopct='%.0f%%')
plt.title("Distribution of health")

plt.savefig('Distribution of health.png')
plt.show()


