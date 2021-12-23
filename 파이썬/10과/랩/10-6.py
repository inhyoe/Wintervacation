import numpy as np
from numpy.core.fromnumeric import mean

player = np.zeros((100,3))
player[:,0] =  175 + 10*np.random.randn(100)
player[:,1] =  70 + 10*np.random.randn(100)
player[:,2] =  22 + 10*np.random.randn(100)
print('선수의 신장 평균겂',mean(player[:,0]))
print('선수의 신징 중앙값',np.median(player[:,0]))
print('선수의 체중',mean(player[:,1]))
print('선수의 체중 중앙값',np.median(player[:,1]))
print('선수의 나이' , mean(player[:,2]))
print('선수의 나이 중앙값' , np.median(player[:,2]))







