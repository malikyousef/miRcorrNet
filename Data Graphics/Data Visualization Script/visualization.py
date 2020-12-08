# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:33:28 2020

@author: goygokhanPC
"""

#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#
#
#df = pd.read_excel('D:\\YaptigimCalismalar\\Malik Hoca\\Data Visualization\\whole_Results.xlsx')
#fig = plt.figure(num=None, figsize=(50, 15), dpi=300)
#index = ['BLCA-maTE',
#'BLCA-miRcorrNet',
#'BLCA-svm-rfe-8',
#'BLCA-svm-rfe-125',
#'BRCA-maTE',
#'BRCA-miRcorrNet',
#'BRCA-svm-rfe-8',
#'BRCA-svm-rfe-125',
#'KICH-maTE',
#'KICH-miRcorrNet',
#'KICH-svm-rfe-8',
#'KICH-svm-rfe-125',
#'KIRC-maTE',
#'KIRC-miRcorrNet',
#'KIRC-svm-rfe-8',
#'KIRC-svm-rfe-125',
#'KIRP-maTE',
#'KIRP-miRcorrNet',
#'KIRP-svm-rfe-8',
#'KIRP-svm-rfe-125',
#'LUAD-maTE',
#'LUAD-miRcorrNet',
#'LUAD-svm-rfe-8',
#'LUAD-svm-rfe-125',
#'LUSC-maTE',
#'LUSC-miRcorrNet',
#'LUSC-svm-rfe-8',
#'LUSC-svm-rfe-125',
#'PRAD-maTE',
#'PRAD-miRcorrNet',
#'PRAD-svm-rfe-8',
#'PRAD-svm-rfe-125',
#'STAD-maTE',
#'STAD-miRcorrNet',
#'STAD-svm-rfe-8',
#'STAD-svm-rfe-125',
#'THCA-maTE',
#'THCA-miRcorrNet',
#'THCA-svm-rfe-8',
#'THCA-svm-rfe-125',
#'UCEC-maTE',
#'UCEC-miRcorrNet',
#'UCEC-svm-rfe-8',
#'UCEC-svm-rfe-125'
#]
#
#barWidth = 0.04
#
#ax = fig.add_subplot(111) # Create matplotlib axes
#ax2 = ax.twinx()
#
#
#
##df = pd.read_excel('C:\\Users\\goygokhanPC\\Dropbox\\Samed_Burcue\\Results\\Figure Result Summary.xlsx')
#
#df.index=index;
#
#df.Number_Of_Genes.plot(kind='bar', color='green', ax=ax, width=barWidth, position=3,rot=0)
#df.Accuracy.plot(kind='bar',color='yellow',width=barWidth,position=2)
#df.Sensitivity.plot(kind='bar', color='black',width=barWidth, position=1)
#df.Area_Under_Curve.plot(kind='bar', color='red', ax=ax2, width=barWidth, position=0,rot=0)
#
#
#ax.set_ylabel('Number Of Genes',fontsize=15)
#ax2.set_ylabel('Area Under Curve',fontsize=15)
##ax.legend(loc='bottom center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)
#ax2.legend(loc='upper center', bbox_to_anchor=(0.595, 1),ncol=3, fancybox=True, shadow=True,fontsize=12)
#ax.legend(loc='upper center', bbox_to_anchor=(0.4, 1),ncol=3, fancybox=True, shadow=True,fontsize=12)
#
#
##ax.tick_params(axis='x', rotation=0,labelsize=20)
#ax.tick_params(axis='x',rotation=90,labelsize=10)
#
#plt.title(label="Cluster Level 2" , loc="center",fontsize=25)
#
#plt.show();


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.rc('font', **font)

df = pd.read_excel('D:\\YaptigimCalismalar\\Malik Hoca\\Data Visualization\\Diseases_Data\\UCEC.xlsx')
fig = plt.figure(num=None, figsize=(50, 15), dpi=100)
index = ['maTE','miRcorrNet','svm-rfe-8','svm-rfe-125'];

barWidth = 0.08

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx()



#df = pd.read_excel('C:\\Users\\goygokhanPC\\Dropbox\\Samed_Burcue\\Results\\Figure Result Summary.xlsx')

df.index=index;

df.Number_Of_Genes.plot(kind='bar', color='#C53248', ax=ax, width=barWidth, position=0.5,rot=0)
df.Accuracy.plot(kind='bar',color='#18E1E6',width=barWidth,position=1.5)
df.Sensitivity.plot(kind='bar', color='#67AB52',width=barWidth, position=2.5)
df.Area_Under_Curve.plot(kind='bar', color='#0404E9', ax=ax2, width=barWidth, position=3.5,rot=0)


ax.set_ylabel('Number Of Genes',fontsize=25)
ax2.set_ylabel('Area Under Curve',fontsize=25)
#ax.legend(loc='bottom center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)
ax2.legend(loc='lower center', bbox_to_anchor=(0.7, 1),ncol=3, fancybox=True, shadow=True,fontsize=30)
ax.legend(loc='lower center', bbox_to_anchor=(0.44, 1),ncol=3, fancybox=True, shadow=True,fontsize=30)
plt.rcParams.update({'font.size': 22})

#ax.tick_params(axis='x', rotation=0,labelsize=20)
ax.tick_params(axis='x',rotation=90,labelsize=30)
ax.grid();

plt.title(label="Cluster Level 2" , loc="left",fontsize=30)

plt.show();


