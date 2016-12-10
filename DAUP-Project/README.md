# Data Analysis of used car dataset

## Info About Dataset
###### The dataset has been taken from kaggle and comprises of used vehicles from all over germany which are on sale on ebay. 
###### The dataset has several missing values and many outliers, hence a lot of data has been cleansed.
###### As the dataset is big it is divided into subsets of data based on brand of vehicles and further on the type of vehicles. 
##### Eg: Brands like Audi, Bmw, Land Rover etc and Vehicle Types as Limosine, Bus, SUV, Coupe etc

## More Info
#### There are 9 Folders under the main folder
###### 5 folders for Analysis1 - Analysis5 which contains the iPython Notebbok for the analysis and a Plots folder for the analysis carried out
###### DataPreparation folder
###### Folder for RawData
###### Folder for Cleaned Data which consists of the entire cleaned dataset named as cleaned_autos.csv and another subfolder consisting of the subsets made as per brands and vehicle types
###### Folder for shell scripts which automate the creation of data structure and also subsets the dataset as said above
## Analysis 1
###### This gives the distribution for the prices of the vehicles which varies over vehicle type. This plot is achieved after cleaning a lot data without which the boxplot was barely visible due to a lot of outliers.
#### Histogram Indicating a lot outliers and inconsistent data as car registration year cannot be greater than 2016 and less than 1890 (assuming the first car ever made was in 1885)
![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/DataPreparation/Plots/vehicle-distribution.png "Logo Title Text 1")
#### Boxplot after cleaning the data
![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/Analysis1/Plots/price-vehicleType-boxplot.png "Logo Title Text 1")
