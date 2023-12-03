# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:38:01 2021
@author: achang
"""
"""
violin polot tutor
https://www.pythoncharts.com/2019/04/24/violin-plots-seaborn/
https://stackoverflow.com/questions/45621545/how-to-use-whisker-parameter-of-boxplot-on-violin-plot-for-seaborn

"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

### Read the data. ###
## data : pRS vs SKD
df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20181017 MCF10A (shScrib vs pRS) - Intensity Scrib, Ecad\SKD-Ecad-viaNMIIb.xlsx')

#df = df.lstrip('\u202a')

#Control = df["pRS-NJ"]
#KDcell = df["SKD-NJ"]
Control = df["pRS-IJ"]
KDcell = df["SKD-IJ"]

# Anchi: you need to put the number of cell, for example [0:?]
Cdata = [Control[0:10], KDcell[0:10]]


### Plot ### 
fig, axes = plt.subplots(figsize=(18,22))

#axes.violinplot(Cdata, showmeans=False, showmedians=False, showextrema=False, widths = 1)
#plt.setp(axes.collections, edgecolor="k", facecolor="lightgray", linewidth=12, alpha=1)

sns.violinplot(data = Cdata, 
                    linewidth = 12, width=1.4, color = "lightgray",
                    saturation=0.3, bw=0.5, cut=0.2, inner = None)
plt.setp(axes.collections, edgecolor="k")

flierprops = dict(marker='o', markerfacecolor='k', markersize=30,
                  linestyle='None', markeredgecolor='white')

axes.boxplot(Cdata,flierprops = flierprops, whis=None, positions=np.array([0,1]), showcaps=False,widths=0.15, patch_artist=True,
            boxprops=dict(color="k", facecolor="k"),
            whiskerprops=dict(color="k", linewidth=12),
            medianprops=dict(color="yellow", linewidth=28))


### Format the figure ###

axes.spines["bottom"].set_linewidth(25)
axes.spines["left"].set_linewidth(25)
axes.set_ylim(0,3800)
axes.set_xlim(-0.7,1.9)

#xlab1 = [ "sh-Ctrl", "sh-Scrib"]
xlab1 = [ "sh-Ctrl", "sh-Scrib"]
xlab2 = ["(n=10)", "(n=10)"] 
xlabels = [f"{x1}\n{x2}" for x1, x2, in zip(xlab1,xlab2)]
axes.set_xticklabels(xlabels, fontname="Arial")

axes.set_ylabel(r"Ecad avg. intensity",fontsize=120, fontname="Arial")

### plot a bar for statistics ###
plt.hlines(y=3800, xmin=0, xmax=1, linewidth=40, color='k')
plt.text(0, 3850, "p=0.3792", fontsize = 100, style = 'italic', fontname="Arial")


### Ready to plot ###
plt.xticks(fontsize= 120, rotation=45)
plt.yticks(fontsize= 100, fontname="Arial")


sns.despine()

plt.show()
