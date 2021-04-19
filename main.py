###### REAL WORLD SCENARIO ################################################################################################################
# The aim of this project is going to be a very high-level Exploratory Data of the Merseyside Crime data
# The data is from Summer 2019 & 2020 to enable an analysis to be completed between the two time periods - summer 2019 vs Summer 2020
#The goal is to see if COVID-19 had any appreciable affect on the Merseyside crime stats?
# I will import the data, clean it, shape it before displaying it.

# Setting up the project by importing packages for the basic python operations
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

############### CREATE REUSEABLE CODE #########################################################################################################################
#create a function to validate the struture and content of a dataframe
def ValidateDataFrameDetails (dfInput) :
#check the shape of the data
    print('Dataframe Shape')
    print(dfInput.shape)
    # print the first 10 rows of the dataset to have a look at the data
    print('')
    print('Dataframe Head - 10 Rows')
    print(dfInput.head(10))
    # print the tail the last 5 rows of the dataset to have a look at the last records in the dataset
    print('')
    print('Dataframe Tail - 5 Rows')
    print(dfInput.tail())
    # describing the dataset
    print('')
    print('Dataframe Describe')
    print(dfInput.describe())
    # Print the names of the columns of the dataset
    print('')
    print('Dataframe Columns')
    print(dfInput.columns)
    # Print the names of the columns of the dataset
    print('')
    print('Dataframe Types')
    print(dfInput.dtypes)
    # Check for Null Values and Sum the Null Values
    print('')
    print('Dataframe Null Value Check')
    print(dfInput.isnull())
    print('')
    print('Dataframe Null Value Sum')
    print(dfInput.isnull().sum())
    # Check for Null Values and Sum the Null Values
    #Next we will check for duplicates
    print('')
    print('Dataframe Duplicate Check')
    print(dfInput[dfInput.duplicated()])
    #Inserted line spaces & end of Function identfier to aid validation where the function is called namerous times together in the code
    print('')
    print('End Of Function ---------------------------------------')
    print('')

############### IMPORTING DATA the datasets ###################################################################################################################
###### IMPORTING JUNE 2019 DATASET
# I will start by importing the crime dataset for July 2019 and looking at the first 5 rows to understand the dataset
df1906 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2019-06-merseyside-street.csv")

# check the shape of the dataframes & validate the contents by calling the ValidateDataFrameDetails Function
#ValidateDataFrameDetails(df1906)  #commented out as I validated the structure is correct

###### ANALYZING THE DATA - REMOVING IRRELEVANT COLUMNS FROM THE  DATASETS
# Having evaluated the data the next step is to decide what data is required for the analysis - 'Month', 'LSOA code', 'LSOA name' & 'Crime Type'
df1906.drop(df1906.columns[[0,2,3,4,5,6,10,11]],axis=1,inplace=True) #'Crime ID','Reported by','Falls within','Longitude','Latitude','Location','Last outcome category','Context'

# Call the ValidateDataFrameDetails Function again to ensure the changed have been applied
#ValidateDataFrameDetails(df1906)  #commented out as I validated the structure is correct

###### IMPORTING JULY & AUGUST 2019 DATASET
# Repeat the process for July & August 2019 - they will be saved into separate dataframes as June 2019 has been validated
df1907 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2019-07-merseyside-street.csv")
df1908 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2019-08-merseyside-street.csv")

# check the shape of the dataframes & validate the contents by calling the ValidateDataFrameDetails Function
#ValidateDataFrameDetails(df1907)  #commented out as I validated the structure is correct - dataframe created correctly
#ValidateDataFrameDetails(df1908)  #commented out as I validated the structure is correct - dataframe created correctly

###### ANALYZING THE DATA - REMOVING IRRELEVANT COLUMNS FROM THE  DATASETS
# Having evaluated the data the next step is to decide what data is required for the analysis - 'Month', 'LSOA code', 'LSOA name' & 'Crime Type'
df1907.drop(df1907.columns[[0,2,3,4,5,6,10,11]],axis=1,inplace=True) #'Crime ID','Reported by','Falls within','Longitude','Latitude','Location','Last outcome category','Context'
df1908.drop(df1908.columns[[0,2,3,4,5,6,10,11]],axis=1,inplace=True) #'Crime ID','Reported by','Falls within','Longitude','Latitude','Location','Last outcome category','Context'
#After the unwanted columns are dropped we will have a clean dataset for July & August 2019 records

# Call the ValidateDataFrameDetails Function again to ensure the changed have been applied
#ValidateDataFrameDetails(df1907)  #commented out as I validated the structure is correct - correct colums dropped
#ValidateDataFrameDetails(df1908)  #commented out as I validated the structure is correct - correct columns dropped

###### IMPORTING JUNE, JULY & AUGUST 2020 DATASET
# Having validated the data for 2019 - I have now imported the data for 2020 - June, July & August - validating the data as I load it
df2006 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2020-06-merseyside-street.csv")
df2007 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2020-07-merseyside-street.csv")
df2008 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2020-08-merseyside-street.csv")

# check the shape of the dataframes & validate the contents by calling the ValidateDataFrameDetails Function
#ValidateDataFrameDetails(df2006)  #commented out as I validated the structure is correct - dataframe created correctly
#ValidateDataFrameDetails(df2007)  #commented out as I validated the structure is correct - dataframe created correctly
#ValidateDataFrameDetails(df2008)  #commented out as I validated the structure is correct - dataframe created correctly

###### ANALYZING THE DATA - REMOVING IRRELEVANT COLUMNS FROM THE  DATASETS
# Having evaluated the data the next step is to decide what data is required for the analysis - 'Month', 'LSOA code', 'LSOA name' & 'Crime Type'
df2006.drop(df2006.columns[[0,2,3,4,5,6,10,11]],axis=1,inplace=True) #'Crime ID','Reported by','Falls within','Longitude','Latitude','Location','Last outcome category','Context'
df2007.drop(df2007.columns[[0,2,3,4,5,6,10,11]],axis=1,inplace=True) #'Crime ID','Reported by','Falls within','Longitude','Latitude','Location','Last outcome category','Context'
df2008.drop(df2008.columns[[0,2,3,4,5,6,10,11]],axis=1,inplace=True) #'Crime ID','Reported by','Falls within','Longitude','Latitude','Location','Last outcome category','Context'
#After the unwanted columns are dropped we will have a clean dataset for July & August 2019 records

# Call the ValidateDataFrameDetails Function again to ensure the changed have been applied
#ValidateDataFrameDetails(df2006)  #commented out as I validated the structure is correct - dataframe created correctly
#ValidateDataFrameDetails(df2007)  #commented out as I validated the structure is correct - dataframe created correctly
#ValidateDataFrameDetails(df2008)  #commented out as I validated the structure is correct - dataframe created correctly

###### ANALYZING THE DATA - SORTING THE DATASETS
# Next I want to sort the data to made it easier to interpret
df1906_sorted = df1906.sort_values(by=['LSOA code','Crime type'],ascending=True)
#ValidateDataFrameDetails(df1906_sorted)  #commented out as I validated the structure is correct - dataframe created correctly & sorted correctly
df1907_sorted = df1907.sort_values(by=['LSOA code','Crime type'],ascending=True)
#ValidateDataFrameDetails(df1907_sorted)  #commented out as I validated the structure is correct - dataframe created correctly & sorted correctly
df1908_sorted = df1908.sort_values(by=['LSOA code','Crime type'],ascending=True)
#ValidateDataFrameDetails(df1908_sorted)  #commented out as I validated the structure is correct - dataframe created correctly & sorted correctly

df2006_sorted = df2006.sort_values(by=['LSOA code','Crime type'],ascending=True)
#ValidateDataFrameDetails(df2006_sorted)  #commented out as I validated the structure is correct - dataframe created correctly & sorted correctly
df2007_sorted = df2007.sort_values(by=['LSOA code','Crime type'],ascending=True)
#ValidateDataFrameDetails(df2007_sorted)  #commented out as I validated the structure is correct - dataframe created correctly & sorted correctly
df2008_sorted = df2008.sort_values(by=['LSOA code','Crime type'],ascending=True)
#ValidateDataFrameDetails(df2008_sorted)  #commented out as I validated the structure is correct - dataframe created correctly & sorted correctly

###### ANALYZING DATA - ADDING THE THREE DATAFRAMES TOGETHER TO CREATE A SINGLE 2019 VIEW OF THE ORIGIONAL DATA - using the sorted data frame as the basis
df2019_Merged_Origional = pd.concat([df1906_sorted,df1907_sorted,df1908_sorted],ignore_index=True)
#ValidateDataFrameDetails(df2019_Merged_Origional) #totals match - number of individual crime Types is 42,236; maup up of 13,297 (June), 14,534 (July) & 14,405(August)

df2020_Merged_Origional = pd.concat([df2006_sorted,df2007_sorted,df2008_sorted],ignore_index=True)
#ValidateDataFrameDetails(df2020_Merged_Origional) #totals match - number of individual crime Types is 45,243; maup up of 14,684 (June), 14,980 (July) & 15,579(August)


###### ANALYZING DATA - DROPPING DUPLICATED VALUES THROUGH CHANGING THE TABLE ORIENTATATION
# This will allow me to count the instances of crimes accross the LSOA areas

#manipulate the data by creating a column for each crime type
dfcount1906 = pd.crosstab([df1906_sorted['Month'], df1906_sorted['LSOA code'],df1906_sorted['LSOA name'] ], df1906_sorted['Crime type'])
dfcount1906.reset_index(inplace=True)
#ValidateDataFrameDetails(dfcount1906)  #commented out as I validated the structure is correct - we now have a cross tab with the crime types as column headers

dfcount1907 = pd.crosstab([df1907_sorted['Month'], df1907_sorted['LSOA code'],df1907_sorted['LSOA name'] ], df1907_sorted['Crime type'])
dfcount1907.reset_index(inplace=True)
#ValidateDataFrameDetails(dfcount1907)  #commented out as I validated the structure is correct - we now have a cross tab with the crime types as column headers

dfcount1908 = pd.crosstab([df1908_sorted['Month'], df1908_sorted['LSOA code'],df1908_sorted['LSOA name'] ], df1908_sorted['Crime type'])
dfcount1908.reset_index(inplace=True)
#ValidateDataFrameDetails(dfcount1908)  #commented out as I validated the structure is correct - we now have a cross tab with the crime types as column headers

dfcount2006 = pd.crosstab([df2006_sorted['Month'], df2006_sorted['LSOA code'],df2006_sorted['LSOA name'] ], df2006_sorted['Crime type'])
dfcount2006.reset_index(inplace=True)
#ValidateDataFrameDetails(dfcount2006)  #commented out as I validated the structure is correct - we now have a cross tab with the crime types as column headers

dfcount2007 = pd.crosstab([df2007_sorted['Month'], df2007_sorted['LSOA code'],df2007_sorted['LSOA name'] ], df2007_sorted['Crime type'])
dfcount2007.reset_index(inplace=True)
#ValidateDataFrameDetails(dfcount2007)  #commented out as I validated the structure is correct - we now have a cross tab with the crime types as column headers

dfcount2008 = pd.crosstab([df2008_sorted['Month'], df2008_sorted['LSOA code'],df2008_sorted['LSOA name'] ], df2008_sorted['Crime type'])
dfcount2008.reset_index(inplace=True)
#ValidateDataFrameDetails(dfcount2008)  #commented out as I validated the structure is correct - we now have a cross tab with the crime types as column headers

###### GET THHE TOTAL COUNT THE INSTANCES OF CRIME TYPE BY LOSA REGION #######   LOOPING WITH ITERROWS #####################################
#settimg an int variable to hold the total crimes for the file
TotalCrime = 0
for val, row in dfcount1906.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration  for June 2019 & add a column called Total
    dfcount1906.loc[val, "Total"] = crime

    # validate the variable is populating correctly for each LSOA & that there are no null values
    TotalCrime = crime + TotalCrime

#create a dictionary to stored the value of total crime for Jun 2019
dict_total_by_Month = {"06-2019":TotalCrime}

#Create a list to hold the totals in by Month - to be used in the Seaborn Visulations
list_month =[]
list_month_19 =[]
list_month.append(TotalCrime)
list_month_19.append(TotalCrime)

#validation of the figures
#print ("June 2019 - Total Crime " + str(TotalCrime))
#ValidateDataFrameDetails(dfcount1906)  #commented out as I validated the structure is correct - total column correct by row (LSOA area) and overall count

################ July 2019
TotalCrime = 0
for val, row in dfcount1907.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for July 2019 & add a column called Total
    dfcount1907.loc[val, "Total"] = crime
    TotalCrime = crime + TotalCrime

#Append to dictionary the value of total crime for Jul 2020 & append to the lists already created
dict_total_by_Month["07-2019"] = TotalCrime
list_month.append(TotalCrime)
list_month_19.append(TotalCrime)

#validate that the totals are correct
#print ("July 2019 - Total Crime " + str(TotalCrime))
#ValidateDataFrameDetails(dfcount1907)  #commented out as I validated the structure is correct - total column correct by row (LSOA area) and overall count

################ August 2019
TotalCrime = 0
for val, row in dfcount1908.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for August 2019 & add a column called Total
    dfcount1908.loc[val, "Total"] = crime
    TotalCrime = crime + TotalCrime

#Append to dictionary the value of total crime for Aug 2019 & append to the list already created
dict_total_by_Month["08-2019"] = TotalCrime
list_month.append(TotalCrime)
list_month_19.append(TotalCrime)

#print ("August 2019 - Total Crime " + str(TotalCrime))
#ValidateDataFrameDetails(dfcount1908)  #commented out as I validated the structure is correct - total column correct by row (LSOA area) and overall count

################ June 2020
#created new list for 2020
list_month_20 = []
TotalCrime = 0
for val, row in dfcount2006.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for June 2020 & add a column called Total
    dfcount2006.loc[val, "Total"] = crime
    TotalCrime = crime + TotalCrime

#Append to dictionary the value of total crime for Aug 2020
dict_total_by_Month["06-2020"] = TotalCrime
list_month.append(TotalCrime)
list_month_20.append(TotalCrime)

#print ("June 2020 - Total Crime " + str(TotalCrime))
#ValidateDataFrameDetails(dfcount2006)  #commented out as I validated the structure is correct - total column correct by row (LSOA area) and overall count

################ July 2020
TotalCrime = 0
for val, row in dfcount2007.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for July 2020 & add a column called Total
    dfcount2007.loc[val, "Total"] = crime
    TotalCrime = crime + TotalCrime

#Append to dictionary the value of total crime for Jun 2020
dict_total_by_Month["07-2020"] = TotalCrime
list_month.append(TotalCrime)
list_month_20.append(TotalCrime)

#print ("July 2020 - Total Crime " + str(TotalCrime))
#ValidateDataFrameDetails(dfcount2007)  #commented out as I validated the structure is correct - total column correct by row (LSOA area) and overall count

################ August 2020
TotalCrime = 0
for val, row in dfcount2008.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for August 2020 & add a column called Total
    dfcount2008.loc[val, "Total"] = crime
    TotalCrime = crime + TotalCrime

#Append to dictionary the value of total crime for Aug 2020
dict_total_by_Month["08-2020"] = TotalCrime
list_month.append(TotalCrime)
list_month_20.append(TotalCrime)

#print ("August 2020 - Total Crime " + str(TotalCrime))
#ValidateDataFrameDetails(dfcount2008)  #commented out as I validated the structure is correct - total column correct by row (LSOA area) and overall count

###### ANALYZE DATA - GROUPING TO GET UNIQUE COUNTS
# For the various datasets - see how many different crime types there were by LSOA - visually inspect result against counts from dfcount dataframe for each period - tota;s should match bt LSOA
#print(df1906_sorted.groupby('LSOA code')['Crime type'].value_counts()) # E01006264 is 1 on both lists
#print(dfcount1906.head(25)) # compare with dfcount1906.head() function looking at the total column for an overall count
#print(df1907_sorted.groupby('LSOA code')['Crime type'].value_counts()) # E01006412 is 3 on both lists
#print(dfcount1907.head(10)) # compare with dfcount1907.head() function looking at the total column for an overall count
#print(df1908_sorted.groupby('LSOA code')['Crime type'].value_counts()) #E01006363 is 1 on both lists
#print(dfcount1908.head(10)) # compare with dfcount1908.head() function looking at the total column for an overall count
#print(df2006_sorted.groupby('LSOA code')['Crime type'].value_counts()) #E01006225 is 1 on both lists
#print(dfcount2006.head(10)) # compare with dfcount2006.head() function looking at the total column for an overall count
#print(df2007_sorted.groupby('LSOA code')['Crime type'].value_counts()) #E01006412 is 15 on both lists
#print(dfcount2007.head(10)) # compare with dfcount2007.head() function looking at the total column for an overall count
#print(df2008_sorted.groupby('LSOA code')['Crime type'].value_counts()) #E01006412 is 13 on both lists
#print(dfcount2008.head(10)) # compare with dfcount1908.head() function looking at the total column for an overall count
#Since they match; this means the data has been created successfully

########################### Join the Datasets together to craete a single dataset ###################   Merge dataframes  ####################################
#I want to create a new dataframe called merged totals 2019 - i will use the concat method

#merging the tables using concat - ignoring the index as it is of no use to me
df2019_Merged = pd.concat([dfcount1906,dfcount1907,dfcount1908],ignore_index=True)
#ValidateDataFrameDetails(df2019_Merged)  # 2719 records - 18 columns - no null value - but each LSPA is in ther 3 times - for June, July & August 2019
#verify the record count by viewing the individuals dataframes - it is a count of districts reporting crime so no great variations expected
#print(dfcount1906.shape) # 911 records - 18 columns - no null value
#print(dfcount1907.shape) # 910 records - 18 columns - no null value
#print(dfcount1908.shape) # 908 records - 18 columns - no null value
# success - they match the merge was successful - 2719 vs 2719

df2020_Merged = pd.concat([dfcount2006,dfcount2007,dfcount2008],ignore_index=True)
#ValidateDataFrameDetails(df2020_Merged)  # 2729 records - 18 columns - no null value - but each LSPA is in ther 3 times - for June, July & August 2020
#verify the record count by viewing the individuals dataframes - it is a count of districts reporting crime so no great variations expected
#print(dfcount2006.shape) # 911 records - 18 columns - no null value
#print(dfcount2007.shape) # 910 records - 18 columns - no null value
#print(dfcount2008.shape) # 908 records - 18 columns - no null value
# success - they match the merge was successful - 2729 vs 2729

###### PYTHON - FUNCTIONS - NUMPY #######################################################################################
#Create code to carry out mathemitical operations over collections quickly using Numpy
np2019 = df2019_Merged.to_numpy()
np_2019_Total = np.sum(np2019[:,17])

# Creating a list of the crime types names
ms_crimes_2019 = list(df2019_Merged)[2:] # List crime types

#starting the counter with 2 as I do not want to get the sum of the first few columns
counter = 2

#Define the 2019 dictionary to hold the values fpr total, max, min, & Std;
#I had what to create a dummy record ti initialise the dectionary as I was unable to create it within the for loop
dict_2019_total = {"names":0}
dict_2019_max = {"names":0}
dict_2019_min = {"names":0}
dict_2019_std = {"names":0}

for names in ms_crimes_2019 :
    if names != 'LSOA name' :
        counter = counter + 1
        total = np.sum(np2019[:,counter])
        max = np.max(np2019[:,counter])
        min = np.min(np2019[:,counter])
        stdev = np.std(np2019[:,counter])
        #print("Crime Type: " + names + "; Total: " + str(total) + "; Max: " + str(max) + "; Min: " + str(min) + "; stdev: " + str(stdev))

        #Populate the 2019 dictionary with the summary values
        dict_2019_total[names] = total
        dict_2019_max[names] = max
        dict_2019_min[names] = min
        dict_2019_std[names] = stdev

#delete the dictionary initialising values as they are of no value now since the disctionary was populated with vales from the for loop
del dict_2019_total["names"]
del dict_2019_max["names"]
del dict_2019_min["names"]
del dict_2019_std["names"]

#unfortunately, this analysis did not provide useable data to variation between the max and min values was too great to be useable
print("Dictionary - Max, Min & standard Dev for 2019 Crime Types")
print(dict_2019_total)
print(dict_2019_max)
print(dict_2019_min)
print(dict_2019_std)

##################### Repeating for 2020

#Create  code to carry out mathemitical operations over collections quickly using Numpy
np2020 = df2020_Merged.to_numpy()
np_2020_Total = np.sum(np2020[:,17])

# Creating a list of the crime types names
ms_crimes_2020 = list(df2020_Merged)[2:] # List crime types

#starting the counter with 2 as I do not want to get the sum of the first few columns
counter = 2

#Define the 2020 dictionary to hold the values fpr
dict_2020_total = {"names":0}
dict_2020_max = {"names":0}
dict_2020_min = {"names":0}
dict_2020_std = {"names":0}

for names in ms_crimes_2020 :
    if names != 'LSOA name' :
        counter = counter + 1
        total = np.sum(np2020[:,counter])
        max = np.max(np2020[:,counter])
        min = np.min(np2020[:,counter])
        stdev = np.std(np2020[:,counter])
        #print("Crime Type: " + names + "; Total: " + str(total) + "; Max: " + str(max) + "; Min: " + str(min) + "; stdev: " + str(stdev))

        #Populate the 2020 dictionary with the summary values
        dict_2020_total[names] = total
        dict_2020_max[names] = max
        dict_2020_min[names] = min
        dict_2020_std[names] = stdev

#delete the dictionary initialising values as they are of no value now since the dictionary was populated with vales from the for loop
del dict_2020_total["names"]
del dict_2020_max["names"]
del dict_2020_min["names"]
del dict_2020_std["names"]

#unfortunately, this analysis did not provide useable data to variation between the max and min values was too great to be useable
print("Dictionary - Max, Min & standard Dev for 2020 Crime Types")
print(dict_2020_total)
print(dict_2020_max)
print(dict_2020_min)
print(dict_2020_std)

###########  VISUALIZE - SEABORN & MATPLOTLIB  ############################################################################################
#%matplotlib notebook
plt.style.use('seaborn-white')

######## Line graph - Summer 2019 vs Summer 2020 #########################
###### Figure 1: Recorded Crimes in Merseyside - Summer 2019 vs Summer 2020
#create a line graph to show the total of crimes in June, July & Aug 2019 vs the same period in 2020
list_month_names = ['06-June','07-July','08-Aug']
fig, ax = plt.subplots()
ax.plot(list_month_names,list_month_19, marker="o", linestyle='dotted', color="r",label='2019')
ax.plot(list_month_names,list_month_20, marker="v", linestyle="--", color="b",label='2020')
plt.legend()
ax.set_xlabel("Time (Months)")
ax.set_ylabel("Number of Recorded Crimes")
ax.set_title("Recorded Crimes in Merseyside - Summer 2019 vs Summer 2020")
plt.show()

######## Bar graph - Crime by Area 2019 & 2020 #########################
#create a bar graph showing the crimes by area for 2019 & 2020 in Matplotlib
###### Figure 2 -  Crimes by Type - Summer 2019
crime_no = ['Anti-social behaviour','Bicycle theft','Burglary','Criminal damage and arson','Drugs','Other crime','Other theft','Possession of weapons','Public Order','Robbery','Shoplifting', 'Theft from the person','Vehicle crime','Violence and sexual offences']
#crime_no = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
LSOA = df1908_sorted["Crime type"].unique()
fig, ax = plt.subplots()
for LSOA in ms_crimes_2019:
    if (LSOA not in ["Total", "LSOA name"]) :
        ax.bar(LSOA, df2020_Merged[LSOA].sum())
ax.set_ylabel("Total Crime Numbers")
ax.set_xticklabels(crime_no)
plt.xticks(rotation=45)
plt.title ("Crimes By Type - Summer 2019")
plt.xlabel("List of Offenses")
plt.ylabel("Number of Offenses")
plt.grid()
plt.tight_layout()
plt.show()


###### Figure 3 -  Crimes by Type - Summer 2020
fig, ax = plt.subplots()
for LSOA in ms_crimes_2020:
    if (LSOA not in ["Total", "LSOA name"]) :
        ax.bar(LSOA, df2020_Merged[LSOA].sum())
ax.set_ylabel("Total Crime Numbers")
ax.set_xticklabels(crime_no)
plt.xticks(rotation=45)
plt.title ("Crimes By Type - Summer 2020")
plt.xlabel("List of Offenses")
plt.ylabel("Number of Offenses")
plt.grid()
plt.tight_layout()
plt.show()

######## SEABORN Bar graph - Crime by Area 2019 & 2020 #########################
#create a bar graph showing the crimes by area for 2019 & 2020 in Seaborn
###### Figure 4 -  Crimes by Type - Summer 2020 ~ although created these mirrored the outputs from MatplotLI & I preferred that version
df2019_Merged_whole = pd.concat([df1906_sorted,df1907_sorted,df1908_sorted],ignore_index=True)
ms2019_Crime = df2019_Merged_whole['Crime type']
ms2019_Crime = ms2019_Crime.sort_values()
barchart = sns.countplot(x=ms2019_Crime)
barchart.set_xticklabels(barchart.get_xticklabels(),rotation=45)
plt.title('Crimes By Type - Summer 2019')
plt.xlabel("List of Offenses")
plt.ylabel("Number of Offenses")
plt.grid()
plt.tight_layout()
plt.show()

###### Figure 5 -  Crimes by Type - Summer 2020 ~ although created these mirrored the outputs from MatplotLI & I preferred that version
df2020_Merged_whole = pd.concat([df2006_sorted,df2007_sorted,df2008_sorted],ignore_index=True)
ms2020_Crime = df2020_Merged_whole['Crime type']
ms2020_Crime = ms2020_Crime.sort_values()
barchart = sns.countplot(x=ms2020_Crime)
barchart.set_xticklabels(barchart.get_xticklabels(),rotation=45)
plt.title('Crimes By Type - Summer 2020')
plt.xlabel("List of Offenses")
plt.ylabel("Number of Offenses")
plt.grid()
plt.tight_layout()
plt.show()

###### Heatmap showing the crimes per region - most on the left and together with a number of outliers to the right
#craete an unstacked table with LSOA the totals- fill in any NaN values with zeros since no crime occurred
###### Figure 6 -  Heatmap by LSOA Location - Summer 2019 - Seaborne
Crime_LSOA = df2019_Merged.groupby('LSOA code').Total.value_counts().unstack().fillna(0)
sns.heatmap(Crime_LSOA)
plt.title('Heatmap - Crime per Location - Summer 2019')
plt.grid()
plt.tight_layout()
plt.show()

###### Figure 7 -  Heatmap by LSOA Location - Summer 2019 - Seaborne
# Crime_LSOA = df2020_Merged.groupby('LSOA code').Total.value_counts().unstack().fillna(0)
sns.heatmap(Crime_LSOA)
plt.title('Heatmap - Crime per Location - Summer 2020')
plt.grid()
plt.tight_layout()
plt.show()

###### Joining the count of LSOA into the one table for comparison purposes for both 2019 & 2020
df2019_LSOA = pd.concat([dfcount1906,dfcount1907,dfcount1908],ignore_index=True)
df2020_LSOA = pd.concat([dfcount2006,dfcount2007,dfcount2008],ignore_index=True)
#ValidateDataFrameDetails(df2019_LSOA)  #commented out as I validated the structure is correct - dataframe created correctly
#ValidateDataFrameDetails(df2020_LSOA)  #commented out as I validated the structure is correct - dataframe created correctly

#dropping the following columns'Month', 'LSOA name', 'Anti-social behaviour','Bicycle theft', 'Burglary', 'Criminal damage and arson', 'Drugs','Other crime', 'Other theft', 'Possession of weapons', 'Public order','Robbery', 'Shoplifting', 'Theft from the person', 'Vehicle crime','Violence and sexual offences',
df2019_LSOA.drop(df2019_LSOA.columns[[0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16]],axis=1,inplace=True)
df2020_LSOA.drop(df2020_LSOA.columns[[0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16]],axis=1,inplace=True)
#ValidateDataFrameDetails(df2019_LSOA)  #commented out as I validated the structure is correct - dataframe created correctly
#ValidateDataFrameDetails(df2020_LSOA)  #commented out as I validated the structure is correct - dataframe created correctly

#commenting out of the use of `distplot` as it is a deprecated function and will be removed in a future version.
#sns.distplot(df2019_LSOA.Total)
#sns.distplot(df2019_LSOA.Total, rug=True, hist=True,kde=True)
#plt.show()

#sns.histplot(df2019_LSOA.Total,kde=True, bins=300,binwidth=20, stat='density')
#plt.show()

#Estimate probability mass, and it can add a smooth curve obtained using a kernel density estimate,
###### Figure 8 -  Histogram (Prpbability Mass) - Summer 2019 - Seaborne
sns.histplot(df2019_LSOA.Total,stat='probability', fill=False, element='step', cumulative=True)
plt.title('Histogram (Probability Mass) - Crime per Location - Summer 2019')
plt.xlabel("Count of Offenses")
plt.ylabel("Normalizes counts so that the sum of the bar heights is 1")
plt.grid()
plt.tight_layout()
plt.show()

###### Figure 9 -  Histogram (Prpbability Mass) - Summer 2020 - Seaborne
sns.histplot(df2020_LSOA.Total,stat='probability', fill=False, element='step', cumulative=True)
plt.title('Histogram (Probability Mass) - Crime per Location - Summer 2020')
plt.xlabel("Count Of Offenses")
plt.ylabel("Normalizes counts so that the sum of the bar heights is 1")
plt.grid()
plt.tight_layout()
plt.show()

###### Percentage of crimes in each catogery -2019 & 2020

###### Figure 11 -  Piechart - Percentage of Crimesin each category - Summer 2019
font1 = {'family': 'DejaVu Sans','color':  'darkblue','weight': 'bold','size': 35,}
lables = df2019_Merged_Origional['Crime type'].unique()
lables.sort()
sizes = df2019_Merged_Origional.groupby(['Crime type']).size()
plt.figure(figsize=(20,10))
ax = plt.axes()
ax.set_facecolor("lightblue")
plt.title('Percentage of Crimes in each Category - Summer 2019\n',fontdict=font1)
ab=plt.pie(sizes, labels=lables, startangle=90,autopct='%1.1f%%', textprops={'fontsize': 8,'color':'darkblue'})
plt.tight_layout()
plt.show()

###### 2020 - Pie Chart

###### Figure 11 -  Piechart - Percentage of Crimesin each category - Summer 2019
lables = df2020_Merged_Origional['Crime type'].unique()
lables.sort()
sizes = df2020_Merged_Origional.groupby(['Crime type']).size()
plt.figure(figsize=(20,10))
ax = plt.axes()
ax.set_facecolor("lightblue")
plt.title('Percentage of Crimes in each Catogery - Summer 2020\n',fontdict=font1)
ab=plt.pie(sizes, labels=lables, startangle=90,autopct='%1.1f%%', textprops={'fontsize': 8,'color':'darkblue'})
plt.tight_layout()
plt.show()

#========examine the top 25 LSOA by month in each year by total crime
dfTop25_2019 = df2019_LSOA.sort_values('Total',ascending=False)
dfTop25_2019 = dfTop25_2019.drop_duplicates(['LSOA name'],keep='first')
dfTop25_2019 = dfTop25_2019.head(25)

dfTop25_2020 = df2020_LSOA.sort_values('Total',ascending=False)
dfTop25_2020 = dfTop25_2020.drop_duplicates(['LSOA name'],keep='first')
dfTop25_2020 = dfTop25_2020.head(25)

#Join the tables to see the top LSOA for summer 2019 & 2020 - doing an inner join to only take the information where it is in both tables
#dftop_LSAO_Merged = pd.merge(left=dfTop25_2019, right=dfTop25_2020, left_on='LSOA name', left_index='_2019', right_on='LSOA name', right_index='_2020')
#dfTop25_2019.merge(dfTop25_2020[['LSOA name','Total']],on='LSOA name')
dfTopLSAO_Merged = dfTop25_2019.merge(dfTop25_2020,on='LSOA name',suffixes=["_2019","_2020"])
#ValidateDataFrameDetails(dfTopLSAO_Merged)

###### Figure 10 -  Boxplot (Prpbability Mass) - Seaborne
plt.figure(1,figsize=(14,4))
for i in range(1,3) :
    plt.subplot(1,2,i)
    plt.boxplot(dfTopLSAO_Merged[dfTopLSAO_Merged.columns[i]])
    plt.title("Boxplot " + dfTopLSAO_Merged.columns[i])
    plt.xlabel("LSAO Area")
    plt.ylabel("Count Of Offences")
    plt.grid()
plt.show()

#create a barchart showing the top LSOA for crime in 2019 vss 2020

###### Figure 13 -  BarChart Top LSOA for Crime in Merseyside
dfTopLSAO_Merged.plot.bar(x='LSOA name',rot=45,title="Top LSOA Areas by Crime Numbers - Merseyside")
plt.xlabel("LSOA Area")
plt.ylabel("Count Of Offenses")
plt.grid()
plt.tight_layout()
plt.show()

#####  END OF CODE  ###########################################################################################################################################