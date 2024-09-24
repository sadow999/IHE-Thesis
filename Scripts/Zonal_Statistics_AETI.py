#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import numpy as np
import pandas as pd
import tifffile as tiff  # Use tifffile instead of Pillow for reading TIFF images

# Define the class values for all crops (normal and irrigated variants)
crop_classes = {
    "Potato": [10, 110],
    "Orchard (dense)": [13, 113],
    "Grapes": [15, 115],
    "Wheat": [108],
    "Maize": [109],
    "Potatoes": [110],
    "Grapes (Irrigated)": [115],
    "Rice": [120],
    "Cotton": [124],
    "Clover": [125],
    "Onions": [126],
    "Carrots": [127],
    "Eggplants": [128],
    "Flax": [129],
    "Sugar beet": [131]
}

# Directories containing the AETI and Land Classification files
aeti_dir = r'D:\Thesis Work\FAO_WAPOR_Data\waporact_test\L3\02_download\L3_AETI_D'
land_class_dir = r'D:\Thesis Work\FAO_WAPOR_Data\waporact_test\L3\02_download\L3_LCC_D'

# Initialize a list to store the results
results = []

# List files in both directories
aeti_files = os.listdir(aeti_dir)
land_class_files = os.listdir(land_class_dir)

# Extract the number after AETI and LCC in filenames for pairing
def extract_number(filename, prefix):
    start = filename.find(prefix) + len(prefix)
    end = filename.find('.tif', start)
    return filename[start:end]

# Create a dictionary for land class files with extracted numbers as keys
land_class_dict = {extract_number(f, 'LCC_'): f for f in land_class_files if f.endswith('.tif')}

# Function to process each pair of AETI and Land Classification files
def process_files(aeti_file, land_class_file):
    # Load the images using tifffile
    aeti_data = tiff.imread(aeti_file)
    land_class_data = tiff.imread(land_class_file)
    
    # Dictionary to store the average AETI for each crop
    crop_aeti_values = {}
    
    # Iterate over all crops
    for crop_name, class_values in crop_classes.items():
        # Identify pixels corresponding to the crop in the land classification image
        crop_pixels = np.isin(land_class_data, class_values)
        
        # Extract the corresponding AETI values for the crop
        crop_aeti = aeti_data[crop_pixels]
        
        # Filter out no-data values (assuming -9999.0 is a no-data value)
        valid_crop_aeti = crop_aeti[crop_aeti != -9999.0]
        
        # Sum and then average the AETI values for the crop
        if valid_crop_aeti.size > 0:
            avg_aeti = np.mean(valid_crop_aeti)
        else:
            avg_aeti = np.nan
        
        crop_aeti_values[crop_name] = avg_aeti
    
    return crop_aeti_values

# Iterate through the AETI files and find the corresponding land class files
for aeti_filename in aeti_files:
    if aeti_filename.endswith('.tif'):
        # Extract the number from the AETI filename
        number = extract_number(aeti_filename, 'AETI_')
        
        # Find the corresponding land class filename using the extracted number
        land_class_filename = land_class_dict.get(number)
        
        if land_class_filename:
            # Construct the full file paths
            aeti_file_path = os.path.join(aeti_dir, aeti_filename)
            land_class_file_path = os.path.join(land_class_dir, land_class_filename)
            
            # Process the files and calculate the combined average AETI for each crop
            crop_aeti_values = process_files(aeti_file_path, land_class_file_path)
            
            # Assuming that date extraction should be updated to match your file naming convention
            date = number
            
            # Append the results to the list with the date
            for crop_name, avg_aeti in crop_aeti_values.items():
                results.append({
                    'Date': date,
                    'Crop': crop_name,
                    'Average AETI': avg_aeti
                })
            print(f"Processed {aeti_filename} and {land_class_filename}")
        else:
            print(f"Matching land class file not found for {aeti_filename}")

# Convert the results list to a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a CSV file
results_df.to_csv('average_aeti_all_crops.csv', index=False)
print("Results saved to average_aeti_all_crops.csv")


# In[4]:


import os
import numpy as np
import pandas as pd
import tifffile as tiff  # Use tifffile instead of Pillow for reading TIFF images

# Define the class values for all crops (normal and irrigated variants)
crop_classes = {
    "Potato": [10, 110],
    "Orchard (dense)": [13, 113],
    "Grapes": [15, 115],
    "Wheat": [108],
    "Maize": [109],
    "Potatoes": [110],
    "Grapes (Irrigated)": [115],
    "Rice": [120],
    "Cotton": [124],
    "Clover": [125],
    "Onions": [126],
    "Carrots": [127],
    "Eggplants": [128],
    "Flax": [129],
    "Sugar beet": [131]
}

# File selection based on user preference for each season
file_selection = {
    "Winter": "L3_AETI_2228.tif",  # File for Winter
    "Summer": "L3_AETI_2216.tif",  # File for Summer
    "Nili": "L3_AETI_2221.tif"     # File for Nili
}

# Directories containing the AETI and Land Classification files
aeti_dir = r'D:\Thesis Work\FAO_WAPOR_Data\waporact_test\L3\02_download\L3_AETI_D'
land_class_dir = r'D:\Thesis Work\FAO_WAPOR_Data\waporact_test\L3\02_download\L3_LCC_D'

# Initialize a list to store the results
results = []

# Extract the number after AETI and LCC in filenames for pairing
def extract_number(filename, prefix):
    start = filename.find(prefix) + len(prefix)
    end = filename.find('.tif', start)
    return filename[start:end]

# Create a dictionary for land class files with extracted numbers as keys
land_class_files = os.listdir(land_class_dir)
land_class_dict = {extract_number(f, 'LCC_'): f for f in land_class_files if f.endswith('.tif')}

# Function to process each pair of AETI and Land Classification files
def process_files(aeti_file, land_class_file):
    # Load the images using tifffile
    aeti_data = tiff.imread(aeti_file)
    land_class_data = tiff.imread(land_class_file)

    # Dictionary to store the pixel count for each crop
    crop_pixel_counts = {}

    # Check if both images have the same shape
    if aeti_data.shape != land_class_data.shape:
        print(f"Shape mismatch: AETI {aeti_data.shape}, Land Classification {land_class_data.shape}")
        return None  # Skip processing this pair
    
    # Iterate over all crops
    for crop_name, class_values in crop_classes.items():
        # Identify pixels corresponding to the crop in the land classification image
        crop_pixels = np.isin(land_class_data, class_values)
        
        # Count the number of pixels for this crop
        crop_pixel_count = np.sum(crop_pixels)
        crop_pixel_counts[crop_name] = crop_pixel_count
    
    return crop_pixel_counts

# Initialize a dictionary to store seasonal pixel counts for each crop
seasonal_crop_data = {season: {crop: 0 for crop in crop_classes} for season in file_selection}

# Iterate through the files selected for each season
for season, aeti_filename in file_selection.items():
    aeti_file_path = os.path.join(aeti_dir, aeti_filename)
    
    # Extract the number from the AETI filename
    number = extract_number(aeti_filename, 'AETI_')
    
    # Find the corresponding land class filename using the extracted number
    land_class_filename = land_class_dict.get(number)
    
    if land_class_filename:
        # Construct the full path for the land class file
        land_class_file_path = os.path.join(land_class_dir, land_class_filename)
        
        # Process the files and get the pixel counts for each crop
        crop_pixel_counts = process_files(aeti_file_path, land_class_file_path)
        
        # If no crop pixels were found, skip to the next file
        if crop_pixel_counts is None:
            continue
        
        # Add the pixel counts to the corresponding season's data
        for crop_name, pixel_count in crop_pixel_counts.items():
            seasonal_crop_data[season][crop_name] += pixel_count
        
        print(f"Processed {aeti_filename} and {land_class_filename} for {season} season")
    else:
        print(f"Matching land class file not found for {aeti_filename}")

# Check if any data was processed
if not any(any(v > 0 for v in crops.values()) for crops in seasonal_crop_data.values()):
    print("No valid data was processed.")
else:
    # Convert the seasonal crop data to percentages
    seasonal_results = []
    for season, crops_data in seasonal_crop_data.items():
        total_pixels = sum(crops_data.values())
        
        if total_pixels > 0:  # Avoid division by zero
            for crop_name, pixel_count in crops_data.items():
                crop_percentage = (pixel_count / total_pixels) * 100
                seasonal_results.append({
                    'Season': season,
                    'Crop': crop_name,
                    'Crop Percentage': crop_percentage
                })

    # Convert the results to a DataFrame
    seasonal_results_df = pd.DataFrame(seasonal_results)

    # Save the seasonal crop percentages to a CSV file
    seasonal_results_df.to_csv('seasonal_crop_percentages.csv', index=False)
    print("Seasonal crop percentages saved to seasonal_crop_percentages.csv")


# In[ ]:




