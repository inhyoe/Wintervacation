import numpy as np

y = np.arange(12)

print(y.reshape(2,-1)) # new_array = old_array.reshape(1차원,2차원,3차원)
print(y.reshape(6,-1)) # -1 = 데이터의 개수에 맞춰 자동으로 배열의 형태가 결정.

# -------------- 10-16
print(np.random.rand(10))
# 랜덤한 0<x<1보다 작은 난수 10개를 생성

print(np.random.rand(5,3))
# 5행 3열의 배열 출력

a = 10
b = 20
print((b-a)*np.random.rand(5)+a) # 10*난수 + 10 = 10~ 20사이의 난수 (실수)
print(np.random.randint(10,20,size=10)) # 10<=x<20사이의 10개의 원소를 가지는 랜덤한 정수 생서