# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

myfile = input("filename:")
data = np.genfromtxt(myfile, skip_header=2, skip_footer=1)

if myfile == "CO2 298K.txt":
    myfile_label = '$\mathregular{CO_{2}}$ 298K'
    myfile_fig1 = 'sample1 CO2 298K'
    myfile_fig2 = 'sample2 CO2 298K'
if myfile == "CH4 298K.txt":
    myfile_label ='$\mathregular{CH_{4}}$ 298K'
    myfile_fig1 = 'sample1 CH4 298K'
    myfile_fig2 = 'sample2 CH4 298K'
if myfile == "C3H8 298K.txt":
    myfile_label = '$\mathregular{C_{3}H_{8}}$ 298K'
    myfile_fig1 = 'sample1 C3H8 298K'
    myfile_fig2 = 'sample2 C3H8 298K'
    
# plot the first sample    
x1=data[:,3]
x1=x1/1000/60
y1=data[:,4]
plot1, = plt.plot(x1,y1,'ko', label=myfile_label)

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

plt.savefig(myfile_fig1, dpi=600)
plt.close()

# plot the second sample
x2=data[:,3]
x2=x2/1000/60
y2=data[:,22]

plot2, = plt.plot(x2,y2,'ko', label = myfile_label)

xmin2, xmax2 = x2.min(), x2.max()
ymin2, ymax2 = y2.min(), y2.max()
dx2, dy2 = (xmax2-xmin2)*0.1, (ymax2-ymin2)*0.1
plt.xlim(xmin2-dx2, xmax2 + dx2)
plt.ylim(ymin2-dy2, ymax2 + dy2)

plt.ylabel('Pressure (torr)')
plt.xlabel('time (minutes)')

ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.legend(numpoints=1, loc='upper left', frameon=False, title=None)

plt.savefig(myfile_fig2, dpi=600)
plt.close()
print("done")