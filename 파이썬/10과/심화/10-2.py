# 0 ~ 24까지의 값을 가지는 5x5크기의 2차원의 행렬n_arr생성
import numpy as np

n_arr = (np.arange(25)).reshape(5,5)
print(n_arr)

# n_arr의 가장 첫원소와 가장 마지막원소를 인덱싱 하여 다음과 같이 출력하기 마지막
# 원소의 인덱싱은 반드시 음수 값 사용
print(n_arr[0][0])
print(n_arr[-1][-1])

# n_arr 배열에 슬라이싱을 적용하여 다음과 같은 값을 가지는 배열을 생성하여라.

print(n_arr[::1][:2])
# == 
print(n_arr[:2])

# 4) 
print(n_arr[2::])
# 5)
print(n_arr[::,0::2]) 
# 6)
print(n_arr[::2,::2])
#7) 슬라이싱을 적용한 후 reshape을 적용하여 값을 가지는 배열 생성하기.

print(((n_arr[:2])).reshape(5,2))

