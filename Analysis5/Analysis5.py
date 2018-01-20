
# coding: utf-8

# # Analysis 5

# In[1]:

#get_ipython().magic('matplotlib inline')


# In[6]:

# importing required libraries
import os
import sys
import subprocess
import stat
import glob
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


# In[4]:

# path to clean data
clean_data_path = homefolder_path + "/CleanData/CleanedDataSet/cleaned_autos.csv"

# reading csv into raw dataframe
df = pd.read_csv(clean_data_path,encoding="latin-1")


# In[9]:

# concatinating files of the same brand 
search_term = str(sys.argv[1])
# search_term = "audi"
path = homefolder_path + "/CleanData/DataForAnalysis/" + search_term # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)


# In[15]:

frame.head(2)


# In[28]:

# colors = ["#47d147", "#ff8c1a","#a180cc"]
colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
fig, ax = plt.subplots(figsize=(8,5))
sns.set_palette(sns.xkcd_palette(colors))
sns.stripplot(x="vehicleType", y="NoOfDaysOnline", hue="gearbox", split=True, data=frame,size=8, alpha=0.5, jitter=True)
ax.set_title("No of days a add is online before the vehicles of brand " + search_term + " is sold")
plt.show()


# In[27]:

fig.savefig((abs_path + "/Plots/vehicletype-NoOfDaysOnline.png"))


# In[ ]:



