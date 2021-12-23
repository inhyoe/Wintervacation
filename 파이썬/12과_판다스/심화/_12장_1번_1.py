import pandas as pd

f = pd.read_csv('C:\Users\kk\Desktop\파이썬 자습\코딩\파이썬\12과_판다스\weather.csv',index_col=0,encoding = 'CP949')
#한글이 깨지게 나와서 인코딩을해줌
#index_col로 깔끔하게해줌

print(f.head()[:3])
print(f.tail()[-3:])