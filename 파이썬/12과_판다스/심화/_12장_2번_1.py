import pandas as pd

df = pd.DataFrame({
    'name' : ['A','B','C','D','E','F','G'],
    'horse power' : [130,250,190,300,210,220,170],
    'weight' : [1.9,2.6,2.2,2.9,2.4,2.3,2.2],
    'efficiency' : [16.3,10.2,11.1,7.1,12.1,13.2,14.2]
})

set_df = df.set_index('name')
#df에 인덱스를 네임으로 바꿔서 set_df라는 변수에 넣어줌

print(set_df)
#출력