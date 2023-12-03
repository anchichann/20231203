# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:53:02 2021

@author: achang
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20181017 MCF10A (shScrib vs pRS) - Intensity Scrib, Ecad\SKD-Ec-Sc-Width.xlsx')
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210108 MCF10A siScrib, cortical, AJ intensity (Ecad)\Si-Ec-Sc-width.xlsx')

fig, axes = plt.subplots(figsize=(11,11))

sns.scatterplot(data=df,
                x="Scrib", 
                y="Ecad",
                size="width",
                hue="Cell",
                sizes=(500,10000),
                alpha=0.5, edgecolor="k",linewidth=4,
                legend=False,
                palette=['gray','violet'],
                )

# Put the legend out of the figure
#plt.legend(bbox_to_anchor=(1.1, 1),borderaxespad=0)

# Here we create a legend:
# we'll plot empty lists with the desired size and label
#for area in [25, 500, 1000]:
#    plt.scatter([], [], c='k', alpha=1, s=area,
#                       label=str(area) + ' km$^2$')
#plt.legend(scatterpoints=1, frameon=False,
#                  labelspacing=10, title='width')

# Put the legend out of the figure
#plt.legend(bbox_to_anchor=(1.2, 0.9),borderaxespad=0)

####################################################################################################################
axes.spines["bottom"].set_linewidth(10)
axes.spines["top"].set_linewidth(10)
axes.spines["right"].set_linewidth(10)
axes.spines["left"].set_linewidth(10)
axes.set_facecolor('whitesmoke')


axes.set_xlabel('Scribble mean intensity' + '\n' +"at daughters' contact", fontname="Arial", fontsize = 0)
axes.tick_params(axis='x',labelsize=50, length=15, width=5)

axes.set_xlim(0,3200) # shRNA
#axes.set_xlim(0,2200) # siRNA

#axes.set_ylabel("E-cadherin avg. intensity" + "\n" + "at daughters' contact", fontname="Arial", fontsize = 0) # for sh-Scrib
#axes.tick_params(axis='y',labelsize=50, length=15, width=5) # for sh-Scrib


axes.set_ylabel("E-cad mean intensity" + "\n" + "at daughters' contact", fontname="Arial", fontsize = 0) # for si-Scrib
#axes.tick_params(axis='y',labelsize=30, length=15, width=5, which='both', labelleft=True, labelright=False) # for si-Scrib
axes.tick_params(axis='y',labelsize=50, length=15, width=5) # for si-Scrib (v2)

#axes.yaxis.tick_left() # shRNA
#axes.yaxis.set_label_position("left") #shRNA


#axes.yaxis.tick_right() # siRNA
axes.yaxis.tick_left() # siRNA_v2
axes.yaxis.set_label_position("left") # siRNA


axes.set_ylim(0,2500) # shRNA
#axes.set_ylim(0,3300) # siRNA

"""
## Legend for data siScrib
circle1 = plt.Circle((150, 2950), 70, color='k', fill=True)
axes.add_patch(circle1)
circle2 = plt.Circle((150, 2750), 70, color='red', fill=True)
axes.add_patch(circle2)
axes.text(250, 2900, 'si-Ctrl,(n=25)', color='K', fontsize=32, fontname="Arial")
axes.text(250, 2700, 'si-Scrib,(n=30)', color='K', fontsize=32, fontname="Arial")

circle3 = plt.Circle((150, 3150), 70, color='k', fill=False, lw=5)
axes.add_patch(circle3)
axes.text(250, 3100, "Size=Width of daughters' contact", color='K', fontsize=32, fontname="Arial")
"""

"""
## Legend for data shScrib
circle1 = plt.Circle((150, 2250), 70, color='k', fill=True)
axes.add_patch(circle1)
circle2 = plt.Circle((150, 2100), 70, color='red', fill=True)
axes.add_patch(circle2)
axes.text(250, 2200, 'sh-Ctrl,(n=24)', color='K', fontsize=32, fontname="Arial")
axes.text(250, 2050, 'sh-Scrib,(n=25)', color='K', fontsize=32, fontname="Arial")

circle3 = plt.Circle((150, 2400), 70, color='k', fill=False, lw=5)
axes.add_patch(circle3)
axes.text(250, 2350, "Size=Width of daughters' contact", color='K', fontsize=32, fontname="Arial")

"""

#axes.arrow(1.6, 0.25, 0.4, 0, head_width=0.2, head_length=0.2, width = 0.05, fc='k', ec='k')

