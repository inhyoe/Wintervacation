import pandas as pd

Q = pd.DataFrame({'name' : ['A','B','C','D'],
                  'horse power' : [120,220,120,200],
                  'weight' : [1.9,2.1,1.5,2.9],
                  'efficiency' : [18.3,19.2,21.1,17.3]})
lst = []
for i in range(len(Q)):
    lst.append('Q')
dict1 ={}
dict1['com'] = lst
Q1 = pd.DataFrame(dict1)#빈딕셔너리로 com의 데이터 프레임을 만듬
Q = pd.concat([Q,Q1],axis=1)# 데이터프레임 합침
Q = Q.set_index('name')# NAME을인덱스로 잡아줌
df = pd.DataFrame({
    'name' : ['A','B','C','D','E','F','G'],
    'horse power' : [130,250,190,300,210,220,170],
    'weight' : [1.9,2.6,2.2,2.9,2.4,2.3,2.2],
    'efficiency' : [16.3,10.2,11.1,7.1,12.1,13.2,14.2]
})
lst2 = []
for i in range(len(df)):
    lst2.append('P')
dict2 = {}
dict2['com'] = lst2
P2 = pd.DataFrame(dict2)#위의 원리와 동일
df = pd.concat([df,P2], axis=1)
P = df.set_index('name')

hpeQP = pd.DataFrame({'com' : ['P','Q'],
             ' ' : [P['horse power'].mean()*P['efficiency'].mean(), Q['horse power'].mean()*Q['efficiency'].mean()]})#각자의 마력과 효율의 평균값을 곱해주고 그에대한 데이터프레임을 만듬


hpeQP = hpeQP.set_index('com')#인덱스를 com으로 바꾸고
print(hpeQP)#출력
