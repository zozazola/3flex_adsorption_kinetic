# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:19:39 2015

@author: JIANGH
"""

import numpy as np
import matplotlib.pyplot as plt

myfile = input("filename:")
data = np.genfromtxt(myfile, skip_header=2, skip_footer=1)

x1=data[:,3]
x1=x1/1000/60
y1=data[:,4]

x2=data[:,3]
x2=x2/1000/60
y2=data[:,22]

if myfile == "CO2 VT.txt":
    myfile_fig1 = 'sample1 CO2 VT.png'
    myfile_label_1 = '$\mathregular{CO_{2}}$ 298K'
    myfile_fig1_1 = 'sample1 CO2 298K.png'
    myfile_fig2_1 = 'sample2 CO2 298K.png'
    x1_1=data[0 : 53896,3]
    x1_1=x1_1/1000/60
    y1_1=data[0 : 53896,4]
    x2_1=data[0 : 53896,3]
    x2_1=x2/1000/60
    y2_1=data[0 : 53896,22]
    myfile_label_2 = '$\mathregular{CO_{2}}$ 288K'
    myfile_fig1_2 = 'sample1 CO2 288K.png'
    myfile_fig2_2 = 'sample2 CO2 288K.png'
    x1_2=data[53897 :100704,3]
    x1_2=x1_2/1000/60
    y1_2=data[53897 :100704,4]
    x2_2=data[53897 :100704,3]
    x2_2=x2_2/1000/60
    y2_2=data[53897 :100704,22]
    myfile_label_3 = '$\mathregular{CO_{2}}$ 273K'
    myfile_fig1_3 = 'sample1 CO2 273K.png'
    myfile_fig2_3 = 'sample2 CO2 273K.png'
    x1_3=data[100705 :188024,3]
    x1_3=x1_3/1000/60
    y1_3=data[100705 :188024,4]
    x2_3=data[100705 :188024,3]
    x2_3=x2/1000/60
    y2_3=data[100705 :188024,22]
    myfile_label_4 = '$\mathregular{CO_{2}}$ 258K'
    myfile_fig1_4 = 'sample1 CO2 258K.png'
    myfile_fig2_4 = 'sample2 CO2 258K.png'
    x1_4=data[188025 :,3]
    x1_4=x1_4/1000/60
    y1_4=data[188025 :,4]
    x2_4=data[188025 :,3]
    x2_4=x2/1000/60
    y2_4=data[188025 :,22]
    

fig = plt.figure()
fig.set_size_inches(6, 4)
plt.plot(x1_1,y1_1,'k.', label=myfile_label_1)
plt.plot(x1_2,y1_2,'r.', label=myfile_label_2)
plt.plot(x1_3,y1_3,'g.', label=myfile_label_3)
plt.plot(x1_4,y1_4,'b.', label=myfile_label_4)

xmin1, xmax1 = x1.min(), x1.max()
ymin1, ymax1 = y1.min(), y1.max()
dx1, dy1 = (xmax1-xmin1)*0.1, (ymax1-ymin1)*0.1
plt.xlim(xmin1-dx1, xmax1 + dx1)
plt.ylim(ymin1-dy1, ymax1 + dy1)
plt.ylabel('Pressure (torr)')
plt.xlabel('time (minutes)')

ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.legend(numpoints=1, loc='upper left', frameon=False, title=None)
plt.savefig(myfile_fig1, format="png", dpi=600)
plt.close()
print("done")
