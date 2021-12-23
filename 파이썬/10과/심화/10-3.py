# 난수로 이루어진 3x3x3 형태의 배열 a를 생성하기

import numpy as np


a = np.random.rand(3,3,3)
print(a)

#2 )
print('a원소들중 최댓값의',a.max())

# 3)
print('a원소들 중 최댓값의 위치',a.argmax())