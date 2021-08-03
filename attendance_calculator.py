# -*- coding: utf-8 -*-
"""Attendance calculator.ipynb

#Step 1: Type Date
#Step 2: Press the play button
#Step 3: Upload two sheets (Attendance ,Students input)

Note: Everytime you reuse this application don't forget to clean the content folder.
"""

from google.colab import files
uploded= files.upload()
 
import pandas as pd
 
Attendance= pd.read_excel('Attendance.xlsx').fillna(0)
students_input= pd.read_excel('Students input.xlsx').fillna(0)
 
date= '2020-09-11' #@param {type:"date"}
Attendance[date]=0
 
 
i=1
while i <= len(students_input):
    j=1
    while j <= len(Attendance):
        if students_input.iloc[i-1,students_input.columns.get_loc("Students ID")] == Attendance.iloc[j-1, Attendance.columns.get_loc("Student ID")] :
                Attendance.iloc[j-1, Attendance.columns.get_loc(date)]="Present"
        elif Attendance.iloc[j-1, Attendance.columns.get_loc(date)] != "Present" :
                Attendance.iloc[j-1, Attendance.columns.get_loc(date)]="Absent"
        j += 1
        
    i += 1
 

with pd.ExcelWriter('Attendance.xlsx') as writer:  
    Attendance.to_excel(writer, sheet_name='Attendance',index=False)
 
files.download('Attendance.xlsx')

Attendance.replace(["Present","Absent"], [1,0])
Attendance["Total Present"]=Attendance.replace(["Present","Absent"], [1,0]).iloc[:, Attendance.columns.get_loc("Student ID")+1:Attendance.columns.get_loc(date)+1].sum(axis=1)
Attendance["Percent Present"]=Attendance["Total Present"]*100/(len(Attendance.columns)-3)


reportname = 'Attendance Report '+date +'.xlsx'

with pd.ExcelWriter(reportname) as writer:  
    Attendance.to_excel(writer, sheet_name='Attendance Report',index=False)

files.download(reportname)

"""#Get report of a particular student
#Type the Student Id & Press the play button
"""

student_id =  43217 #@param {type:"number"}

ID_Present= Attendance["Total Present"].iloc[Attendance[Attendance["Student ID"]==student_id].index.values]
ID_Absent= (len(Attendance.columns)-4-ID_Present)

import matplotlib.pyplot as plt

# Data to plot
labels = 'Present', 'Absent'
sizes = [int(ID_Present), int(ID_Absent)]
colors = ['yellowgreen', 'red']
explode = ( 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)


plt.axis('equal')
plt.show()

Attendance.iloc[Attendance[Attendance["Student ID"]==student_id].index.values,:]

"""#Get the Sum of total students present
#Type Teacher Name & press the play button
"""

Teacher_Name = "Ashfaq" #@param {type:"string"}
sum=Attendance['Total Present'].sum(axis = 0, skipna = True) 
print("Teacher Name: "+ Teacher_Name +"\nSum of total students present "+str(sum))

"""#See Report :
#Press the play button
"""

Attendance
