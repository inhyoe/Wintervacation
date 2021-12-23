import numpy as np

player = [[170, 76.4]
         ,[183, 86.2]
         ,[181, 78.5]
         ,[176, 80.1]]
np_player = np.array(player)
print('몸무게 80이상')
print( np_player[np_player[:,1] >= 80])

print('키가 180이상')
print( np_player[np_player[:,0] >= 180])
