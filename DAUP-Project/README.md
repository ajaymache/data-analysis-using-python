# Data Analysis for used car dataset
## DataSet Overview
###### The dataset is taken from kaggle and contains details of the used cars in germany which are on sail on ebay. The dataset is not clean and hence a lot of data cleaning is carried out. For e.g. prices where too high which are replaced by the median and outliers are removed accordingly. Also vehicles whose registration year was greater than 2016 and less than 1890 were removed from the dataset as this data is inconsistense and would yield incorrect results.
###### The dataset is cleaned and stored in a CleanDataset folder which contains the entire cleaned dataset named as cleaned_autos.csv and another folder containing files structures containing subsets of the cleaned dataset based on brand of the vehicles and vehicle types.
##### Sample Dataset
![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/DataPreparation/Plots/Screen%20Shot%202016-12-10%20at%2012.04.52%20PM.png "Logo Title Text 1")
## More Info
#### The main folder contains 9 folders.
###### Folders from Analysis1 - Analysis5 contain the iPython Notebook along with the Plots for that analysis.
###### Folder for shell scripts which automate the entire for creating files structures and splitting the data as mentioned above.
###### Datapreparation folder contains the Datapreparation iPython Notebook for cleaning of data.
###### CleanData folder contains the clean dataset and subsets of data as per the file structure.
###### RawData folder which contains the raw dataset.
## Analysis 1
###### This analysis gives the distribution of prices of vehicles based on vehicles types. Output before the cleaning the data is shown below in order to highlight the importance of cleaning this dataset.
![alt text](https://github.com/ajaymache/DataAnalysisUsingPython/blob/master/DAUP-Project/DataPreparation/Plots/Screen%20Shot%202016-12-10%20at%2012.04.52%20PM.png "Logo Title Text 1")
