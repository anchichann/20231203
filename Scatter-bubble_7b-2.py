# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:53:02 2021

@author: achang
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210110-2 MCF10A (DMSO vs CK869) (Scrib, Ecad), daughter width\CK-Ecad-M2.xlsx')


fig, axes = plt.subplots(figsize=(10,10))

sns.scatterplot(data=df,
                x="M2ratio-div2", 
                y="Ecadratio",
                size="width",
                hue="Cell",
                sizes=(500,10000),
                alpha=0.6, edgecolor="k",linewidth=4,
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

axes.spines["bottom"].set_linewidth(8)
axes.spines["top"].set_linewidth(8)
axes.spines["right"].set_linewidth(8)
axes.spines["left"].set_linewidth(8)
axes.set_facecolor('whitesmoke')

axes.set_xlabel('0.5x Ratio of NMIIb mean intensity,' + '\n' +'cortical vs cytoplasmic', fontname="Arial", fontsize = 0)
axes.tick_params(axis='x',labelsize=50, length=15, width=5)
axes.set_xlim(0,4.2)

axes.set_ylabel("Ratio of E-cad mean intensity," + "\n" + "daughters' contact vs cortical", fontname="Arial", fontsize = 0)
axes.tick_params(axis='y',labelsize=50, length=15, width=5)
axes.set_ylim(0,3.8)

"""
## Legend for data CK-869
circle1 = plt.Circle((0.25, 3.55), 0.1, color='k', fill=True)
axes.add_patch(circle1)
circle2 = plt.Circle((0.25, 3.3), 0.1, color='red', fill=True)
axes.add_patch(circle2)
axes.text(0.4, 3.5, 'DMSO,(n=18)', color='K', fontsize=32, fontname="Arial")
axes.text(0.4, 3.2, 'CK-869,(n=31)', color='K', fontsize=32, fontname="Arial")

circle3 = plt.Circle((0.25, 3.8), 0.1, color='k', fill=False, lw=5)
axes.add_patch(circle3)
axes.text(0.4, 3.75, "Size=Width of daughters' contact", color='K', fontsize=32, fontname="Arial")

#axes.arrow(1.6, 0.25, 0.4, 0, head_width=0.2, head_length=0.2, width = 0.05, fc='k', ec='k')
"""


