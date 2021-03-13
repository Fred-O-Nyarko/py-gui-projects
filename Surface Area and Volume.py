# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:34:10 2021

@author: gh
"""

import numpy as np
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Calculating the Surface Area and Volume of a Cyliner")
win.resizable(True,True)

ttk.Label(win, text = "radius:").grid(column = 0, row = 0)
ttk.Label(win, text = "height:").grid(column = 2, row = 0)

radiusName = tk.StringVar()
heightName = tk.StringVar()
radiusEntry = ttk.Entry(win, width = 4, textvariable = radiusName).grid(column = 1, row = 0)
heightEntry = ttk.Entry(win, width = 4, textvariable = heightName).grid(column = 3, row = 0)

ttk.Label(win, text = "area:").grid(column = 0, row = 2)
ttk.Label(win, text = "volume:").grid(column = 0, row = 3)

def clickMe():
    height = float(heightName.get())
    radius = float(radiusName.get())
    volume = np.pi*radius**2*height
    area = 2*np.pi*radius*height + 2*np.pi*radius**2
    ttk.Label(win, text = str(area)).grid(column = 1, row = 2)
    ttk.Label(win, text = str(volume)).grid(column = 1, row = 3)
    
SolveButton = tk.Button(win, text = "Solve", command = clickMe)
SolveButton.grid(column = 1, row = 1)
win.mainloop()
