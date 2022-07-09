#!/usr/bin/env python
# coding: utf-8

# # UFCFLR-15-M Course Assessment
# # 21066220 
# # Anjolaoluwa Aworinde

# In[62]:

# import pandas to read the csv file, seperating the file with the ','  as a delimiter or seperator
# define the dataframe beneath to call up the file
import pandas as pnd
bristol_data = pnd.read_csv('bristol-air-quality-data.csv', delimiter = ';')
bristol_data


# 

# In[61]:

# Setting up date. Make use of pandas datetime function to convert to date time
# Call-up the 'Date Time' colum within the dataframe to eliminate any errors with the date. This is to help with cleaning the data
bristol_data['Date Time'] = pnd.to_datetime(bristol_data['Date Time'], errors='coerce')
bristol_data


# In[58]:

# Data clean-up involving the removing any irrelevant date that is not necessary for the analysis 
bristol_data = bristol_data.loc[bristol_data['Date Time'] >= '2010-01-01 00:00:00+00:00'] 
bristol_data


# In[55]:

# convert cleaned data to csv
bristol_data.to_csv("crop.csv")

