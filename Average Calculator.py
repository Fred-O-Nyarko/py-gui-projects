# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import tkinter as tk
from tkinter import ttk

win = tk.Tk()                                              #Create a window
win.title('Average Calculator')                            #Create a tile for the window
win.resizable(False,False)                                 #

ttk.Label(win, text="Credit Hours").grid(row=0,column=0,padx=5,pady=5)  #Create a label called Credit Hours
credit = tk.StringVar()                                                 #Assigning a text variable called credit
ttk.Entry(win, width=4, textvariable=credit).grid(row=0,column=1,padx=5,pady=5)
 
ttk.Label(win, text="Average").grid(row=0,column=2,padx=5,pady=5)
average = tk.StringVar()
ttk.Entry(win, width=4, textvariable=average).grid(row=0,column=4,padx=5,pady=5)

ttk.Label(win, text="Course").grid(row=1,column=0,padx=5,pady=5)     #Create a label called Course
ttk.Label(win, text="Mark").grid(row=1,column=1,padx=5,pady=5)       #Create a label called Mark

course = tk.StringVar()
courseSelected = ttk.Combobox(win, width=23, textvariable=course, state="readonly")
courseSelected["value"] = ("Computer Aided Design",\
                           "Computer Programming",\
                           "Theory of Structures",\
                           "Principles of Design",\
                           "Differential Equations",\
                           "Engineering Geology",\
                           "Literature",\
                           "Engineering in Society",\
                           "Strength of Materials")
courseSelected.grid(row=2,column=0,)

mark = tk.StringVar()
ttk.Entry(win, width=4, textvariable=mark).grid(row=2,column=1)

database = {}

def clickAdd():
    currentCourse = course.get()
    currentMark = float( mark.get() )
    
    if currentCourse == "Computer Aided Design":
        creditHours = 2
    elif currentCourse == "Computer Programming":
        creditHours = 2
    elif currentCourse == "Theory of Structures":
        creditHours = 3
    elif currentCourse == "Principles of Design":
        creditHours = 2
    elif currentCourse == "Differential Equations":
        creditHours = 4
    elif currentCourse == "Engineering Geology":
        creditHours = 2
    elif currentCourse == "Literature":
        creditHours = 1
    elif currentCourse == "Engineering in Society":
        creditHours = 2
    elif currentCourse == "Strength of Materials":
        creditHours = 2
    
    if 70<=currentMark<=100:
        grade = "A"
    elif 60<=currentMark<70:
        grade = "B"
    elif 50<=currentMark<60:
        grade = "C"
    elif 40<=currentMark<50:
        grade = "D"
    else:
        grade = "F"
    
    database[currentCourse] = (creditHours, grade, currentMark)
    lengthDatabase = len( database.keys() )
    
    ttk.Label(resultsFrame, text=currentCourse).grid(row=lengthDatabase, column=0, sticky="w")
    ttk.Label(resultsFrame, text=str(creditHours)).grid(row=lengthDatabase, column=1)
    ttk.Label(resultsFrame, text=str(currentMark)).grid(row=lengthDatabase, column=2)
    ttk.Label(resultsFrame, text=str(grade)).grid(row=lengthDatabase, column=3)
    
AddButton = ttk.Button(win, text="Add", command=clickAdd).grid(row=2,column=2,padx=5,pady=5)

def clickCalcuate():
    previousCredit = float( credit.get() )
    previousAverage = float( average.get() )
    
    registeredCourses = database.keys()
    
    sumMark = 0
    for i in registeredCourses:
        courseItems = database[i]
        sumMark = courseItems[0]*courseItems[2] + sumMark 
        creditHourSum = courseItems[0] + creditHourSum
        
        semesterAverage = sumMark/creditHourSum

CalculateButton = ttk.Button(win, text="Calculate", command=clickCalculate().grid(row=2,column=2,padx=5,pady=5)

resultsFrame = ttk.LabelFrame(win, text="Course Details")
resultsFrame.grid(row=3,column=0,padx=5,pady=5)
ttk.Label(resultsFrame, text="Course").grid(row=0,column=0,padx=5,pady=5)
ttk.Label(resultsFrame, text="Credit").grid(row=0,column=1,padx=5,pady=5)
ttk.Label(resultsFrame, text="Mark").grid(row=0,column=2,padx=5,pady=5)
ttk.Label(resultsFrame, text="Grade").grid(row=0,column=3,padx=5,pady=5)


win.mainloop()