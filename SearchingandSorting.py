#NUMPY SEARCHING ARRAY-> you can serach an array for a certain value and return the indexes that return the match.
# by using where
import numpy as np
kirat=np.array([1,2,3,4,5,4,4,4])
kirat_new=np.where(kirat == 4)
print(kirat_new)
z=np.array([1,2,3,4,5,6,7,8,9,10])
z1=np.where(z%2==0)   #it give the index values.
print(z1)

#SEARCH AND SORTED IN ARRAY->
#DO THE BINARY SEARCH IN ARRAY->
#We will now find the index where 7 should be inserted.
import numpy as np
x=np.array([6,7,8,9])
x1=np.searchsorted(x,9)
print(x1)   #output we get is (3)
# Now we will serach form the right side.
x2=np.searchsorted(x,8,side='left')
print(x2)
# # How to search the multiple values->
# import numpy as np                       #SKIP TILL FURTHER CLARIFICATION
# w1=np.array([1,3,5,7])
# w2=np.searchsorted(w1,[2,4,6])
# print(w2)
#NUMPY SORTING ARRAYS->
#sort()-> the numpy ndarray object has a function which is called the sort which sort the specify array.
import numpy as np
print("Sorting the 1-D array:")
x=np.array([8,3,9,5,7,4])
x2=np.sort(x)
print(x2)

print("Sorting the strings:")
z=np.array(['apple','cherry','banana'])
z2=np.sort(z)
print(z2)

print("Sorting the boolean array:")
q=np.array([True,False,True])
q1=np.sort(q)
print(q1)
print("Sorting the 2-D array:")
c=np.array([[3,2,4],[5,0,1]])
c1=np.sort(c)
print(c1)
