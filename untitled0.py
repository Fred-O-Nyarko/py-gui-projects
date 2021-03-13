# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 00:43:45 2021

@author: gh
"""

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("")
win.geometry('800x600')
win.resizable(True,True)

def popup():
    popupwin = tk.Toplevel(win)
    popupwin.title("Truss Properties")
    popupwin.resizable(True,True)
    ttk.Label(popupwin, text="Joint No:").grid(row=0, column=0)
    ttk.Label(popupwin, text="X-coordinates:").grid(row=1, column=0)
    ttk.Label(popupwin, text="Y-coordinates:").grid(row=2, column=0)
    ttk.Label(popupwin, text="Support").grid(row=0, column=4)
    ttk.Label(popupwin, text="Cross-sectional Area").grid(row=0, column=6)
    ttk.Label(popupwin, text="").grid(row=0, column=6)
    
    JName = tk.StringVar()
    XcName = tk.StringVar()
    YcName = tk.StringVar()
    AreaName = tk.StringVar()
    
    JNameEntry = ttk.Entry(popupwin, width = 4, textvariable = JName).grid(column=2, row=0)
    XcNameEntry = ttk.Entry(popupwin, width = 4, textvariable = XcName).grid(column=2, row = 1)
    YcNameEntry = ttk.Entry(popupwin, width = 4, textvariable = YcName).grid(column=2, row = 2)
    AreaNameEntry = ttk.Entry(popupwin, width = 16, textvariable = AreaName).grid(column=6, row=2)

    B2 = ttk.Button(popupwin,text="Edit",).grid(row=5, column=4)
   # B1 = ttk.Button(popupwin, text="Next", command=popupwin.destroy).grid(row=5,column=0)
    B1 = ttk.Button(popupwin, text="Next", command= addToList).grid(row=5,column=0)
    value = addToList(JName)
    displayValues(value)
    popupwin.mainloop()

def displayValues(value):
    T = tk.Text(win, height=5, width=40)
    l = tk.Label(win, text = "Values") 
    l.pack() 
    T.pack() 
    T.insert(tk.END, value) 
    
def addToList(JName):
    joint = JName.get()
    print("joint",joint)
   # valuesList = []
   # valuesList.append(joint)
    return joint;
    
def main():
  OpenButton = ttk.Button(win, text="Open", command=popup)
  OpenButton.pack()
  win.mainloop()
  
    
if __name__ == "__main__":
    main()