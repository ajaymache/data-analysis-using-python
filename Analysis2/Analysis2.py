
# coding: utf-8

# # Analysis 2

# In[7]:

# get_ipython().magic('matplotlib inline')


# In[2]:

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


# In[3]:

# absolute path till parent folder
abs_path = os.getcwd()
path_array = abs_path.split("/")
path_array = path_array[:len(path_array)-1]
homefolder_path = ""
for i in path_array[1:]:
    homefolder_path = homefolder_path + "/" + i 


# In[6]:

# path to clean data
clean_data_path = homefolder_path + "/CleanData/CleanedDataSet/cleaned_autos.csv"

# reading csv into raw dataframe
df = pd.read_csv(clean_data_path,encoding="latin-1")


# ## No of Vehicles by Brand Available on ebay for sale

# In[50]:

# Count plot to show the number of vehicles belonging to each brand
sns.set_style("whitegrid")
g = sns.factorplot(y="brand", data=df, kind="count",
                   palette="Reds_r", size=7, aspect=1.5)
g.ax.set_title("Count of vehicles by Brand",fontdict={'size':18})
# for p in g.ax.patches:
#      g.ax.annotate((p.get_width()), (p.get_width()-0.1, p.get_y()-0.1))


# In[51]:

# saving the plot
g.savefig((abs_path + "/Plots/brand-vehicleCount.png"))


# ## Average price for vehicles based on the type of vehicle as well as on the type of gearbox

# In[62]:

fig, ax = plt.subplots(figsize=(8,5))
colors = ["#00e600", "#ff8c1a","#a180cc"]
sns.barplot(x="vehicleType", y="price",hue="gearbox", palette=colors, data=df)
ax.set_title("Average price of vehicles by vehicle type and gearbox type")
plt.show()


# In[64]:

# saving the plot
fig.savefig((abs_path + "/Plots/vehicletype-gearbox-price.png"))


# In[ ]:



