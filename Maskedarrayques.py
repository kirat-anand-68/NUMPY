import numpy as np

arr = np.random.randint(1, 20, (4, 4))
print(arr)
mask=np.eye(4,dtype=bool)
mx=np.ma.array(arr,mask=mask)
print(mx.mean())


import numpy as np

# Generate a 4x4 random integer array
arr = np.random.randint(1, 20, (4, 4))
print("Original Array:\n", arr)

# Mask values that are <= 10
mx = np.ma.masked_where(arr <= 10, arr)

# Compute the sum of numbers > 10
result = mx.sum()
print("Sum of values > 10:", result)
