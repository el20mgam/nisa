# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:28:33 2022

@author: nisan
"""

#used libraries
#import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import IntSlider, interact
import numpy as np
from matplotlib import colors

#assigning the variables
df_transport = pd.read_csv (r'\Users\nisan\Documents\Semester 2\ProgrammingGEOG55\assignment2\transport.csv') 
df_population = pd.read_csv (r'\Users\nisan\Documents\Semester 2\ProgrammingGEOG55\assignment2\population.csv') 
df_geology = pd.read_csv (r'\Users\nisan\Documents\Semester 2\ProgrammingGEOG55\assignment2\geology.csv')


#display map result
#plt.title("Geology", fontsize=12)
#plotting the graph in matplotlib.pyplot as 'plt'
#plt.xlim(0,335) #defining the grid, x, y and title
#plt.ylim(525,0)
#plt.xlabel("X axis")
#plt.xticks(np.arange(0, 0))
#plt.ylabel("Y axis")
#plt.yticks(np.arange(0, 0))
#plt.get_cmap('magma') # SETS THE COLOUR FRAME 

#Display map results
#plt.imshow(df_transport)
#plt.show() 
#plt.imshow(df_population)
#plt.show()
#plt.imshow(df_geology)
#plt.show()

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

"""
Trying to assign function to get value of the slider

def slider_transport(val):
    print (val)
"""

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


"""
Trying to set up resest button 

slider_reset = IntSlider(
    value=0)
button = Button(slider_reset, 'Reset', hovercolor='0.975')

def reset(event):
    slider_population.reset()
    slider_geology.reset()
    slider_transport.reset()
button.on_clicked(reset)

----------------------------------------------------------------------


how to save in the file 
The imsave() displayes an image it saves it to a file. In the file each element of the numpy 
array describes one pixel. 
Example code:
n = 500
# create an nxn numpy array
a = np.random.random((n,n))
# save the image to a file 'test.png' using  the 'jet' color map to specify colors
plt.imsave('test.png', a, cmap = 'inferno')
- To save as image 
plt.savefig('redwhite.pdf')
"""

fig_main = plt.figure(figsize=(10,10)) #setting the defult size of the model window that it opens up as

cmap = colors.ListedColormap(['white', 'black']) #make it grey later on  
df_main = df_transport + df_population + df_geology # Merging layers 

plt.imshow(df_main, cmap=cmap)
plt.title("Main Map", fontsize=12)
plt.show()
#plt.imsave('df_main.png', cmap='inferno') #shows blank, missing arr argurment(define array,set x and y???)

"""
-----------------------------------------------------       
Trying to get functions to update map according to slider 
slider_population=
slider_geology=
slider_transport=
?????
t=
def f (t, population, geology, transport)
        
def slider_update (val):
       l.set_ydata(f(slider_population.val, slider_geology.val, slider_transport.val))
        fig.canvas.draw_idle()
    l.set_xdata..

"""

def square1(number): 
    return None

interact(square1, number=slider_transport)
interact(square1, number=slider_population)
interact(square1, number=slider_geology)

"""

I need to get the pixels of each scrollbar, add them together and then divide them by the total of the scrollbars (300) to re-range the dataset back to 0-255
(geology x scrollbargeology) + (population x scrollbarpopulation) + (transport x scrollbartransport) /300-scrollbar
---------------------------------------------------------------------
Trying to update map from scrollbar
def update(df_main):
    fig.clear() 
    
def run():
    
    canvas.draw() 


---------------------------------------------------------------
Setting values to 1, Dont really know what im doing
df_main[]
for value in dataframe:
    for value between [:.] in raw:
        if value != 0:
            set value = 1
            update dataframe
        else:
            update dataframe   
    
----------------------------------------------------------------- 
for value in dataframe:
    for value between [:.] in raw:
        if value != 0:
            set value = /100 #gettign fraction of number
                            #   assign how much of each value will
-----------------------------------------------------------------
For extra marks:
Show top 10 , getting largest areas
df['fig_main'].nlargest(n=10)
df_main.nlargest(n=10)????
"""