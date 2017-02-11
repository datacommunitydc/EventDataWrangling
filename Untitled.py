
# coding: utf-8

# In[ ]:

#import data 

import os
os.getcwd()
os.chdir(Directory)

import csv
import numpy as np
import pandas as pd

#combine two columns into another one for the DCW file
df = pd.read_csv('file name')
df['Full Name'] = df.xs('First Name', axis=1) + " " + df.xs('Last Name', axis=1)
df.to_csv('file name')

# Convert the Survey columns into the way we wanted
with open(filename, "r") as f:
    reader = csv.reader(f,delimiter=":")
    for row in reader:
        print(row)

replaceDict = {"Training" : "Get Training","New Job":"Get Hired","Volunteering":"Volunteering","Teaching":"Give Training","Hiring":"Hiring","Speaking": "Event Speaking","Sponsoring":"Sponsoring","None":"None"}

filename = 'file name'

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
dsdc.to_csv("New File Name")


dsdc.head()


# combine all 3 files into one by only select the columns with the specific names

filename = ['file 1','file 2','file 3']


concat_df = []

for i in filename:
    dsdc = pd.read_csv(i)
    columnNames = ["User Name","User ID","Full Name","First Name","Last Name","Email","What may we help with?","May we contact you?" ]
    export_csv = pd.DataFrame()
    for y in columnNames:
        if y in dsdc.columns:
            export_csv[y] = dsdc[y]
    concat_df.append(export_csv)

final_df = pd.concat(concat_df)
final_df.to_csv("final File name")
    



