# import numpy as np
# x=np.arange(0,10,2)
# y=np.zeros((2,5))
# z=np.linspace(0,10,3)#it give the evenly space number between 0 and 10,they give by default the float value.
# q=np.eye(5)#It is used to create the identity matrix.
# e=np.random.rand(1)
# e1=np.random.randn(2,3)
# e2=np.random.randint(0,100,(2,3))
# import numpy as np
#
# # Set the seed
# np.random.seed(42)
#
# # Generate random numbers
# print(np.random.rand(3))  # Output will always be the same when seed is 42
# #Return back the Integer Numbers
# print(e2)
# print(e)
# print(e1)
# print(z)
# print(y)
# print(x)
# print(q)
# ranarray=np.random.randint(0,101,20)
# p=ranarray.max()
# p1=ranarray.min()
# p_1=ranarray.argmax() #used to get the max value index
# p_2=ranarray.argmin() # used to get the min value index
# print("The Max value is find at:", p_1,"and the Max value is :",p)
# print("The Min value o find out at:",p_2,"And the Min value is",p1)
# print(ranarray)
#
# z=np.arange(0,10)
# print(z)
# z[:5]=100   # this is called the broadcasting as it allows to set all the values same as shown below->
# print(z)
# o=np.array([[1,2,3],[4,5,6]])
# print(o)
# o1=o[:2,1:]
# print(o1)
# z_=np.arange(0,10)
# z1=z_>4  # It will give the boolean values.
# print(z1)

#NUMPY OPERATIONS->
import numpy as np
z=np.arange(0,10)
print(z)
print(z+5)
print(z-2)
print(z+z)
print(z*z)
# print(z/z)#😛
print(np.sqrt(z))
print(np.sin(z))
# print(np.log(z))
print(z.max())
print(z.mean())
print(z.min())
print(z.std())
print(z.min())
arr2d=np.arange(0,25).reshape(5,5)
print(arr2d)
print(arr2d.sum())
print(arr2d.sum(axis=1)) # it will give the sum along the columns.
print(arr2d.sum(axis=0)) # it will give the sum along the rows
