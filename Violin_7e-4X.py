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

Control = df["pRS-NJ"]
KDcell = df["SKD-NJ"]
Control2 = df["pRS-IJ"]
KDcell2 = df["SKD-IJ"]

# Anchi: you need to put the number of cell, for example [0:?]
Cdata = [Control[0:24], KDcell[0:21], Control2[0:23], KDcell2[0:21]]


### Plot ### 
fig, axes = plt.subplots(figsize=(25,12))

#axes.violinplot(Cdata, showmeans=False, showmedians=False, showextrema=False, widths = 1)
#plt.setp(axes.collections, edgecolor="k", facecolor="lightgray", linewidth=12, alpha=1)

sns.violinplot(data = Cdata, 
                    linewidth = 12, width=1.4, color = "lightgray",
                    saturation=0.3, bw=0.5, cut=0.2, inner = None)
plt.setp(axes.collections, edgecolor="k")

flierprops = dict(marker='o', markerfacecolor='k', markersize=30,
                  linestyle='None', markeredgecolor='white')

axes.boxplot(Cdata,flierprops = flierprops, whis=None, positions=np.array([0,1,2,3]), showcaps=False,widths=0.15, patch_artist=True,
            boxprops=dict(color="k", facecolor="k"),
            whiskerprops=dict(color="k", linewidth=12),
            medianprops=dict(color="yellow", linewidth=28))


### Format the figure ###

axes.spines["bottom"].set_linewidth(17)
axes.spines["left"].set_linewidth(17)
axes.set_ylim(0,4700)
axes.set_xlim(-1,4)

#xlab1 = [ "sh-Ctrl", "sh-Scrib"]
xlab1 = [ "sh-Ctrl", "sh-Scrib","sh-Ctrl", "sh-Scrib",]
xlab2 = ["(n=23)", "(n=21)", "(n=23)", "(n=21)"] 
xlabels = [f"{x1}\n{x2}" for x1, x2, in zip(xlab1,xlab2)]
axes.set_xticklabels(xlabels, fontname="Arial")

axes.set_ylabel(r"E-cad mean intensity",fontsize=80, fontname="Arial")

### plot a bar for statistics ###
plt.hlines(y=3880, xmin=0, xmax=1, linewidth=10, color='k')
plt.text(0.1, 4010, "p<0.001", fontsize = 60, style = 'italic', fontname="Arial") #p=3.0895*e-09
plt.hlines(y=4600, xmin=-0.8, xmax=1.5, linewidth=17, color='k')
plt.text(-0.8, 4800, "Nascent junction", fontsize = 80, style = 'italic', fontname="Arial")


plt.hlines(y=3600, xmin=2, xmax=3, linewidth=10, color='k')
plt.text(2.2, 3740, "p<0.05", fontsize = 60, style = 'italic', fontname="Arial") #p=0.0283
plt.hlines(y=4600, xmin=1.6, xmax=3.9, linewidth=17, color='k')
plt.text(1.6, 4800, "Interphase junction", fontsize = 80, style = 'italic', fontname="Arial")

### Ready to plot ###
plt.xticks(fontsize= 80, rotation=45)
plt.yticks(fontsize= 80, fontname="Arial")


sns.despine()

plt.show()
