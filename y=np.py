import numpy as np

y=np.ones((3,3))
print(y.dtype)
y=y.astype('int')
print(y)
print(y.reshape(3,3,1))

