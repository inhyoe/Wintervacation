
# 5x5크기의 행렬 생성 후 내부는 모두 0,1로 이루어져있다.
import numpy as np


x = np.array([x%2 for x in range(1,26)])
print(x)
print(x.reshape(5,5))

#2)
print(sum(x.reshape(5,5)))
