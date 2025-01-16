import numpy as np

arr2=np.array([0,1,20,68,11,17,112,679,4,202])
print("before sorting;",arr2)
r=np.sort(arr2,kind='mergesort')
print("After sorting:",r)