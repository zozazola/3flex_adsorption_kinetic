# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:44:48 2015

@author: JIANGH
"""

filename = input("filename: ")
#filename = "CO2 VT.txt"
count_line = 0
count = []
fhand = open(filename)
for line in fhand:
    count_line += 1
    if line.startswith("#ManPress"):
        count.append(count_line)
        print("count: " + str(count_line))        
print(count)

file = open(filename, 'r')
data = file.readlines()
for i in range(len(count)):
    filename_new = str(i + 1) + ".txt"
    newfile = open(filename_new, 'w')
    newfile.write("gas")    
    newfile.write(str(i + 1))
    newfile.write("\n")
    if i == len(count) -1:
        newdata = data[count[i]-1:]
    else:
        newdata = data[count[i]-1:count[i+1]-1]
    for line in newdata: 
        newfile.write(line)
    newfile.close()
    
    