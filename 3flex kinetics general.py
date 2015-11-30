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
    myfile_fig1 = 'sample1 CO2 298K.png'
    myfile_fig2 = 'sample2 CO2 298K.png'
if myfile == "CH4 298K.txt":
    myfile_label ='$\mathregular{CH_{4}}$ 298K'
    myfile_fig1 = 'sample1 CH4 298K.png'
    myfile_fig2 = 'sample2 CH4 298K.png'
if myfile == "C3H8 298K.txt":
    myfile_label = '$\mathregular{C_{3}H_{8}}$ 298K'
    myfile_fig1 = 'sample1 C3H8 298K.png'
    myfile_fig2 = 'sample2 C3H8 298K.png'
if myfile == "n-Butane.txt":
    myfile_label = '$\mathregular{n-C_{4}H_{10}}$ 298K'
    myfile_fig1 = 'sample1 n-C4H10 298K.png'
    myfile_fig2 = 'sample2 n-C4H10 298K.png'
if myfile == "iso-Butane.txt":
    myfile_label = '$\mathregular{iso-C_{4}H_{10}}$ 298K'
    myfile_fig1 = 'sample1 iso-C4H10 298K.png'
    myfile_fig2 = 'sample2 iso-C4H10 298K.png'
  
x1=data[:,3]
x1=x1/1000/60
y1=data[:,4]

x2=data[:,3]
x2=x2/1000/60
y2=data[:,22]

if myfile == "CO2 VT.txt":
    myfile_label = '$\mathregular{CO_{2}}$ 258K'
    myfile_fig1 = 'sample1 CO2 258K.png'
    myfile_fig2 = 'sample2 CO2 258K.png'
    x1=data[188028 :,3]
    x1=x1/1000/60
    y1=data[188028 :,4]
    x2=data[188028 :,3]
    x2=x2/1000/60
    y2=data[188028 :,22]
    
def figure_plot(x, y, myfile_label, myfile_fig):
    fig = plt.figure()
    fig.set_size_inches(6, 4)
    plot, = plt.plot(x,y,'ko', label=myfile_label)
    
    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()
    dx, dy = (xmax-xmin)*0.1, (ymax-ymin)*0.1
    plt.xlim(xmin-dx, xmax + dx)
    plt.ylim(ymin-dy, ymax + dy)
    plt.ylabel('Pressure (torr)')
    plt.xlabel('time (minutes)')
    
    ax = plt.gca()
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    plt.legend(numpoints=1, loc='upper left', frameon=False, title=None)
    plt.savefig(myfile_fig, format="png", dpi=600)
    plt.close()
    
# plot the first sample    
figure_plot(x1, y1, myfile_label, myfile_fig1)
# plot the second sample
figure_plot(x2, y2, myfile_label, myfile_fig2)
print("done")