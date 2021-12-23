import numpy as np


np_array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np_array1[np_array1>5]) # 1차원 배열 생성.

print(np_array1[np_array1[:,2]>5])

print(np_array1 % 2==0)

print(np_array1[ np_array1%2 == 0 ])