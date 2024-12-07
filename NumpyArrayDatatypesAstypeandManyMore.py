# #Data types in Python-> string ,integer ,float ,boolean,complex
# #Data types in Numpy-. i integer,b-Boolean,f-float,u-Unsigned integer,M-Datetime,O-object,c-complex float
# #m- timedelta,S-string, U-for unicode string,V-memory.
# # we check the data type using the dtype.
# # import numpy as np
# # a=np.array(['a','b','c','d','e'])
# # b=np.array([1,2,3,4,5],dtype='S')
# # print(b)
# # print(b.dtype)
# # print(a.dtype)
# # x=np.array([1,2,3,4,5],dtype='i4')
# # print(x)
# # print(x.dtype)
# #converting the data type into the existing array  astype().
# import numpy as np
# x=np.array([1.1,1.2,1.3,0])
# x1=x.astype('i')
# #converting data type into bool
# x2=x.astype(bool)
# print(x)
# print(x.dtype)
# print(x1)
# print(x1.dtype)
# print(x2)
# print(x2.dtype)
#********************ARRAY COPY AND VIEW**************** .
# import numpy as np
# x=np.array([1,2,3,4,5])
# x1=x.copy()
# x[0]=78
# print(x)
# print(x1)
# # In copy as we make the copy of the array then if we change the array then the array copy not change
#
# import numpy as np
# y=np.array([1,2,3,4,5])
# y1=y.view()
# y[0]=56
# print(y)
# print(y1)
# In view as if we change the array then in the copy of that array also get change.
#**********************************SHAPING OF AN ARRAY**************************
# The shape of an array is the number of element in the each dimensions
import numpy as np
x=np.array([[1,2,3,4],[5,6,7,8]])
print(x.shape)
#it give(2,4) as their is 2 dimension having the 4 elements in it.

# now we will create the 5 dimensional array
import numpy as np
z=np.array([1,2,3,4,5],ndmin=5)
print(z)
print("shape of the array is :",z.shape)
