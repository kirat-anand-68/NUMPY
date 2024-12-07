import numpy as np
#We will create the numpy ndarray
#the array object in numpy is called ndarray
x=np.array([1,2,3,4])    #inside the list
print(type(x))
print(x)
#we can also pass the list tuple or any array to the array and it will pass ti the ndarray.
import numpy as np
y=np.array((1,2,3,4,5,6))
print(type(y))
print(y)
#Dimensions in array -> dimensions in array is 1 level of array depth(nested array)
#Array ke ander array usko nested array kehte haa
#0-D array / scalars array are the elements in the array, each value in an array is an 0-D.

# Now we crete the 0d array->
# nromally we use the 0-D array
#most basic and the common array is 1-D array.->
# 1_D->an array that has 0-D array as it elements that are called the unidirectional.
import numpy as np
print("The 2-D array is given below")
create=np.array([[1,2,3],[2,4,5]])
print(create)
print("Printing the 3-D array")
import numpy as np
e=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(e)
# to check the how many dimensions that the array have we use the ndim attribute->
print(e.ndim)
print(create.ndim)
# how to convvert the any array into the biggest array sing the ndim method as shown ->
import numpy as np
kirat=np.array([1,2,3,4],ndmin=5)
print(kirat)
print("The array is ",kirat.ndim)
# OUTPUT->[[[[[1 2 3 4]]]]]
# The array is  5
