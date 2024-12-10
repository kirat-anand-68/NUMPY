#Their are 5 ways of rounding of the decimals in numpy
#Truncation,fix,rounding,ceil,floor,
#these command remove the decimal and return the float number closest to zero.
# trunc() and fix()
import numpy as np
#It works on arrays or lists of numbers, and thus,
# the input should generally be enclosed in square brackets if you provide a list of numbers.
# x=np.trunc([-3.666,3.6666]) #output= -3 and 3 in float
# print(x)
# y=np.fix([-3.666,3.6666]) #output= -3 and 3 in float
# print(y)# Works SAME AS TRUNC
#You don't need square brackets when providing a single number to np.around,
# as the function is designed to work with both scalars and arrays
# u=np.around(3.1666,2) #output= -3 and 3 in float
# u1=np.around(3.5,4)
#Around() functions increment the preceding digits and decimal by nearest to 1 if n>5 it increment by 1 or n<5= it seems to be the zero 0
# And if it is equal to 5 it not change any cases.
# print(u)
# print(u1)
#Floor -> Round of the decimal to the lower integer
#Ceil -> it round of the integer to the upper integer
# u8=np.floor(3.5)
# u9=np.ceil(3.5)
# print(u8)
# print(u9)
#SUMMATION->addition id done between two argument while summation id done over n elements->
#ADDING TWO ARRAY
import numpy as np
from pandas.conftest import axis_1

kirat=np.array([1,2,3])
kirat1=np.array([4,5,6])
kirat3=np.add(kirat1,kirat1)
print(kirat3)
#Sum the value of two arrays
import numpy as np
kirat=np.array([1,2,3])
kirat1=np.array([4,5,6])
kirat3=np.sum([kirat1,kirat1])
print(kirat3)
#Summation over the Axis->if you specify axis=1 numpy sum the number in each array
import numpy as np
x=np.array([1,2,3])
x1=np.array([4,5,6])
x3=np.sum([x,x1],axis=1) # it gives in return the sum of the axis element .
print(x3)

#CUMMULATIVE SUM-> it means that the partially adding up the elements of the array
#{1,2,3,4]=>{1,1+2,1+2+3,1+2+3+4]=[1,3,6,10]
r=np.array([1,2,3,4])
r1=np.cumsum(r)
print(r1)
#products->prod() function here we will find the product of the element of the enelow array
kirat=np.array([1,2,3,4])
kirat_new=np.prod(kirat)
print(kirat_new)
#Here we will find the products of elemets in  2 differemt arrays
kirat=np.array([1,2,3,4])
kirat2=np.array([5,6,7,8])
kirat_new=np.prod([kirat,kirat2])
print(kirat_new)
#Product over an axis
kirat=np.array([1,2,3,4])
kirat2=np.array([5,6,7,8])
kirat_new=np.prod([kirat,kirat2],axis=1)
print(kirat_new)
#CUMULATIVE PRODUCT->
#The partial product of the [1,2,3,4] is[1,1*2,1*2*3,1*2*3*4]
kirat=np.array([1,2,3,4])
# kirat2=np.array([5,6,7,8])
kirat_new=np.cumprod(kirat)
print(kirat_new)
#********************************NUMPY DIFFERENCES************************************
#diff->Syntax for finding the difference->
q=np.array([1,2,4,5])
q_new=np.diff(q)
print(q_new)
#The descrete difference of this would be  [2-1,4-2,5-4]. by usig diff.


