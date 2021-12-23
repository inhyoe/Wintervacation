import numpy as np

y = [[1,2,3],[4,5,6],[7,8,9]]

np_array = np.array(y)

print(np_array)
print(np_array[::][::])
# 1 2 3 <--
# 4 5 6
# 7 8 9

np_array1 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 이렇게도 가능하다.

print(np_array1[0,2]) # 행렬이기에 가능하다.

np_array1[0,0] = 12
print(np_array1) # 수정 또한 가능하다.
# np_array1[0,0] = 1.234  -- >파이썬의 리스트와는 달리 넘파이는 자료형이 같아야 가능하다. 그러므로 소수점 이하값은 자동으로 삭제.

np_array2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(np_array2[0:3,1:4])
print(np_array2[::][::])
print(np_array2.shape)