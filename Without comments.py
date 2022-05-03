# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:27:11 2022

@author: nisan
"""


#used libraries

import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import IntSlider, interact
from matplotlib import colors
import tkinter
matplotlib.use('TkAgg')
#assigning the variables
df_transport = pd.read_csv (r'\Users\nisan\Documents\Semester 2\ProgrammingGEOG55\assignment2\transport.csv') 
df_population = pd.read_csv (r'\Users\nisan\Documents\Semester 2\ProgrammingGEOG55\assignment2\population.csv') 
df_geology = pd.read_csv (r'\Users\nisan\Documents\Semester 2\ProgrammingGEOG55\assignment2\geology.csv')



#adding in sliders
slider_transport = IntSlider(
    value=0,
    min=0,
    max=100,
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d',
    description='Transport:')

slider_population = IntSlider(
    value=0,
    min=0,
    max=100,
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d',
    description='Population:')

slider_geology = IntSlider(
    value=0,
    min=0,
    max=100,
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d',
    description='Geology:')



fig_main = plt.figure(figsize=(10,10)) #setting the defult size of the model window that it opens up as

cmap = colors.ListedColormap(['white', 'black']) #make it grey  
df_main = df_transport + df_population + df_geology # Merging layers 

plt.imshow(df_main, cmap=cmap)
plt.title("Main Map", fontsize=12)
plt.show()
#plt.imsave('df_main.png', cmap='inferno') #shows blank, missing arr argurment(define array,set x and y?)



def square1(number): 
    return None

interact(square1, number=slider_transport)
interact(square1, number=slider_population)
interact(square1, number=slider_geology)




def slider_transport(val):
    print (val)
    

root = tkinter.Tk() #building the main window, before the canvas.draw plots the environment and agents
menu = tkinter.Menu(root) #adding a menu bar to  window
root.config(menu=menu)
model_menu = tkinter.Menu(menu) 
menu.add_cascade(label="Run Model", command=slider_transport) #setting button and function into tkinter window to run model when clicked
root.wm_title("Environment and Agents") #title for the window
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg( master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

tkinter.mainloop()   #running the tkinter event loop
