
# coding: utf-8

# # Analysis 1

# ## Some general analysis encountered during Data Cleaning

# In[24]:

#get_ipython().magic('matplotlib inline')


# In[19]:

# importing required libraries
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
sns.set(style="white")


# In[20]:

# absolute path till parent folder
abs_path = os.getcwd()
path_array = abs_path.split("/")
path_array = path_array[:len(path_array)-1]
homefolder_path = ""
for i in path_array[1:]:
    homefolder_path = homefolder_path + "/" + i   


# In[22]:

# path to clean data
clean_data_path = homefolder_path + "/CleanData/CleanedDataSet/cleaned_autos.csv"

# reading csv into raw dataframe
df = pd.read_csv(clean_data_path,encoding="latin-1")


# ## Distribution of Vehicles based on Year of Registration

# In[64]:

# Distribution of vehicles based on year of registration
fig, ax = plt.subplots(figsize=(8,6))
sns.distplot(df["yearOfRegistration"], color="#33cc33",kde=True, ax=ax)
ax.set_title('Distribution of vehicles based on Year of Registration', fontsize= 15)
plt.ylabel("Density (KDE)", fontsize= 15)
plt.xlabel("Year Of Registration", fontsize= 15)
plt.show()


# In[33]:

# saving the plot
fig.savefig(abs_path + "/Plots/vehicle-distribution.png")


# ## Variation of the price range by the vehicle type

# In[44]:

# Boxplot to see the distribution after outliers has been removed
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x="vehicleType", y="price", data=df)
ax.text(5.25,27000,"Boxplot After removing outliers",fontsize=18,color="r",ha="center", va="center")
plt.show()


# In[45]:

# saving the plot
fig.savefig(abs_path + "/Plots/price-vehicleType-boxplot.png")


# ## Total count of vehicles by type available on ebay for sale

# In[53]:

# Count plot to show the number of vehicles belonging to each vehicleType
sns.set_style("white")
g = sns.factorplot(x="vehicleType", data=df, kind="count",
                   palette="BuPu", size=6, aspect=1.5)
# to get the counts on the top heads of the bar
for p in g.ax.patches:
    g.ax.annotate((p.get_height()), (p.get_x()+0.1, p.get_height()+500))


# In[54]:

# saving the plot
g.savefig(abs_path + "/Plots/count-vehicleType.png")


# In[ ]:



