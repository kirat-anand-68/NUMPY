import numpy as np
# joining the numpy array
#Here for this we will pass the concatenate.
kirat=np.array([1,2,3])
kirat1=np.array([4,5,6])
kirat2=np.concatenate((kirat,kirat1))
print(kirat2)

#Joining of 2-D arrays along with rows(axis=1)
import numpy as np
kirat=np.array([[1,2,3],[4,5,6]])
kirat1=np.array([[7,8,9],[10,11,12]])
kirat2=np.concatenate((kirat,kirat1),axis=1)
print(kirat2)
#Joining of Array using the Stack Function->
import numpy as np
kirat=np.array([1,2,3])
kirat1=np.array([4,5,6])
kirat2=np.stack((kirat,kirat1),axis=1)   #it join the array with the indexes
print(kirat2)

# Stacking along with the rows
import numpy as np
kirat=np.array([1,2,3])
kirat1=np.array([4,5,6])
kirat2=np.hstack((kirat,kirat1))
print(kirat2)

# STacking along with columns->
import numpy as np
kirat=np.array([1,2,3])
kirat1=np.array([4,5,6])
kirat2=np.vstack((kirat,kirat1))
print(kirat2)

#STackinh along with height(depth)
import numpy as np
kirat=np.array([1,2,3])
kirat1=np.array([4,5,6])
kirat2=np.dstack((kirat,kirat1))
print(kirat2)

