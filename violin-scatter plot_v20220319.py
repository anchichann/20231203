# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:46:29 2021

@author: achang

Set subplot spicing:
    https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots-in-matplotlib


"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns
import pandas as pd
import matplotlib.patches as mpatches

##############################################################################################################
##############################################################################################################
### Load data ################################################################################################
#################        Data shScrib       ##########################
# for DNA distance vs width
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210311 MCF10A (pRS-SKD) daughter width\SKD-width.xlsx')

# for width vs Ecad (intensity)
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20181017 MCF10A (shScrib vs pRS) - Intensity Scrib, Ecad\SKD-Ec-Width_v2022.xlsx')

# for Scrib vs Ecad (intensity)
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20181017 MCF10A (shScrib vs pRS) - Intensity Scrib, Ecad\SKD-Sc-Ec_v2022.xlsx')


#################        Data siScrib       ##########################
# for DNA distance vs width
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210108 MCF10A siScrib, cortical, AJ intensity (Ecad)\Si-daughter width.xlsx')

# for width vs Ecad (intensity)
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210108 MCF10A siScrib, cortical, AJ intensity (Ecad)\Si-Ec-width_v20220319.xlsx')

# for Scrib vs Ecad (intensity)
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210108 MCF10A siScrib, cortical, AJ intensity (Ecad)\Si-Sc-Ec_v20220319.xlsx')


#################        Data CK-869       ##########################
# for DNA distance vs width
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210110-2 MCF10A (DMSO vs CK869) (Scrib, Ecad), daughter width\CK-daughter width.xlsx')

# for width vs Ecad (ratio)
#df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210110-2 MCF10A (DMSO vs CK869) (Scrib, Ecad), daughter width\CK-Ec-width_v20220319.xlsx')

# for Myosin II vs Ecad (ratio)
df = pd.read_excel (r'C:\Users\ACHANG\Desktop\Swinburne Research\(2-2) Statistcs -MCF10A\20210110-2 MCF10A (DMSO vs CK869) (Scrib, Ecad), daughter width\CK-Ec-M2_v20220319.xlsx')


################################################################################################################
################################################################################################################
### Data Structuring ###########################################################################################

CDDD=df["CDDD"] # Control daughters' DNA distance
CDW=df["CDW"] # Conrol daughters' width / and other variable (intensity)
SDDD=df["SDDD"] #si(sh and drug) daughters' DNA distance
SDW=df["SDW"] # si(sh and drug) daughters' width  / and other variable (intensity)

#################################################################################################################
#################################################################################################################
#################        Data shScrib       ##########################
# For data set sh-ctrl vs sh-Scrib  - width vs DNA distance
#data1=[CDW[0:35],SDW[0:24]]
#data2=[CDDD[0:35],SDDD[0:24]]

# For data set sh-ctrl vs sh-Scrib  - 'width vs Ecad intensity' or 'Sc intensity vs Ec intensity'
#data1=[CDW[0:24],SDW[0:25]]
#data2=[CDDD[0:24],SDDD[0:25]]


#################        Data siScrib       ##########################
# For data set siScrib vs siControl
#data1=[CDW[0:25],SDW[0:30]]
#data2=[CDDD[0:25],SDDD[0:30]]


#################        Data CK-869       ##########################
# For data set DMSO vs CK-869 - width vs DNA distance
#data1=[CDW[0:19],SDW[0:29]]
#data2=[CDDD[0:19],SDDD[0:29]]

# For data set DMSO vs CK-869 - 'width vs Ecad intensity ratio'
data1=[CDW[0:18],SDW[0:31]]
data2=[CDDD[0:18],SDDD[0:31]]


###################################################################################################################
###################################################################################################################
### Figure design ###
#plt.style.use('default')

fig, axes = plt.subplots(2, 2, figsize=(9,9), gridspec_kw={
                           'width_ratios': [1, 2],
                           'height_ratios': [2, 1]})
fig.tight_layout(pad=0) #for adjusting the spacing between subplot 
axes[1, 0].axis('off')

##################################################################################################################
##################################################################################################################

##################################################################################################################
### for Subfig [1,0] ###
##################################################################################################################
### for Subfig [0,0] ###
colors_list = ['white', 'gray']
sns.violinplot(ax=axes[0, 0], data=data1, linewidth = 4, width=1.2, palette=colors_list,
                    saturation=0.3, bw=0.5, cut=0.2, inner = None)
plt.setp(axes[0,0].collections, edgecolor="k")


flierprops = dict(marker='o', markerfacecolor='k', markersize=10,
                  linestyle='None', markeredgecolor='white')
axes[0,0].boxplot(data1, flierprops = flierprops, whis=None, positions=np.array([0,1]), showcaps=False,widths=0.2, patch_artist=True,
            boxprops=dict(color="k", facecolor="k"),
            whiskerprops=dict(color="k", linewidth=4),
            medianprops=dict(color="yellow", linewidth=8))

axes[0,0].spines["bottom"].set_linewidth(7)
axes[0,0].spines["top"].set_linewidth(7)
axes[0,0].spines["right"].set_linewidth(0)
axes[0,0].spines["left"].set_linewidth(7)
axes[0,0].set_facecolor('whitesmoke')


xlab1 = [ "sh-Ctrl", "sh-Scrib"]
#xlab2 = ["(n=35)", "(n=24)"] 
#xlab1 = [ "si-Ctrl", "si-Scrib"]
#xlab2 = ["(n=25)", "(n=30)"] 
#xlab1 = [ "DMSO", "CK-869"]
#xlab2 = ["(n=26)", "(n=24)"] 
#xlabels = [f"{x1}\n{x2}" for x1, x2, in zip(xlab1,xlab2)]
axes[0,0].set_xticklabels(xlab1, fontname="Arial", fontsize = 0, rotation=45)
axes[0,0].set_xlim(-0.8,1.8)

axes[0,0].set_ylabel("Width of daughters' contact", fontname="Arial", fontsize = 0)
axes[0,0].tick_params(axis='y',labelsize=28)
#axes[0,0].set_ylim(0,23) # for d-d width
#axes[0,0].set_ylim(0,3100) # for (shScrib) Scrib intensity
#axes[0,0].set_ylim(0,2000) # for (siScrib) Scrib intensity
axes[0,0].set_ylim(0,4.1) # for (CK869) Myosin II ratio


###########################################################################################################
### for subfig [0,1] ###
#sns.scatterplot(ax=axes[0, 1], data=data1)

axes[0,1].scatter(CDDD, CDW, s=500, c='white', marker="o", edgecolor='black', linewidth=3) #label='first')
axes[0,1].scatter(SDDD, SDW, s=500, c='gray', marker="o", edgecolor='black', linewidth=3) #label='second')

## For data si=Scrib
#black_patch = mpatches.Patch(color='k', label='si-Ctrl', hatch ='o', lw=0.5, ls='-')
#red_patch = mpatches.Patch(color='red', label='si-Scrib', hatch ='o', lw=0.5, ls='-')

#black_patch = mpatches.Patch(color='k', label='DMSO', hatch ='o', lw=0.5, ls='-')
#red_patch = mpatches.Patch(color='red', label='CK-869', hatch ='o', lw=0.5, ls='-')

#black_patch = mpatches.Patch(color='k', label='sh-Ctrl', hatch ='o', lw=0.5, ls='-')
#red_patch = mpatches.Patch(color='red', label='sh-Scrib', hatch ='o', lw=0.5, ls='-')

#axes[0,1].legend(handles=[black_patch, red_patch], loc='upper left',fontsize=28, labelspacing=0.2, handletextpad=0.4, framealpha=0) # for CK-869
#axes[0,1].legend(handles=[black_patch, red_patch], loc='upper right',fontsize=28) # for sh-Scrib, si-Scirb

axes[0,1].spines["bottom"].set_linewidth(7)
axes[0,1].spines["top"].set_linewidth(7)
axes[0,1].spines["right"].set_linewidth(7)
axes[0,1].spines["left"].set_linewidth(7)
axes[0,1].set_facecolor('whitesmoke')

#axes[0,1].set_xlabel('Distance of daughters DNA', fontname="Arial", fontsize = 22)
axes[0,1].tick_params(axis='x',labelsize=0, length=10, width=5)
#axes[0,1].set_xlim(0,18) # for DNA distance
#axes[0,1].set_xlim(0,2200) # for (shScrib) Ecad intensity
#axes[0,1].set_xlim(0,3300) # for (siScrib) Ecad intensity
axes[0,1].set_xlim(0,3.4) # for (CK869) Ecad intensity ratio

#axes[0,1].set_ylabel('Width of daughters contact', fontname="Arial", fontsize = 22)
axes[0,1].tick_params(axis='y',labelsize=0, length=10, width=5)
#axes[0,1].set_ylim(0,23) # for d-d width
#axes[0,1].set_ylim(0,3100) # for (shScrib) Scrib intensity
#axes[0,1].set_ylim(0,2000) # for (siScrib) Scrib intensity
axes[0,1].set_ylim(0,4.1) # for (CK869) Myosin II ratio


###############################################################################################################
### for subfig [1,1] ###
sns.violinplot(ax=axes[1, 1], data=data2, orient="h", linewidth = 4, width=1.2, palette=colors_list,
                    saturation=0.3, bw=0.5, cut=0.2, inner = None)
plt.setp(axes[1,1].collections, edgecolor="k")


flierprops1 = dict(marker='o', markerfacecolor='k', markersize=10,
                  linestyle='None', markeredgecolor='white')

axes[1,1].boxplot(data2, vert=False, flierprops = flierprops1, whis=None, positions=np.array([0,1]), showcaps=False,widths=0.2, patch_artist=True,
            boxprops=dict(color="k", facecolor="k"),
            whiskerprops=dict(color="k", linewidth=4),
            medianprops=dict(color="yellow", linewidth=8))

axes[1,1].spines["bottom"].set_linewidth(7)
axes[1,1].spines["top"].set_linewidth(0)
axes[1,1].spines["right"].set_linewidth(7)
axes[1,1].spines["left"].set_linewidth(7)
axes[1,1].set_facecolor('whitesmoke')


#ylab1 = [ "sh-Ctrl", "sh-Scrib"]
#ylab2 = ["(n=26)", "(n=24)"] 
#ylab1 = [ "si-Ctrl", "si-Scrib"]
#ylab2 = ["(n=25)", "(n=30)"] 
ylab1 = [ "DMSO", "CK-869"]
#ylab2 = ["(n=19)", "(n=29)"] 
#ylabels = [f"{x1}\n{x2}" for x1, x2, in zip(ylab1,ylab2)]
axes[1,1].set_yticklabels(ylab1, fontname="Arial", fontsize = 0, rotation = 45)
axes[1,1].set_ylim(-0.8,1.8)

axes[1,1].set_xlabel("Distance b/w daughters' nucleus", fontname="Arial", fontsize = 0)
axes[1,1].tick_params(axis='x',labelsize=28)

#axes[1,1].set_xlim(0,18) # for DNA width
#axes[1,1].set_xlim(0,2200) # for (shScrib) Ecad intensity
#axes[1,1].set_xlim(0,3300) # for (siScrib) Ecad intensity
axes[1,1].set_xlim(0,3.4) # for (CK869) Ecad intensity ratio

# for data sh-Scrib
#axes[1,1].vlines(x=17, ymin=0, ymax=1, linewidth=5, color='k')
#axes[1,1].text(18, 0.5, 'N.S.', style='italic', rotation = 270,
#        verticalalignment='center', horizontalalignment='center', color='K', fontsize=24) #p=0.7605

# for data CK-869
#axes[1,1].vlines(x=19, ymin=0, ymax=1, linewidth=5, color='k')
#axes[1,1].text(20, 0.5, 'N.S.', style='italic', rotation = 270,
#        verticalalignment='center', horizontalalignment='center', color='K', fontsize=24) #p=0.6215


# for data si-Scrib
#axes[1,1].vlines(x=17, ymin=0, ymax=1, linewidth=5, color='k')
#axes[1,1].text(18, 0.5, 'N.S.', style='italic', rotation = 270,
#        verticalalignment='center', horizontalalignment='center', color='K', fontsize=24) #p=0.0499

###################################################################################################

plt.show()


####################################################################################################
#ax1.set_title('data 1')
#ax1.set_xlabel('x')
#ax1.set_ylabel('y')
#ax1.tick_params(axis='both', which='major', labelsize=20)

#ax2.set_title('data 2')
#ax2.set_xlabel('x')
#ax2.set_ylabel('y')
#ax2.tick_params(axis='both', which='major', labelsize=20)
#ax2.set_ylim(0, 50)
#ax2.set_xlim(0, 50)


#ax4.set_title('data 2')
#ax4.set_xlabel('x')
#ax4.set_ylabel('y')
#ax4.tick_params(axis='both', which='major', labelsize=20)

