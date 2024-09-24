#!/usr/bin/env python
# coding: utf-8

# ## Downloading rasters from the WAPOR data portal
# 
# #### Introduction
# 
# The waporact package is built for the effecient and easy retrieval and analysis of rasters from the WAPOR portal. Download of data from the wapor portal using the waporact package is carried out using the script:
# 
# *waporact\scripts\retrieval\wapor_retrieval.py*
# 
# This notebook guides you through that first important step the downloading of data using the class **WaporRetrieval** found in the script *wapor_retrieval.py*. 
# 
# A tutorial video is also available: https://www.youtube.com/watch?v=pRh1BG_PGjQ 
# 
# ### **Steps**:<br>
# 
# 1. Importing of the modules and functions needed<br><br> 
# 
# 2. Get a download api token from the WAPOR [portal](https://wapor.apps.fao.org/home/WAPOR_2/1)<br><br> 
# 
# 3. activating/initiating the class **WaporRetrieval**: This python class holds all the functions used to interact with the WAPOR portal and retrieve information from it. It is built on top of the class **WaporAPI** originally written by Bich Tran at IHE Delft for the various open source WAPOR packages released by IHE DELFT.<br><br>  
# 
# 4. running of the function *download_wapor_rasters*: This function downloads rasters form the WAPOR portal according to the users requirements and processes, masks and stores them accordingly.<br><br>  
# 
# 5. Take a look at where the retrieved data is stored<br><br> 
# 
# NOTE: If this is your first time running this please read the instructions below and follow the steps, otherwise feel free to use the notebook as you wish.
# 
# ***

# NOTE: Reading the following is not required but it is advised
# 
# ### A quick guide to the waporact package scripts and the automatic folder structure used in the classes can be found via the links below:
# 
# - [automated folder structure explained](https://github.com/eLEAF-Github/WAPORACT/wiki/2.-The-WaPORAct-Package-4.-Automated-Folder-Structure-Explained)
# 
# - [waporact package structure further explained](https://github.com/eLEAF-Github/WAPORACT/wiki/2.-The-WaPORAct-Package-2.-WaPORAct-Toolset)
# 
# ***

# ## 1. Import modules/libraries

# In[7]:


import os
from datetime import datetime

# import retrieval claval import WaporRetrieval
print('retrieval class succesfully imported')

print('class imported successfully, you are at the starting line')


# ***
# ## 2. Get a download token from the WAPOR website
# 
# Get your API Token from https://wapor.apps.fao.org/profile, once you have it you pass it as an argument below when intiating the class
# as api_token='<your_token_goes_here>' . Remember to use '' so that it is recognized as a string object
# 

# ***
# ## 3. Initiate/activate the class **WaporRetrieval**. 
# 
# **Background info**: 
# 
# the class **WaporRetrieval** is built on top of (inherits) an edited version of the class **WaporAPI** originally written by Bich Tran at IHE Delft for the various open source WAPOR packages released by IHE DELFT. It is this class that allows access to the data on the wapor portal. 
# 
# It is a great package for accessing the WAPOR data via API and if you want more flexibility in your implementation or if you want to dive into the code directly; I recommend you check out the original code available via their packages on GIT. You can also check out the edited version of their **WaporAPI** class that can be found in this package.
# 
# ### **Activating the class**:
# 
# to intiate the class you need to enter/edit the following inputs below:
# 
# #### Required Inputs:
# 
# - **waporact_directory**: path to the directory where the project specific directory will be created. the class *WaporRetrieval* automatically creates a new directory using the input *project_name* on activation and creates subfolders to organise the data as well. The functions that follow automatically use these folders.<br><br> 
# 
# - **shapefile_path**: the shapefile is a needed input that specifies the location to download data for as well as the projection to output it in. Directly the input is the path to the shapefile itself. The function retrieves the data for the area(s) shown in the shapefile.<br>
# 
#     - **Note**: A shapefile is required and provides alot of the required info for the project including the extent and the output projection. Any projection (crs) is accepted, wapor data is always downloaded in epsg: 4326 and the shapefile bounding box is transformed as needed to match. If needed the retrieved data is transformed to match the original projection of the input shapefile if needed.<br><br>  
# 
# - **wapor_level**: level of WAPOR data to download. There are 3 levels from low resolution 250m (1) and mid resolution 100m (2) to high resolution 30m (3). All of Africa and part of the middle east is available at level 1. Specific countries are available at level 2. Only some specific locations around the size of valleys or hydrosheds are available at level 3. For more info on the levels please see: https://wapor.apps.fao.org/home/WAPOR_2/1. <br> 
# 
#     - **Note**: A spatial check is carried out on the download area specified in your shapefile to see if data is available for it at the given level when running (only level 1 and 3 spatial checks exist currently). Error messages provide details.<br><br> 
# 
# - **api_token**: the api token retrieved form the WAPOR site goes here. see the instructions above on how to retrieve a token from the WAPOR website.<br><br>
# 
# - **period_start**: date you want to start your data download from, enter as a datetime object. This can be provided again later in other functions overwriting the stored period_start.<br><br> 
# 
# - **period_end**: date you want to end your data download at, enter as a datetime object.This can be provided again later in other functions overwriting the stored period_end. <br><br>
# 
#     - **datetime objects**: A specific way of formatting dates for python. It is made up of the function datetime followed by the date in brackets split into the sections: Year (4 digits), month (2 or 1 digit), day (2 or 1 digits). (google python datetime object for more details)<br>
# 
#         - *Example*: November 4th 2020 or 4-11-2020: datetime(2020,11,4)<br>
# 
#         - *Note*: do not use leading zeros for single digit dates (1 not 01).<br><br>  
# 
# 
# #### Optional Inputs:
# 
# The following inputs are optional and have default values. They can also be provided later when running the class functions. 
# 
# - **project_name**: name of the directory that will be created, all data retrieved and analysed can be found in here, auto set to *test* if not provided.<br><br> 
# 
# - **return_period**: return period to download data for, given as a single letter code. available periods include: I: Daily, D: Dekadal, S: Seasonal, A: Annual (yearly). This can also be provided later when running the class functions. Auto sets to the Dekadal (D) if not provided.<br><br> 
# 
# - **silent**: boolean option automatically set to False. If set to True the more general messages shared with the user when running the class will be turned off.<br><br> 
# 
#     - **Note**: class arguments period_start, period_end and return_period are stored in the class and the user does not need to provide them anymore afterwards. If the argument is provided again while using a function (example: *download_wapor_rasters*) the argument stored in the class instance is replaced and the new version is used moving forward.

# In[27]:


import sys
from datetime import datetime

# Add the path to the waporact module
sys.path.append(r"D:\Thesis Work\Codes\WAPORACT-master")

# Import the WaporRetrieval class
from wapor_retrieval import WaporRetrieval

# Activation of the Wapor retrieval class
retrieval = WaporRetrieval(            
    waporact_directory=r"D:\Thesis Work\FAO_WAPOR_Data",
    vector_path=r"D:\Thesis Work\Study_Area_SHP\Study_Area.shp",
    wapor_level=3,
    period_start=datetime(2009,1,1),
    period_end=datetime(2023,1,1),
    return_period='D',
    project_name='waporact_test',
    api_token='18752ac71d6ef17af547c6e4a295ab6def16577cff69faa587abe34de30bd5eb962e0c899878f371'
)


# ### NOTE: The retrieval function uses a bbox to retrieve data 
# 
# TTo make sure all data falls within the bbox. the bbox is constructed based on the vector given as input to the class and then made slightly larger to make sure all the data falls within it. This bbox is stored internally in the class instance see below. the vector file of it is also available in the metadata folder of the wapor level that you are retrieving data for:

# In[24]:


# print bbox tuple and a shapefile path as an example

print('bbox: {}'.format(retrieval.bbox))


# ***
# ### 3.1 Check out the level catalogues and availability shapefile
# 
# #### Wapor Catalogs:
# 
# - When  you run the class **WaporRetrieval** for the first time the class automatically downloads a catalog of the data available at level 1 2 and 3 as .csv and stores it in:<br>
# 
#     - *<user_specified_waporact_directory>\metadata*<br><br>
# 
#     - These catalogs are useful for finding out what data is availalble on the wapor portal as well as which codes represent which datasets/countries/time periods. Feedback on which codes are available is also given as feeback to the user when passed incorrectly to functions from the **WaporRetrieval** class
# 
# #### Wapor level 3 availability shapefile:
# 
# - When  you run the class **WaporRetrieval** for the first time the class automatically generates a level 3 availability shapefile and also stores it in:<br>
# 
#     - *<user_specified_waporact_directory>\metadata*<br><br>
# 
#     - This shapefile shows for which areas wapor level 3 data is available. It is also used to check if level 3 data is available for any given area when attempting to download level 3 data using a shapefile. And provides the level 3 country code required by the **WaporAPI** to donwload data for that area if it is available. <br><br>
#     
# - NOTE: On activating the class these files are automatically checked for and downloaded again if they are not found/deleted. In cas the files are older than 2 months they are also donwloaded again.

# ***
# ## 4. Download data from the WAPOR portal
# 
# After activating the class **WaporRetrieval** it is possible to donwload data from the wapor portal using the function: *download_wapor_rasters*. 
# 
# ### Description
# 
# *download_wapor_rasters* is made up of two sub functions *retrieve_wapor_download_info* and *retrieve_wapor_rasters*. So to help you understand what is going on inside both here is some more info.<br><br>
# 
# - *retrieve_wapor_download_info*: per raster to be downloaded sets up a download and preprocessing dictionary containing all info needed to retrieve each raster from the wapor portal. including what to call each file and where to store it, preprocessing info and retrieval of the download url <br><br>
# 
#     - **NOTE**: you can call this function multiple times if you like in a loop for different parameters and extend the output list using the python function extend() to make one list for input into the follow up function *retrieve_wapor_rasters*<br><br>
# 
# - *retrieve_actual_wapor_rasters*: retrieval of the actual rasters using the url provided by *retrieve_wapor_download_info* as well as all preprocessing of the rasters according to the information found in the dictionaries returned by *retrieve_wapor_download_info*. the standardised file paths provided in the dictionaries also allow previosly donwloaded files to be found and skipped. <br><br> 
# 
# The reason why *download_wapor_rasters* is split between two subfunctions (aside from better coding practices) is so that you can retrieve different sets of download info and group them together. That way you can make multiple calls to *retrieve_wapor_download_info* with different parameters and then retrieve and format the retrieved rasters all at the same time in the same way using *retrieve_actual_wapor_rasters*.

# ***
# ### 4.1 download rasters from the WAPOR portal
# 
# to run the **WaporRetrieval** class function *download_wapor_rasters* you need to provide the following inputs:
# 
# #### Required Inputs:
# 
# - **datacomponents**: datacomponents (parameters of interest such as transpiration and net primary productivity) to download data for. These are input as single letter code strings seperated by a ',' in a list such as: ['T', 'NPP']. if you set the datacomponents input to ['ALL'] it will download all datacomponents available for that return period and level at that location.<br><br>
# 
# 
# #### Optional Inputs:
# 
# - **period_start**: date you want to start your data download from, enter as a datetime object. This could also have been provided when intitiating the class.<br><br>
# 
# - **period_end**: date you want to end your data download at, enter as a datetime object. This could also have been provided when intitiating the class.<br><br>
# 
#     - NOTE: see the class explanation above for more details on *datetime objects*<br><br>
# 
# - **return_period**: return period to download data for, given as a single letter code. available periods include: I: Daily, D: Dekadal, S: Seasonal, A: Annual (yearly). This could also have been provided when intitiating the class.<br><br>
# 
# - **template_raster_path**: if provided uses the raster as a template and matches the diemansions of all retrieved rasters to this raster, also masks all retrieved rasters too this raster. If not provided the first downloaded raster in the download list is automatically used as the template raster<br>
# 
#     - NOTE: make sure you provide a matching aoi_name name if you provide a template raster yourself<br><br>
# 
# - **aoi_name**: this is the subfolder where processed data is stored, in case no name is provided it is auto set to nomask. If there is already data in the mask folder the download will not occur as it assumes data already exists.<br><br>
# 
#     - NOTE: The purpose of the aoi_name is so that you can carry out an analysis in the same area (bbox) for multiple different masks, skipping the download. downloaded rasters are maintained therefore the user can skip the download when carrying out an analysis for a new aoi (mask) in the same area (bbox) <br><br>
# 
# - **output_nodata**: nodata value to use for the retrieved rasters auto set to -9999<br>
# 
# #### Output:
# 
# - a python dictionary containing python dictionaries. Each dictionary named after a datacomponent and each one containing a list of rasters downloaded for that datacomponent 
# 
#     - NOTE: a raster list consists of all the rasters found for a datacomponent between the two period dates given at the interval specified by the reurn period and the path to a vrt that compiles all those rasters into one.

# In[29]:


# run the code and download rasters from the wapor portal
retrieved_rasters = retrieval.download_wapor_rasters(
  datacomponents=['AETI'])

# see next code cell for the results 


# In[ ]:


# print the list of retrieved rasters for AETI
print('retrieved AETI rasters:\n {} \n'.format(retrieved_rasters['AETI']['raster_list']))

# print the path to the AETI vrt
print('path to the retrieved AETI vrt:\n {}'.format(retrieved_rasters['AETI']['vrt_path']))


# ***
# ## 5. Check out the data 
# 
# if the code ran succesfully you should be able to find the data in the subfolders under the folders: <br>
# 
# - *{wapor_directory}/{project_name>}/L{number}/02_download* <br><br>
# 
# - *{wapor_directory}/{project_name}/L{number}/03_masked*<br>
# 
# there is also the folder: <br>
# 
# - *{wapor_directory}/{project_name}/L{number}/01_temp*<br>
# 
# unedited data is placed here temporarily while downloading. If the download process is successful the data here is automatically deleted. So in the case of an error during the download, part of the data may be found here.
# 
# You can check the data using a program such as Qgis or arcGIS or however you want.
# 
# ***
# 

# ***
# ## The next step: statistics
# 
# to analyse the data retrieved using this notebook check out the notebook *01B_basic_statistical_analysis_and_plotting.ipynb* on how to  analyze the data retrieved and produce some statistics
