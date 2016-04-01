

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

myfile = "Ar_87K.txt"
data = np.genfromtxt(myfile, skip_header=2, skip_footer=0)

x1=data[:,0]
y1=data[:,1]

x2=data[:,2]
y2=data[:,3]

myfile_label = '$\mathregular{CO_{2}}$ 298K'
myfile_fig1 = 'sample1 CO2 298K.png'

def figure_plot(x, y, myfile_label, myfile_fig):
    fig = plt.figure()
    #fig.set_size_inches(6, 4)
    plot, = plt.plot(x,y,"o", 
        label=myfile_label, 
        markeredgecolor="blue", 
        markerfacecolor="white")
    
    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()
    dx, dy = (xmax-xmin)*0.1, (ymax-ymin)*0.2
    plt.xlim(xmin-dx, xmax + dx)
    plt.ylim(ymin-dy, ymax + dy)
    plt.ylabel('Pressure (torr)')
    plt.xlabel('time (minutes)')
    
    ax = plt.gca()
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    plt.legend(numpoints=1, loc='best', frameon=False, title=None)
    plt.savefig(myfile_fig, format="png", dpi=200)
    Image.open(myfile_fig).save("test.tiff", "TIFF")
    plt.close()

figure_plot(x1, y1, myfile_label, myfile_fig1)