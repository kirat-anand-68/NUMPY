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
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x=random.zipf(a=2,size=1000)
sns.distplot(x[x<10],kde=False)
plt.show()
