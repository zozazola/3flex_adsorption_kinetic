# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:44:48 2015

@author: JIANGH
"""
#import numpy as np

# filename = input("filename: ")
filename = "CO2 VT.txt"
count_line = -3
count = []
fhand = open(filename)
for line in fhand:
    count_line += 1
    if line.startswith("#ManPress"):
        count.append(count_line)
        print("count: " + str(count_line))
        
print(count)
#data = np.genfromtxt(filename)
#for i in len(count):
#    newdata = data[count[i]:count[i+1]]
#    export_filename = str(i) + ".txt"
#    np.savetxt(export_filename, newdata)
    