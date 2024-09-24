#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Load the Excel file (update the path as needed)
file_path = r'D:\Thesis Work\charts\AgERA52.xlsx'
df_modified = pd.read_excel(file_path, sheet_name='Sheet1')

# Select the numerical variables for PCA
variables_modified = df_modified[['Humidity', 'Solar Radiation', 'Temperature Mean', 'Temperature Max',
                                  'Temperature Min', 'Wind Speed', 'Precipitation']]

# Standardize the data
scaler_modified = StandardScaler()
scaled_data_modified = scaler_modified.fit_transform(variables_modified)

# Perform PCA
pca_modified = PCA()
pca_data_modified = pca_modified.fit_transform(scaled_data_modified)

# Eigenvalues and PC Values Table
eigenvalues_modified = pca_modified.explained_variance_
pc_values_modified = pca_data_modified

# Loading scores (coefficients of the original variables)
loading_scores_modified = pca_modified.components_.T * np.sqrt(eigenvalues_modified)

# Covariance Matrix
cov_matrix_modified = np.cov(scaled_data_modified.T)

# Function to plot a clearer biplot with longer arrows
def biplot(score, coeff, pc_x=0, pc_y=1, labels=None, ax=None):
    ax.scatter(score[:, pc_x], score[:, pc_y], color='gray', s=50, alpha=0.7, label="PC scores")
    
    # Plot loadings (blue arrows)
    for i in range(coeff.shape[0]):
        ax.arrow(0, 0, coeff[i, pc_x], coeff[i, pc_y], color='blue', alpha=0.8, 
                 head_width=0.2, head_length=0.5, linewidth=1.5)
        ax.text(coeff[i, pc_x] * 8.15, coeff[i, pc_y] * 7.15, labels[i], 
                color='blue', ha='center', va='center', fontsize=12)
    
    ax.set_xlabel(f"PC{pc_x+1}")
    ax.set_ylabel(f"PC{pc_y+1}")
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()

# Create subplots for the first three components
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot the first two principal components in the first subplot
biplot(pca_data_modified, np.transpose(pca_modified.components_), 0, 1, labels=variables_modified.columns, ax=axes[0])

# Plot PC1 vs PC3 in the second subplot
biplot(pca_data_modified, np.transpose(pca_modified.components_), 0, 2, labels=variables_modified.columns, ax=axes[1])

# Plot PC2 vs PC3 in the third subplot
biplot(pca_data_modified, np.transpose(pca_modified.components_), 1, 2, labels=variables_modified.columns, ax=axes[2])

plt.tight_layout()
plt.show()

# Show tables and the biplot
eigenvalues_table_modified = pd.DataFrame(eigenvalues_modified, columns=["Eigenvalues"])
pc_values_table_modified = pd.DataFrame(pc_values_modified, columns=[f"PC{i+1}" for i in range(pc_values_modified.shape[1])])
loading_scores_table_modified = pd.DataFrame(loading_scores_modified, index=variables_modified.columns, columns=[f"PC{i+1}" for i in range(loading_scores_modified.shape[1])])
cov_matrix_table_modified = pd.DataFrame(cov_matrix_modified, index=variables_modified.columns, columns=variables_modified.columns)

# Print the tables
print("Eigenvalues and PC Values Table:")
print(eigenvalues_table_modified)

print("\nLoading Score Table:")
print(loading_scores_table_modified)

print("\nCovariance Matrix Table:")
print(cov_matrix_table_modified)


# In[ ]:




