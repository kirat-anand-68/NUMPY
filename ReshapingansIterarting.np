#
# #Array ke shape ko reshape krna elements ko add remove krna or elements ke uper operations krna.
# import numpy as np
# #1-D to 2-D
# kirat=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# kirat1=kirat.reshape(4,3) #reshaping the array into the (4,3) type as 4 array having the three-three elements
# print(kirat)
# print(kirat1)
#
# import numpy as np
# #1-D to 3-D
# kirat=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# kirat2=kirat.reshape(2,3,2)
# print(kirat)
# print(kirat2)
# print(kirat2[1][1][1]) # Accessing the elements
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x.reshape(2,4).base)
# this is the view as view not change the array.

import numpy as np
z=np.array([1,2,3,4,5,6,7,8])
z1=z.reshape(2,2,-1)
print(z1)
# Here -1 is an unknown dimensions as it automatically reshape the array


# Flatening the array by converting the multidimensional array in 1-D
# by passing the -1 in the reshape it will convert the array into the 1-D array whether it is,
# of 2-D or it is iof 3-D
import numpy as np
p=np.array([[1,2,3,4],[5,6,7,8]])
p1=p.reshape(-1)
print(p1)
# their are a lot of functions for channging the shapes of an arrayin mupy,likeflatten,ravel and also rearranging the
# the elemenst like rot90,flip,fliplr,flipud they all are actualy comes underadvanced numpy.


#*************************************NUMPY ARRAY ITERATING*********************************
# It means that going through the elements one by one or step by step.
# Iterate the 1-D
import numpy as np
kirat=np.array([1,2,3])
for i in kirat:
    print(i)

#Iteraret in 2-D
import numpy as np
kirat=np.array([[1,2,3],[4,5,6]])
for i in kirat:
    print(i)

#Iterarte on Each Elemet->
import numpy as np
u=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in u:
    for a in i:
        print(a)
#Iterate 3-D
import numpy as np
e=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in e:
    for j in i:
        for k in j:
            print(k)

#Iterating the arrays using the nditer() functions->
# Helping functions for used in the basic to advanced functions to call then using the loops->
import numpy as np
kirat=np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(kirat):
    print(i)

import numpy as np
q=np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(q[: ,::3]):
    print(i)




