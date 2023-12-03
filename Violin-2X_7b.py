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
from matplotlib.ticker import MaxNLocator

### Read the data. ###
## data : pRS vs SKD
df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210110-2 MCF10A (DMSO vs CK869) (Scrib, Ecad), daughter width/CK-Ecad.xlsx')

#df = df.lstrip('\u202a')

Control = df["DM-Ec"]
KDcell = df["CK-Ec"]

Control2 = df["DM-M2"]
KDcell2 = df["CK-M2"]

# Anchi: you need to put the number of cell, for example [0:?], ?=total number of sample
Cdata = [Control[0:18], KDcell[0:31]]
Cdata2 = [Control2[0:18], KDcell2[0:31]]


### Plot ####################################################################################################
fig, axes = plt.subplots(2, figsize=(10,20), gridspec_kw={
                           #'width_ratios': [1, 2],
                           'height_ratios': [1, 1]})
fig.tight_layout(pad=0) #for adjusting the spacing between subplot 

##############################################################################################################
#axes.violinplot(Cdata, showmeans=False, showmedians=False, showextrema=False, widths = 1)
#plt.setp(axes.collections, edgecolor="k", facecolor="lightgray", linewidth=12, alpha=1)

sns.violinplot(ax=axes[0], data = Cdata, 
                    linewidth = 12, width=1.3, color = "lightgray",
                    saturation=0.3, bw=0.5, cut=0.2, inner = None)
plt.setp(axes[0].collections, edgecolor="k")

flierprops = dict(marker='o', markerfacecolor='k', markersize=30,
                  linestyle='None', markeredgecolor='white')

axes[0].boxplot(Cdata,flierprops = flierprops, whis=None, positions=np.array([0,1]), showcaps=False,widths=0.15, patch_artist=True,
            boxprops=dict(color="k", facecolor="k"),
            whiskerprops=dict(color="k", linewidth=12),
            medianprops=dict(color="yellow", linewidth=28))


### Format the figure ###

axes[0].spines["bottom"].set_linewidth(14)
axes[0].spines["top"].set_linewidth(0)
axes[0].spines["right"].set_linewidth(0)
axes[0].spines["left"].set_linewidth(14)
axes[0].set_ylim(0,4)
axes[0].set_xlim(-0.8,1.8)

"""
#xlab1 = [ "sh-Ctrl", "sh-Scrib"]
xlab1 = [ "DMSO", "CK-869"]
xlab2 = ["(n=18)", "(n=31)"] 
xlabels = [f"{x1}\n{x2}" for x1, x2, in zip(xlab1,xlab2)]
axs[0].set_xticklabels(xlabels, fontname="Arial")

"""
axes[0].set_ylabel(r"Ratio of"+"\n"+"E-cad mean intensity,"+"\n" +"d-d contact vs. cortical",fontsize=75, fontname="Arial")
axes[0].get_yaxis().set_label_coords(-0.1,0.5)

### plot a bar for statistics ###
axes[0].hlines(y=3.5, xmin=0, xmax=1, linewidth=10, color='k')
axes[0].text(0.2, 3.65, "p<0.005", fontsize = 50, style = 'italic', fontname="Arial") #p=0.0032


### Ready to plot ###
axes[0].tick_params(axis='x',labelsize=0)
axes[0].tick_params(axis='y',labelsize=50)
axes[0].yaxis.set_major_locator(MaxNLocator(integer=True))

########################################################################################################################
sns.violinplot(ax=axes[1], data = Cdata2, 
                    linewidth = 12, width=1.3, color = "lightgray",
                    saturation=0.3, bw=0.5, cut=0.2, inner = None)
plt.setp(axes[1].collections, edgecolor="k")

flierprops = dict(marker='o', markerfacecolor='k', markersize=30,
                  linestyle='None', markeredgecolor='white')

axes[1].boxplot(Cdata2,flierprops = flierprops, whis=None, positions=np.array([0,1]), showcaps=False,widths=0.15, patch_artist=True,
            boxprops=dict(color="k", facecolor="k"),
            whiskerprops=dict(color="k", linewidth=12),
            medianprops=dict(color="yellow", linewidth=28))


### Format the figure ###

axes[1].spines["bottom"].set_linewidth(14)
axes[1].spines["top"].set_linewidth(0)
axes[1].spines["right"].set_linewidth(0)
axes[1].spines["left"].set_linewidth(14)
axes[1].set_ylim(0,9)
axes[1].set_xlim(-0.8,1.8)


xlab1 = [ "DMSO", "CK-869"]
xlab2 = ["(n=18)", "(n=31)"] 
xlabels = [f"{x1}\n{x2}" for x1, x2, in zip(xlab1,xlab2)]
axes[1].set_xticklabels(xlabels, fontname="Arial")


axes[1].set_ylabel(r"Ratio of"+"\n"+"NMIIb mean intensity,"+"\n"+"cortical vs. cytoplasmic",fontsize=75, fontname="Arial")
axes[1].get_yaxis().set_label_coords(-0.1,0.3)

### plot a bar for statistics ###
axes[1].hlines(y=8, xmin=0, xmax=1, linewidth=10, color='k')
axes[1].text(0.2, 8.3, "p<0.001", fontsize = 50, style = 'italic', fontname="Arial") #p=0.0009


### Ready to plot ###
axes[1].tick_params(axis='x',labelsize=75, rotation=45)
axes[1].tick_params(axis='y',labelsize=50)
