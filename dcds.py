
# coding: utf-8

# In[53]:


import os
os.getcwd()
os.chdir('C:/Users/jingcong/Desktop/py')

import csv

'''
with open('DataDC-guests-2017.02.01-10.45.csv - DataDC-guests-2017.02.01-10.45.csv.csv', "r") as f:
    reader = csv.reader(f,delimiter=":")
    for row in reader:
        print(row)
'''

import numpy as np
import pandas as pd
replaceDict = {"Training" : "Get Training","New Job":"Get Hired","Volunteering":"Volunteering","Teaching":"Give Training","Hiring":"Hiring","Speaking": "Event Speaking","Sponsoring":"Sponsoring","None":"None"}

filename = 'DataDC-guests-2017.02.01-10.45.csv - DataDC-guests-2017.02.01-10.45.csv.csv'

dsdc = pd.read_csv(filename)

def replaceVal(x):
    helpValue = ''
    temp = x
    if not isinstance(x,str):
        temp = "None"
    line = temp.replace("\n","")
    line_split = line.split(",")
    for i in line_split:
        helpValue = replaceDict[i] + "," + helpValue
    return helpValue
    
dsdc["What may we help with?"] = dsdc["What may we help with?"].apply(replaceVal)
dsdc.to_csv("test.csv")


# In[4]:

dsdc.head()


# In[55]:




# In[50]:

dsdc.helpUpdated


# In[48]:



