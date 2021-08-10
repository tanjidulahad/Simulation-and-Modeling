# -*- coding: utf-8 -*-
"""find the value of pi using monte carlo simulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a5CGQXxn-FDmlBXfIc_dbkSSXhp2s_1I

**Finding the experimental value of pi**
"""

# initializing values for drawing lower right circle
import random
import numpy as np
import matplotlib.pyplot as plt
import math
x_point=[]
y_point=[]
for x in np.linspace(0,7.5,1000):
  x_point.append(x)
  y=-math.sqrt(56.25-(x)**2)
  y_point.append(y)
# variables for error graph drawing
error_list=[]
no_of_trial=[]
# point generation
for trial_no in range(100,1000,10):
 # variable initialization
  hits=0
  x_min=0
  x_max=7.5
  y_min=0
  y_max=-7.5
  pi=3.1416
  c=pi*56.25/4
  s=7.5**2
  hitx=[]
  hity=[]
  nohitx=[]
  nohity=[]
  # trial_no=100
  for i in range(trial_no):
    xrand=random.uniform(x_min,x_max)
    yrand=random.uniform(y_min,y_max)
    dist=math.sqrt((xrand-0)**2+(yrand-0)**2)
    if dist<=7.5:
      hits=hits+1
      hitx.append(xrand)
      hity.append(yrand)
    else:
      nohitx.append(xrand)
      nohity.append(yrand)
  # experimental pi value calculation
  expi=(hits*s*4)/(trial_no*56.25)
  error=(3.1416-expi)
  error_list.append(abs(error))
  no_of_trial.append(trial_no)
print("Experimental value of pi is: ",expi)
# graph plotting
plt.plot(hitx,hity,'go')
plt.plot(nohitx,nohity,'ro')
plt.plot(x_point,y_point)

"""**Error Graph**"""

# Error graph plotting
plt.plot(no_of_trial,error_list)
plt.xlabel("trial no")
plt.ylabel("error")