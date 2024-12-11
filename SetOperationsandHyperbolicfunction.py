#Hyperbolic Functions->#Numpy provide the ufunc like sinh(),cosh() and tanh() values that takes values in,
#radians and give the sinh(),tanh(),cosh() values.
#Here we will find the value of sinh
import numpy as np
x=np.sinh(np.pi/2)
print(x)

#We will now find the values on array
h=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
h1=np.sinh(h)
print(h1)
#FINDING THE ANGLES->Here We can also find angles-> like arcsinh(),srccosh(),srctanh()
r=np.arcsinh(1.0)
print(r)

import numpy as np
m=np.array([0.1,0.2,0.3])
m1=np.arctanh(m)
print(m1)

#******************************************8SETS******************************************************
#A set is a collection of the elemenst
#For creating the set we use unique() method to find the unique elements from any array.
#Here we will convert the repeated elements to the set
import numpy as np
j=np.array([1,2,3,4,4,55,6,7,78,89,7,])
j1=np.unique(j) #[ 1  2  3  4  6  7 55 78 89]
print(j1)

#for finding the unique array on two different array we use union1d()method
import numpy as np
kirat1=np.array([1,2,3,4])
kirat2=np.array([3,4,5,6])
kirat_new=np.union1d(kirat1,kirat2)
print(kirat_new)  #[1 2 3 4 5 6]

#To find the Intersection value that to find the common value only
# then we do by the use of the intersection
kirat_0=np.intersect1d(kirat1,kirat2,assume_unique=True) # with the assume_unique the processing time delays.
print(kirat_0)  #[3 4]

#SEt-Difference To find the values that are in the first set not in the second set.
kirat1=np.array([1,2,3,4])
kirat2=np.array([3,4,5,6])
l=np.setdiff1d(kirat1,kirat2)
l1=np.setdiff1d(kirat2,kirat1)
print(l1) #[5 6]
print(l)#[1 2]

#To find the values that are not in the both the sets
kirat1=np.array([1,2,3,4])
kirat2=np.array([3,4,5,6])
p=np.setxor1d(kirat1,kirat2)
print(p) #[1 2 5 6]
