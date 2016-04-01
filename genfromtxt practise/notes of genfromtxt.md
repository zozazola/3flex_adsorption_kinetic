#notes of genfromtxt

code:

```
import numpy as np

myfile = input("filename:")
data = np.genfromtxt(myfile)
print(data)
```

if the input file is:

```
genfromtxt test 1

234 34 123
34 234 78
324 768 8967
```
result is:

```
[[             nan              nan   1.00000000e+00]
 [  2.34000000e+02   3.40000000e+01   1.23000000e+02]
 [  3.40000000e+01   2.34000000e+02   7.80000000e+01]
 [  3.24000000e+02   7.68000000e+02   8.96700000e+03]]
```

if the input file is (one of the lines has only 2 numbers):

```
genfromtxt test 1

234 34 123
34 234 
324 768 8967
```
result is:

```
ValueError: Some errors were detected !
    Line #4 (got 2 columns instead of 3)
```
```
 get first two lines:
 x = data[0:2]
 get first two columes:
 x = data[:,0:2]
 from line_1, line_2 get colume_0, colume_1
 x = data[1:3,0:2]
 ```