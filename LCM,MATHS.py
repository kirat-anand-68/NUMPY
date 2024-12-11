#Finding the lcm lowest commom multiple
#Here we will find the Multiple of two numbers
import numpy as np
x=3
y=9
z=np.lcm(x,y)
print(z)
kirat=np.array([1,2,3,4])
kirat_new=np.lcm.reduce(kirat)# reduce method will use the ufunc,
# in this lcm() func on each element and it will reduce the array by 1 dimension.
print(kirat_new)
#Here we will find the Lcm of all array here array contain the integers from 1 to 10
import numpy as np
sharad=np.arange(1,11)
sharad_new=np.lcm.reduce(sharad)
print(sharad_new)
#*************************Greatest Comman Denominator******************************
#finding the Greatest commmon denominator.
#here we will find the HCF of below two numbers
import numpy as np
x=3
x1=9
x2=np.gcd(x,x1)
print(x2) #Answer will be the 3 because it is the highest number and both number is divided by 3.
#Finding the GCD in an Array->
# reduce method will use the ufunc,
# in this gcd() func on each element and ,it will reduce the array by 1 dimension.
import numpy as np
kirat=np.array([20,8,32,16,36])
x2=np.gcd.reduce(kirat)
print(x2)
#It will return the 4 because 4 is the highest number that can be return between the array.
#************************************$ USE OF THE TRIGONOMETRIC FUNCTIONS ********************************
#Numpy provide the ufunc like sin(),cos() and tan() values that takes values in,
#radians and give the sin(),tan(),cos() values.
import numpy as np
c=np.sin(np.pi/2)
print(c)
b=np.tan(np.pi/4)
print(b)
#we will now find the sin values of the array->
f=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
f1=np.sin(f)
print(f1) #OUTPUT-[1.         0.8660254  0.70710678 0.58778525] these all are in radians
#Degree to Radians->
#By default all of the trigono functions takes radians as parameters
# NOTE->Radians values are pi/180*degree value.
#here we will convert all the array values into the radians:
p=np.array([90,180,270,360])
p1=np.deg2rad(p)
print(p1) #[1.57079633 3.14159265 4.71238898 6.28318531] in radians from degrees.

#RADIANS TO DEGREE->
#here we will convert radians to degree
import numpy as np
i=np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
i1=np.rad2deg(i)
print(i1)

#Here We can also find angles-> like arcsin(),srccos(),srctan()
#We will now find the angle of 1.0
r=np.arcsin(1.0)
print(r)
#Angles of each values in an array->
import numpy as np
m=np.array([1,-1,0.1])
m1=np.arcsin(m)
print(m1)
#*****************HYPOTANEOUS IN NUMPY ****************PYTHAGORES THEOREM********************
#hypot() function that takes the values in radians and produce the corresponding sin,cos and tan values.
#Here we will find the hypot() for 4 base and 3 perpendicular.
base=3
perpendicular = 4
o=np.hypot(base,perpendicular)
print("the Hypotaneous we get is:",o)
