# Data Analysis Of Used Car Dataset
### DataSet Overview
  + The dataset is taken from **kaggle** and contains details of the **used cars in germany** which are on sale on **ebay**.
  + The dataset is not clean and hence a lot of data cleaning is carried out. For e.g. prices where too high which are      replaced by the median and outliers are removed accordingly. 
  + Also vehicles whose registration year was **_greater than 2016_ and _less than 1890_** were removed from the dataset as this data is inconsistense and would yield incorrect results.
  + The dataset is cleaned and stored in a **CleanData** folder which contains the entire cleaned dataset named as **[cleaned_autos.csv](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/CleanData/CleanedDataSet)** and another folder named **[DataForAnalysis](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/CleanData/DataForAnalysis)** containing files structures containing subsets of the cleaned dataset based on brand of the vehicles and vehicle types.  
  
### Sample Dataset
dateCrawled | name | seller | offerType | price | abtest | vehicleType | yearOfRegistration | gearbox | powerPS | model | kilometer | monthOfRegistration | fuelType | brand | notRepairedDamage | dateCreated | nrOfPictures | postalCode | lastSeen 
--- | --- | --- | --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
2016-03-24 11:52:17 | Golf_3_1.6 | privat | Angebot | 480 | test | nan | 1993 | manuell | 0 | golf | 150000 | 0 | benzin | volkswagen | nan | 2016-03-24 00:00:00 | 0 | 70435 | 2016-04-07 03:16:57
2016-03-24 10:58:45 | A5_Sportback_2.7_Tdi | privat | Angebot | 18300 | test | coupe | 2011 | manuell | 190 | nan | 125000 | 5 | diesel | audi | ja | 2016-03-24 00:00:00 | 0 | 66954 | 2016-04-07 01:46:50
2016-03-14 12:52:21 | Jeep_Grand_Cherokee_"Overland" | privat | Angebot | 9800 | test | suv | 2004 | automatik | 163 | grand | 125000 | 8 | diesel | jeep | nan | 2016-03-14 00:00:00 | 0 | 90480 | 2016-04-05 12:47:46
***
### More Info
__*The main folder contains 9 folders*__.

  + Folders from Analysis1 - Analysis5 contain the **iPython Notebook**, **python scripts** along with the **Plots** for that analysis.
  + Folder for **[shell scripts](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/ShellScripts)** which automate the creatinn of files structures and splitting the data as mentioned above.
  + Datapreparation folder contains the **[Datapreparation iPython Script](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/DataPreparation/DataPreparation.py)** for cleaning of data.
  + CleanData folder contains the clean dataset and subsets of data as per the **[file structure](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/CleanData/DataForAnalysis)**.
  + RawData folder which contains the **[raw dataset](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/RawData)**.  <br/>
 
***
### Analysis 1 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Analysis1.py](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis1/Analysis1.py)&emsp;[Analysis1.ipynb](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis1/Analysis1.ipynb)&emsp;[Plots](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/Analysis1/Plots)
+ This analysis gives the distribution of prices of vehicles based on vehicles types.
+ Output before the cleaning the data is shown below in order to highlight the importance of cleaning this dataset.
+ **Histogram** and **KDE** before performing data cleaning.
+ It is clearly visible that the dataset has **many outliers** and **inconsistent data** as year of registration **cannot be more than 2016 and less than 1890**.

![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/DataPreparation/Plots/vehicle-distribution.png "Logo Title Text 1")

> Boxplot of prices of vehicles based on the type of vehicles after cleaning the dataset. Based on the vehicle type how the prices vary is depictable from the boxplot. low, 25th, 50th(Median), 75th percentile, high can be estimated from this boxplot.

![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis1/Plots/price-vehicleType-boxplot.png "Logo Title Text 1")
***
### Analysis2 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Analysis2.py](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis2/Analysis2.py)&emsp;[Analysis2.ipynb](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis2/Analysis2.ipynb)&emsp;[Plots](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/Analysis2/Plots)

+ This analysis gives the number of cars which are available for sale in the entire dataset based on a particular brand. 

![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis2/Plots/brand-vehicleCount.png "Logo Title Text 1")

> Barplot of average price of the vehicles for sale based of the type of the vehicle as well as based on the gearbox of the vehicle.

![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis2/Plots/vehicletype-gearbox-price.png "Logo Title Text 1")
***
### Analysis 3 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Analysis3.py](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis3/Analysis3.py)&emsp;[Analysis3.ipynb](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis3/Analysis3.ipynb)&emsp;[Plots](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/Analysis3/Plots)

+ This analysis gives the average number of price for the vehicles based on the fueltype of the vehicle and also based on the type of the vehicle.

![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis3/Plots/fueltype-vehicleType-price.png "Logo Title Text 1")

> Barplot of average power of the vehicle based of the fueltype of the vehicle and also on the type of the vehicle.

![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis3/Plots/power-vehicleType-fuelType.png "Logo Title Text 1")
***
### Analysis 4 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Analysis4.py](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis4/Analysis4.py)&emsp;[Analysis4.ipynb](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis4/Analysis4.ipynb)&emsp;[Plots](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/Analysis4/Plots)

+ This analysis gives you the average price of the brand of vehicles and their types which are likely to be found in the dataset.

![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis4/Plots/heatmap-price-brand-vehicleType.png "Logo Title Text 1")
***
### Analysis 5 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Analysis5.py](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis5/Analysis5.py)&emsp;[Analysis5.ipynb](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis5/Analysis5.ipynb)&emsp;[Plots](https://github.com/ajaymache/DataAnalysisUsingPython/tree/master/DAUP-Project/Analysis5/Plots)

+ This analysis gives you the distribution of the total no of days a partiular vehicle has been online for sale before it was purchased. 
+ This is a **dynamic analysis** and can be applied to **any vehicle** by specifying the brand of choice as argument to the python script.
+ To run this file on your terminal type: __*Analysis5.py 'brand'*__  
+ where **'brand'** is the choice of brand vehicle you would like to see analysis about from the column **'brand'** in the dataset.

![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis5/Plots/vehicletype-NoOfDaysOnline.png "Logo Title Text 1")
***




