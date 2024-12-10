#Ufunc-> stands for the universal functions and they are actually numpy functions and
# that operated on the ndarray.
# Ufunc also takes the arguments like where dtype and so on
#vestorization->converting the iterative statements into  a vector based system
#exmaple withour ufunc
x=[1,2,3,4]
y=[5,6,7,8]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)
#with Ufunc
import numpy as np
x=[1,2,3,4]
y=[5,6,7,8]
z=np.add(x,y)
print(z)
#***********************************Create yourOwn Ufunction*************************8
#to create your own ufunc,you have to define the function like you do in the normal python then add it to the numoy function using the frompufunc() method
#Arguments from pyfunction->function ,inputs and outputs
import numpy as np
def myadd(x,y):
    return x+y

myadd=np.frompyfunc(myadd,2,1) #2 means that 2 array are to be passed and the 1 means that only i output is their to be given.
print(myadd([1,2,3,4],[5,6,7,8]))

#Checking if this function is u function or not
import numpy as np
print(type(np.add))

#Concatenate
import numpy as np
# print(type(np.concatenate))

#What if Ufunc doesnot exist->
# import numpy as np
# print(type(np.huhu)) # random names

#Use an if statement to check the function is ufunc or not.
import numpy as np
if type(np.add) == np.ufunc:
    print('Yes this function is Ufunction')
else:
    print('no a ufunction')

#Arithmetic operators-> +,-,*,%,/
#by Using Ufunc
#here Now we will add Ufunc
import numpy as np
kirat=np.array([1,2,3,4,5,6])
kirat2=np.array([7,8,9,10,11,12])
kirat3=np.add(kirat,kirat2)
kirat4=np.subtract(kirat,kirat2)
kirat5=np.multiply(kirat,kirat2)
kirat6=np.divide(kirat,kirat2)
print(kirat3)
print(kirat4)
print(kirat5)
print(kirat6)

#Power function -> it raises the value from the first array to the
# power of the values to the second array and return the value to the new array
x=([1,2,3,4,5,6])
x1=([1,1,2,2,3,2])
x_new=np.power(x,x1)  # the i array is works as the base and the second array is works as the power to it
print(x_new)

#REMAINDER->mod(),remainder->Function return the remainder of the 1 st array to the 2nd array and
# result in the new array
q=([10,20,30,40,50,60])
q1=([4,7,6,9,8,4])
q2=np.mod(q,q1)
print(q2)
#By using the remainder
q=([10,20,30,40,50,60])
q1=([4,7,6,9,8,4])
q2=np.mod(q,q1)
print(q2)
#Quotient-> it gives the quotient
#The divmod() return the quotient and the mod
q=([10,20,30,40,50,60])
q1=([4,7,6,9,8,4])
q2=np.divmod(q,q1)  # it gives the quotient as well as remainder
print(q2)
#absolute() and abs() they do the same operation but we should use the
# absolute to avoid the confusion with the  maths.abs().
r=np.array([-1,-2,-3,-4,-5])
r1=np.absolute(r)
print(r1)    # it changes to absolute .
