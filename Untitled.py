
import os
os.getcwd()
os.chdir('C:/Users/jingcong/Desktop/py')

import sys
import numpy as np
import pandas as pd

filename = sys.argv[1]
type_of_doc = sys.argv[2]

dsdc = pd.read_csv(filename)
concat_df = []

if type_of_doc == "c":   
    replaceDict = {"Training" : "Get Training","New Job":"Get Hired","Volunteering":"Volunteering","Teaching":"Give Training","Hiring":"Hiring","Speaking": "Event Speaking","Sponsoring":"Sponsoring","None":"None"}
    def replaceVal(x):
        helpValue = ''
        temp = x
        if not isinstance(x,str):
            temp = "None"
        line = temp.replace("\n","")
        line_split = line.split(",")
        for i in line_split:
            if (i in replaceDict):
                helpValue = replaceDict[i] + "," + helpValue
        return helpValue
    dsdc["What may we help you with?"] = dsdc["What may we help you with?"].apply(replaceVal)

if type_of_doc == "d":
    dsdc['Name'] = dsdc['First Name'] + " " + dsdc['Last Name']

columnNames = ["Name","First Name","Last Name","Email","What may we help you with?","May we contact you?","Meetup ID"]
export_csv = pd.DataFrame()
for y in columnNames:
    if y in dsdc.columns:
        export_csv[y] = dsdc[y]
    else:
        export_csv[y] = ""
    concat_df.append(export_csv)

final_df = pd.concat(concat_df)
final_df.to_csv("exported_"+type_of_doc+".csv",index=False)
print("done!\n")
 
  

