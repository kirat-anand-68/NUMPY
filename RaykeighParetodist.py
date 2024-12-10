# #Exponential dist -> it describe the time . exponential define the time event of next data ie.success rate
# #parameters->scale()->inverse of rate,size
# #Here We will draw a sample for exponential dist with the 2.0 scale and 2*3 size.
# from numpy import random
# kirat=random.exponential(scale=2,size=(2,3))
# print(kirat)
#
# #Visualization
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.exponential(size=1000),hist=False)
# plt.show()
# #Poisson describe that ki koi bhi evevnt kitne time period ke liye huya hoega.
# #Exponential describe the time period between two period.
#*******************************Video 26****************************************
#Numpy CHISQUARE Distribution
#IT is basically use as a basis to verify the hypothesis.
#param(df(degree of freedom),size
#sample of chi square with df 2 and size 2*3
# from numpy import random
# kirat=random.chisquare(df=2,size=(2*3))
# print(kirat)
# #Visualization of ChiSquare
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.chisquare(df=2,size=150),hist=False)
# plt.show()
#********************************RAYLEIGH DISTRIBUTION***********************************
#Rayleigh Distribution->used for signal processing
#param-(scale-how flat the distribution is default-1.0,known as standard distribution),size
#sample 2.0 with size 2*3
# from numpy import random
# x=random.rayleigh(scale=2,size=(2*3))
# print(x)
# #VIsualization of Raylist
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.rayleigh(size=1000),hist=False)
# plt.show()
#***********************************PARETO DISTRIBUTION*************************************
#80:20 ->law 20 % factor cost and the 80% outcome cause -> 20 % mehnnet 80% result deti haa.
# 20% inverstment 80% result deti haa
#para>a(shape,sample),size
#Sample of pareto distribution
#shape 2 ans size 2*3
# from numpy import random
# kirat= random.pareto(a=2,size=(2,3))
# print(kirat)
# #VISUALIZATION
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.pareto(a=2,size=1000),kde=False)
# plt.show()
#***********************************ZIPF Distribution*************************************************
#zipf law-> it means that number of times, koi bhi term kitne bar occur hot ahaa usko zipf law kehte haa.
#Its defination is like common word in english occur nearly times as of the most hindi words
# para->a(dist para),size
#Sa,ple for zipdist a=2 size(2*3)
# from numpy import random
# x=random.zipf(size=(2,3),a=2)
# print(x)
#VISUALIZATION OF ZIPF
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# x=random.zipf(a=2,size=1000)
# sns.distplot(x[x<10],kde=False)
# plt.show()
#******************************NUMPY FROM COURSE*******************************************************
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
