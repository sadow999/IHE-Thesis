#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (replace with your file path if necessary)
file_path = r"D:\Thesis Work\MACHINE LEARNING\PCA_Final_Analysis_Manual.xlsx"
df = pd.read_excel(file_path, sheet_name='Original Data')

# Drop the 'Date' column since it's not needed for correlation analysis
df = df.drop(columns=['Date'])

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[ ]:




