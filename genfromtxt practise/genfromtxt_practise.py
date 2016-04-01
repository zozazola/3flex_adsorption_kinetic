import numpy as np

myfile = "test_1.txt"
data = np.genfromtxt(myfile)
print(data)
x = data[1:3,0:2]
print(x)