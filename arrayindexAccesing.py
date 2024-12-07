# #array is same as accesing the element from the array.
# #1-D array
# import numpy as np
# kirat=np.array([1,2,3,4,5])
# print(kirat[3])
# print(kirat[3]+kirat[4])
# #2-D array accesing the element of the 2-d array
# #it is like the roes and the columns->
# import numpy as np
# x=np.array([[1,2,3,4,5],[6,7,8,9,10,]])
# print("Accesing the 2nd element of the 2nd row : ",x[1][1])
# print("Accesing the 2nd row 4th element:",x[1][4])
# #Accesing the element from the 3-D array->
# import numpy as np
# y=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
# print("print the 3 index element from the 3-D array",y[0,0,3])
#***********************************NUMPY ARRAY SLICING***********************************
#slicing array-> slicing in python means taking the element from the one index to the other index.
#[start:end:steps]
#Now we will slice the element from 1-5
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10])
print(x [0:5])
print(x [4:])
#Negative Slicing->
# In Negative Index that it will not contain the element of the last one but  it will not take the
# element of the first one as->
#in below it not takes the value of -1 but it will not tke take the value of -9
print(x[-9:-1])
print(x[-1])
print(x[-8:-2])
# if we have to print the value from the 2-8 from the array then how we write as follows->
# we should write here that -2 to -9 as element in them.
print(x[-9:-2])
print(x[1:6:2])
# it will print the element as from the 1 to 6 as every 2nd number.
#Slicing 2-D array
import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a)
print(a[1,1:4:])
#Picking the 2nd indexing of both the arrays->
print(a[0,1:],a[1,1:])  # ---> it produces the 1-D array.
print(a[0:2 ,2]) #0 means the 0th index array 2 means the 1st index array and the 2 means that
# every 2nd element of the both array
print(a[0:2,1:4])
