#!/usr/bin/env python
# coding: utf-8

# # UFCFLR-15-M Course Assessment
# # 21066220 
# # Anjolaoluwa Aworinde

# In[2]:

# import pandas to read the csv file, seperating the file with the ','  as a delimiter or seperator
# define the dataframe beneath to call up the file
import pandas as pnd
bristol_data = pnd.read_csv('bristol-air-quality-data.csv', delimiter = ';')
bristol_data


# In[3]:


# Call-up the 'Date Time' colum within the dataframe to eliminate any errors with the date. This is to help with cleaning the data
bristol_data['Date Time'] = pnd.to_datetime(bristol_data['Date Time'], errors='coerce')
bristol_data


# In[4]:

# Data clean-up involving the removing any irrelevant date not necessary for the analysis 
bristol_data = bristol_data.loc[bristol_data['Date Time'] >= '2010-01-01 00:00:00+00:00'] 
bristol_data


# In[5]:

# merge the existing data list to identify errors with the data
bristol_data['monitor_station'] = bristol_data['SiteID'].astype(str) +" "+ bristol_data['Location']
bristol_data


# In[6]:


# create a list showing correct/matching SiteID and Location to identify the mismatch
# convert this list to a dataframe and give it column name 'rightlist'

rightlist = {'RightSiteID': [188, 203, 206, 209,213 ,215 , 228 ,270 , 271 , 375 ,395 ,452 ,447 , 459 , 463 , 481 , 500 , 501 ],
        'RightLocation': ['AURN Bristol Centre','Brislington Depot','Rupert Street','IKEA M32','Old Market','Parson Street School',
                     'Temple Meads Station', 'Wells Road','Trailer Portway P&R','Newfoundland Road Police Station',"Shiner's Garage", 
                     'AURN St Pauls','Bath Road','Cheltenham Road \ Station Road','Fishponds Road','CREATE Centre Roof', 'Temple Way', 
                     'Colston Avenue']}

rightlist_df = pnd.DataFrame(rightlist)
print(rightlist_df)


# In[7]:

# check the type of list created
rightlist_df['right_monitor_station'] = rightlist_df['RightSiteID'].astype(str) +" "+ rightlist_df['RightLocation']
rightlist_df


# In[8]:


# get unique values in monitor-station from bristol_data
unique_monitor_station = list(set(bristol_data['monitor_station']))
uniquelist_df = pnd.DataFrame(unique_monitor_station)
print(uniquelist_df)


# In[17]:


# enumenrate to index the stations within the table to find location of mismatch
wrongLocation = {'wronglines':[c for c,z in enumerate(bristol_data['monitor_station'].tolist()) if z not in rightlist_df['right_monitor_station'].tolist()],
                'offlist':[[z]for c,z in enumerate(bristol_data['monitor_station'].tolist()) if z not in rightlist_df['right_monitor_station'].tolist()]}
wrongLocation_df = pnd.DataFrame(wrongLocation)
wrongLocation_df


# In[45]:


# number of rows to know the number of mismatch within the dataset
len(wrongLocation_df.index)


# In[20]:


# Delete wrongLocation from the original data created
bristol_data.drop(bristol_data.index[wrongLocation_df['wronglines']], inplace = True)
bristol_data


# In[21]:

# delete the added colum above
display("DataFrame after deletion")
del bristol_data['monitor_station']
bristol_data


# In[22]:

# convert cleaned data to csv
bristol_data.to_csv("clean.csv")

