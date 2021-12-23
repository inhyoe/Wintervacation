import pandas as pd


Q = pd.DataFrame({'name' : ['A','B','C','D'],
                  'horse power' : [120,220,120,200],
                  'weight' : [1.9,2.1,1.5,2.9],
                  'efficiency' : [18.3,19.2,21.1,17.3]})
Q = Q.set_index('name')# NAME을인덱스로 잡아줌
import pandas as pd

df = pd.DataFrame({
    'name' : ['A','B','C','D','E','F','G'],
    'horse power' : [130,250,190,300,210,220,170],
    'weight' : [1.9,2.6,2.2,2.9,2.4,2.3,2.2],
    'efficiency' : [16.3,10.2,11.1,7.1,12.1,13.2,14.2]
})

P = df.set_index('name')


QP = pd.concat([P,Q])   #책 인쇄본.
print(QP)