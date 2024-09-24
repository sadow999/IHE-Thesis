#!/usr/bin/env python
# coding: utf-8

# # To-do list
# 
# Source: https://cds.climate.copernicus.eu/cdsapp#!/dataset/10.24381/cds.6c68c9bb?tab=form
# 
# - [x] [2m_temperature](#2m_temperature)
# - [x] [solar_radiation_flux](#solar_radiation_flux)
# - [x] [10m_wind_speed](#10m_wind_speed)
# - [x] [2m_dewpoint_temperature](#2m_dewpoint_temperature)
# - [x] [2m_relative_humidity](#2m_relative_humidity)
# - [ ] [vapour_pressure](#vapour_pressure) ??
# 

# # Import

# In[2]:


import cdsapi
import zipfile
import os
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import glob
import tarfile
import calendar
import time
c = cdsapi.Client()


# In[3]:


def try_remove(file_path,max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        try:
            # Try to delete the file
            os.remove(file_path)
            print(f"File {file_path} deleted successfully.")
            break  # Exit the loop if deletion is successful
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                print("Waiting for 30 seconds before the next attempt...")
                time.sleep(30)
            else:
                print(f"All {max_attempts} attempts failed. Unable to delete the file.")

def request_cds_api(dataset,retrieve_dictionary,folder):
    c.retrieve(
    dataset,
    retrieve_dictionary,
    'download.tar.gz')
    with tarfile.open('download.tar.gz', 'r:gz') as tar:
        # Extract all contents to the specified directory
        tar.extractall(path=folder)  
        # Rename files
        # Get the list of TarInfo objects
        members = tar.getmembers()
        # Loop through each member
        for member in members:
            # Get the file name in the archive
            file_name = member.name
            # Join the extraction path with the file name
            file_path = os.path.join(folder, file_name)
            # Print the file path
            new_name = file_name[37:]
            new_fh = os.path.join(folder, new_name)
            os.rename(file_path, new_fh)
        # Close the tar file
        tar.close()        
    try_remove('download.tar.gz')
    
    
    


# In[4]:


# change parameters of data request
save_folder=r'E:\WaPORQA\AgERA5'
variables=['2m_temperature', 'precipitation_flux', 
           'solar_radiation_flux', '10m_wind_speed', 
           '2m_relative_humidity'] # see data product overview for other variables
start='2009-01-01'
end='2023-12-31'
dates=pd.date_range(start,end,freq='MS') #list of dates to download data
latlim=[30, 32]
lonlim=[30, 32]
bbox=[32, 30, 30,32] # ymax, xmin, ymin, xmax



# # 2m_temperature

# ## testing 1 month

# In[10]:


c = cdsapi.Client()

c.retrieve(
    'sis-agrometeorological-indicators',
    {
        'variable': '2m_temperature',
        'statistic': [
            '24_hour_maximum', '24_hour_mean', '24_hour_minimum',
        ],
        'year': '2018',
        'month': '02',
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', 
        ],
        'version': '1_1',
        'area': [
            40, -30, -40,
            60,
        ],
        'format': 'tgz',
    },
    'download.tar.gz')


# ## Bulk-downloading

# In[16]:


# change parameters of data request
save_folder=r'D:\Thesis Work\AgERA5_Data'
variables=['2m_temperature', '2m_dewpoint_temperature', 
           'solar_radiation_flux', '10m_wind_speed', 
           '2m_relative_humidity'] # see data product overview for other variables
start='2009-01-01'
end='2023-12-31'
latlim=[30, 32]
lonlim=[30, 32]
bbox=[32, 30, 30,32] # ymax, xmin, ymin, xmax
dataset='sis-agrometeorological-indicators'

dates=pd.date_range(start,end,freq='MS') #list of dates to download data
folder=os.path.join(save_folder,'2m_temperature')
for date in dates:
    _, last_day = calendar.monthrange(date.year, date.month)
    days_in_month = ['%02d'%day for day in range(1, last_day + 1)]
    retrieve_dictionary={
            'variable': '2m_temperature',
            'statistic': [
                '24_hour_maximum', '24_hour_mean', '24_hour_minimum',
            ],
            'year': str(date.year),
            'month': '%02d'%date.month,
            'day': days_in_month,
            'version': '1_1',
            'area': bbox,
            'format': 'tgz',
        }    
    request_cds_api(dataset,retrieve_dictionary,folder)


# In[18]:


print(date) ## check the last date downloaded


# # solar_radiation_flux

# In[19]:


# change parameters of data request
save_folder=r'D:\Thesis Work\AgERA5_Data'
start='2009-01-01'
end='2023-12-31'
latlim=[30, 32]
lonlim=[30, 32]
bbox=[32, 30, 30,32] # ymax, xmin, ymin, xmax
dataset='sis-agrometeorological-indicators'
variable='solar_radiation_flux'
dates=pd.date_range(start,end,freq='MS') #list of dates to download data
folder=os.path.join(save_folder,variable)
if not os.path.exists(folder):
    os.makedirs(folder)
for date in dates:
    _, last_day = calendar.monthrange(date.year, date.month)
    days_in_month = ['%02d'%day for day in range(1, last_day + 1)]
    retrieve_dictionary={
            'variable': variable,
            'year': str(date.year),
            'month': '%02d'%date.month,
            'day': days_in_month,
            'version': '1_1',
            'area': bbox,
            'format': 'tgz',
        }
    try:
        request_cds_api(dataset,retrieve_dictionary,folder)
    except:
        print(date) ## check the last date downloaded


# # 10m_wind_speed

# In[21]:


# change parameters of data request
save_folder=r'D:\Thesis Work\AgERA5_Data'
start='2009-01-01'
end='2023-12-31'
latlim=[30, 32]
lonlim=[30, 32]
bbox=[32, 30, 30,32] # ymax, xmin, ymin, xmax
dataset='sis-agrometeorological-indicators'
variable='10m_wind_speed'
dates=pd.date_range(start,end,freq='MS') #list of dates to download data
folder=os.path.join(save_folder,variable)
if not os.path.exists(folder):
    os.makedirs(folder)
for date in dates:
    _, last_day = calendar.monthrange(date.year, date.month)
    days_in_month = ['%02d'%day for day in range(1, last_day + 1)]
    retrieve_dictionary={
            'variable': variable,
            'statistic':'24_hour_mean',
            'year': str(date.year),
            'month': '%02d'%date.month,
            'day': days_in_month,
            'version': '1_1',
            'area': bbox,
            'format': 'tgz',
        }    
    try:
        request_cds_api(dataset,retrieve_dictionary,folder)
    except:
        print(date) ## check the last date downloaded


# # Precipitation_flux

# In[5]:


# change parameters of data request
save_folder=r'D:\Thesis Work\AgERA5_Data'
start='2009-01-01'
end='2023-12-31'
latlim=[30, 32]
lonlim=[30, 32]
bbox=[32, 30, 30,32] # ymax, xmin, ymin, xmax
dataset='sis-agrometeorological-indicators'
variable='precipitation_flux'
dates=pd.date_range(start,end,freq='MS') #list of dates to download data
folder=os.path.join(save_folder,variable)
if not os.path.exists(folder):
    os.makedirs(folder)
for date in dates:
    _, last_day = calendar.monthrange(date.year, date.month)
    days_in_month = ['%02d'%day for day in range(1, last_day + 1)]
    retrieve_dictionary={
            'variable': variable,
            'year': str(date.year),
            'month': '%02d'%date.month,
            'day': days_in_month,
            'version': '1_1',
            'area': bbox,
            'format': 'tgz',
        }    
    try:
        request_cds_api(dataset,retrieve_dictionary,folder)
    except:
        print(date) ## check the last date downloaded


# # 2m_relative_humidity

# In[22]:


# change parameters of data request
save_folder=r'D:\Thesis Work\AgERA5_Data'
start='2009-01-01'
end='2023-12-31'
latlim=[30, 32]
lonlim=[30, 32]
bbox=[32, 30, 30,32] # ymax, xmin, ymin, xmax
dataset='sis-agrometeorological-indicators'
variable='2m_relative_humidity'
dates=pd.date_range(start,end,freq='MS') #list of dates to download data
folder=os.path.join(save_folder,variable)
if not os.path.exists(folder):
    os.makedirs(folder)
for date in dates:
    _, last_day = calendar.monthrange(date.year, date.month)
    days_in_month = ['%02d'%day for day in range(1, last_day + 1)]
    retrieve_dictionary={
            'variable': variable,
            'year': str(date.year),
            'month': '%02d'%date.month,
            'day': days_in_month,
            'version': '1_1',
            'area': bbox,
            'format': 'tgz',
            'time': [
            '06_00', '09_00', '12_00',
            '15_00', '18_00']
        }    
    try:
        request_cds_api(dataset,retrieve_dictionary,folder)
    except:
        print(date) ## check the last date downloaded


# ## Inspect data

# In[24]:


fhs=glob.glob(r"D:\Thesis Work\AgERA5_Data\2m_temperature\*.nc")
ds=xr.open_dataset(fhs[0])
ds


# In[25]:


ds.Temperature_Air_2m_Max_24h[0].plot()


# In[ ]:




