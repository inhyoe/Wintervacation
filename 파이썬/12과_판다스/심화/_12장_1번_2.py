import pandas as pd

f = pd.read_csv('C:\Users\kk\Desktop\파이썬 자습\코딩\파이썬\12과_판다스\weather.csv',index_col=0,encoding = 'CP949')

print(f.loc['2015-06-06'])#loc => 테이블안에 있는 값으로 인덱싱을 해주기 위해 사용