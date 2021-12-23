import pandas as pd

df = pd.DataFrame({
    'name' : ['A','B','C','D','E','F','G'],
    'horse power' : [130,250,190,300,210,220,170],
    'weight' : [1.9,2.6,2.2,2.9,2.4,2.3,2.2],
    'efficiency' : [16.3,10.2,11.1,7.1,12.1,13.2,14.2]
})

set_df = df.set_index('name')

print(set_df[set_df['horse power'] == set_df['horse power'].max()])

# 1번_4와 똑같은문제 똑같이 데이터프레임에 조건걸고 해당조건에 해당하는 행을 출력함.