import pandas as pd


Q = pd.DataFrame({'name' : ['A','B','C','D'],
                  'horse power' : [120,220,120,200],
                  'weight' : [1.9,2.1,1.5,2.9],
                  'efficiency' : [18.3,19.2,21.1,17.3]})
Q = Q.set_index('name') # NAME을인덱스로 잡아줌

print(Q)