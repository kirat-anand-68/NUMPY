#Getitng some elements out of some existing array and creating new array is called filterimg
# A Booleanindex list is a listof boolean corresponding to indexes in the array(True and False)
# import numpy as np
# x=np.array([41,42,43,44])
# x1=[True,False,True,True]
# x1_final=x[x1]    # To match the indexing
# print(x1_final)
#Now we will create a Filter Array
#That will return only the values higher tahn 42
import numpy as np
x=np.array([41,42,43,44])
emptyx=[]
for i in x:
    if i > 42:
        emptyx.append(True)
    else:
        emptyx.append(False)
x_new=x[emptyx]
print(emptyx)
print(x_new)
#Create a filter array that will return only the even number form the array->
import numpy as np
kirat=np.array([2,3,1,4,5,6,7,8,9,88,67,65,64])
kirat_new=[]
for elements in kirat:
    if elements%2==0:
        kirat_new.append(True)
    else:
        kirat_new.append(False)
kirat2=kirat[kirat_new]
print(kirat2)
print(kirat_new)
#***************************CREATE FILTER DIRECTLY FROM THE ARRAY**************************
import numpy as np
u=np.array([43,54,41,4,80])
u_new=u>42
u2=u[u_new]
print(u2)
#2nd example->
import numpy as np
kirat=np.array([2,3,1,4,5,6,7,8,9,88,67,65,64])
kirat_new=kirat%2==0
kirat2=kirat[kirat_new]
print(kirat2)
# ******************************************************************************************************
#*************************************NUMPY RANDOM NUMBERS->*******************************************
# Random means that something that cannot be predicted logically->
from numpy import random
# Now we will create a random number form 0-100
kirat=random.randint(0,101)
kirat2=random.rand()*10
print(kirat2)
print(kirat)
#You can also generate the random array->
# We will generate the 1-D array form the random integers->

from numpy import random
kirat=random.randint(100,size=(5))
print(kirat)
# We will generate the 2-D array with 3-rows each row will contain the 5 random int form 0-100
# form the random integers->
from numpy import random
kirat1=random.randint(100,size=(3,5))
print(kirat1)
# We will generate the 1-D array with 3-rows each row will contain the 5 random float
from numpy import random
kirat=random.rand(5)
print(kirat)
# We will generate the 2-D array with 3-rows each row will contain the 5 random float
from numpy import random
kirat=random.rand(3,5)
print(kirat)
#You can also generate the random numbers from the array->
#choice()
from numpy import random
kirat=random.choice([1,2,3,4,5,6])
print(kirat)
# Generate the random array form 2-D array
from numpy import random
kirat=random.choice([1,2,3,4,5,6],size=(3,5))
print(kirat)
