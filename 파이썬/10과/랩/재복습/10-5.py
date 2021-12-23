import numpy as np

player = [[170, 76.4],
         [183, 86.2],
         [181, 78.5],
         [176, 80.1]] # --> 리스트형임
print(player)   

np_player = np.array(player)  # 넘파이형이라 연산이 가능함!!
print('몸무게가 80 이상인 선수 정보' )
print(np_player[np_player[:, 1] >=80.0])
