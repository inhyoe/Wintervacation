import numpy as np

array_a = np.array(range(0,10))
print(array_a)

array_b = np.array([0,1,2,3,4,5,6,7,8,9])
print(array_b)


array_c = np.array(range(0,10,2))
print(array_c)

print(array_c.shape) # m,n의 배열의 크기를 알려줌
print(array_c.ndim) # 배열 축 및 차원 의 개수
print(array_c.size) # 배열 원소의 개수
print(array_c.itemsize) # 배열내의 원소의크기를 바이트단위