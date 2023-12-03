# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:30:04 2021

@author: achang

Scatter plot

Decision Boundary step by step
https://hackernoon.com/how-to-plot-a-decision-boundary-for-machine-learning-algorithms-in-python-3o1n3w07

"""

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import gridspec
import seaborn as sns
import pandas as pd
import matplotlib.patches as mpatches

### Load data ###
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\20210218 MCF10A\test2.xlsx')
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210108 MCF10A siScrib, cortical, AJ intensity (Ecad)\siScrib-Ecad-NJ.xlsx')
df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20181017 MCF10A (shScrib vs pRS) - Intensity Scrib, Ecad\shScrib-Ecad-NJ.xlsx')

CX=df["Ctr-Scrib"] # Control 
CY=df["Ctr-Ecad"] # Conrol 
SX=df["kd-Scrib"] # Scr-KD 
SY=df["kd-Ecad"] # Scr-KD 

### Figure design ###
#sns.scatterplot(ax=axes[0, 1], data=data1)
fig, axes = plt.subplots(figsize=(10,10))
                         
axes.scatter(CX, CY, s=150, c='k', marker="o") #label='first')
axes.scatter(SX, SY, s=150, c='r', marker="o") #label='second')

#black_patch = mpatches.Patch(color='k', label='si-Ctrl', hatch ='o', lw=1, ls='-')
#red_patch = mpatches.Patch(color='red', label='si-Scrib', hatch ='o', lw=1, ls='-')
black_patch = mpatches.Patch(color='k', label='sh-Ctrl', hatch ='o', lw=1, ls='-')
red_patch = mpatches.Patch(color='red', label='sh-Scrib', hatch ='o', lw=1, ls='-')
plt.setp(axes.legend(handles=[black_patch, red_patch], loc='upper left',fontsize=30).texts,family="Arial")

axes.spines["bottom"].set_linewidth(5)
axes.spines["top"].set_linewidth(5)
axes.spines["right"].set_linewidth(5)
axes.spines["left"].set_linewidth(5)
axes.set_facecolor('lightgray')

axes.set_xlabel('Avg. intensity of Scribble', fontname="Arial", fontsize = 40)
axes.tick_params(axis='x',labelsize=20, length=10, width=3)
axes.set_xlim(0,2000)

axes.set_ylabel('Avg. intensity of E-cadherin', fontname="Arial", fontsize = 40)
axes.tick_params(axis='y',labelsize=20, length=10, width=3)
axes.set_ylim(0,3000)


plt.show()
