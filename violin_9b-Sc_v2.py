# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:03:32 2021

@author: achang
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns
import pandas as pd
import matplotlib.patches as mpatches

###################################################################
### Read the data. ###

df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210110-2 MCF10A (DMSO vs CK869) (Scrib, Ecad), daughter width\CK-Scrib-AJ Ratio.xlsx',
                    sheet_name='AJ')

#####################################################################
fig, ax = plt.subplots(figsize=(3, 6))

sns.violinplot(x=["xxx"]*len(df), y='Value',  # please indicate the x = ["type what you want to indicate"]
              data=df, cut=1, bw=0.8, 
              scale='count', 
              hue='Type', split=True, showcaps=False,
              palette=['white','tomato'], linecolor= 'k',
              inner='quartile')

for l in ax.lines:
    l.set_linestyle('--')
    l.set_linewidth(4)
    l.set_color('black')
    l.set_alpha(1)
for l in ax.lines[1::3]:
    l.set_linestyle('-')
    l.set_linewidth(4)
    l.set_color('black')
    l.set_alpha(1)

plt.setp(ax.collections, edgecolor="k", linewidth=3)

######################################################################
ax.spines["bottom"].set_linewidth(5)
ax.spines["left"].set_linewidth(5)
ax.spines["top"].set_linewidth(0)
ax.spines["right"].set_linewidth(0)

ax.get_legend().remove()

ax.set_ylim(0,3.5) 

ax.set_ylabel(r"value",fontsize=0, fontname="Arial")
ax.set_xlabel(r"",fontsize=0, fontname="Arial")

ax.xaxis.set_tick_params(labelsize=0, length =0)
ax.yaxis.set_tick_params(labelsize=25, length =0)