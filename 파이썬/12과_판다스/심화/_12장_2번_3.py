import pandas as pd

df1 = pd.DataFrame({
    'name' : ['A','B','C','D','E','F','G'],
    'horse power' : [130,250,190,300,210,220,170],
    'weight' : [1.9,2.6,2.2,2.9,2.4,2.3,2.2],
    'efficiency' : [16.3,10.2,11.1,7.1,12.1,13.2,14.2]
})
lst = []    #df1이라는 데이터프레임에 추가데이터 넣기위한 준비
df = {}     #또 그걸위한 딕셔너리
for i in range (len(df1)):  #df1의 행의 길이로 hp*efficiency를 리스트에 넣어줌
    lst.append(df1['horse power'][i] * df1['efficiency'][i])
df['hp*horse power'] = lst      #그걸 딕셔너리에 받고
df2 = pd.DataFrame(df, index = ['A','B','C','D','E','F','G'])#인덱스를 set_df랑 같이만들어줌

set_df = df1.set_index('name')
df_3 = pd.concat( [set_df, df2],axis=1) #axis =1 로 열을 늘려줌으로써 데이터프레임 완성

print(df_3[df_3['hp*horse power']==df_3['hp*horse power'].max()])#그대로 출력
