#Normal Distribution is also called the Gaussian distribution-> very important it is part of permutation->
#random.normal is used for normal data visualization it has three level mean(loc) ,size and scale
# We are Generating a Random Normal Distribution of size 2*3
# from numpy import random
# kirat=random.normal(size=(2,3))
# print(kirat)
# #Here we will generate a random normal distribution of size 2*3 with mean at 1 and scale (standard deviation) of 2
# from numpy import random
# kirat1=random.normal(loc=1,scale=2,size=(2,3))
# print(kirat1)

#Visualization form normal distribution->
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.normal(size=1000),hist=False)
# plt.show()

#The Curve of the normal dist is known as bell curve.

#NUMPY BINOMIAL DISTRIBUTION-> it is also known as the decrete distribution->
#3 Parameters-> n=no.of trials, p=probability, size=(shape-return)
#Given 10 trials for a coin which will generate the 10 data points.
# from numpy import random
# kirat=random.binomial(n=10,p=0.5,size=10)
# print(kirat)
#
#
# #Visualization of Binomial
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=True,kde=False)
# plt.show()
#Difference Between normal and Binomial
#Normal is continous nd the Binomial is descrete.
#use 500 data point for binamial and under 100 data point for normal distribution.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50,scale=5,size=1000),hist=False, label='Normal')
sns.distplot(random.binomial(n=100,p=0.5,size=1000),hist=False, label='Binomial')
plt.show()




