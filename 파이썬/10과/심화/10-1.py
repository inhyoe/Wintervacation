import numpy as np

num_arr = np.arange(21) #1번째


print(num_arr) 

num_arr = np.arange(20,0,-1) # 2번째 
print(num_arr)

print('num_arr내의 모든 원소의 합' , sum(num_arr)) # sum함수 세번째

print('5행 4열의 배열 ')
print(num_arr.reshape(5,4)) # 5행 4열로 변경 네번째빈칸