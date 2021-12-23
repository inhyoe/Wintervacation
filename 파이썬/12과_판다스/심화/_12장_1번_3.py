import pandas as pd

f = pd.read_csv('C:\Users\kk\Desktop\파이썬 자습\코딩\파이썬\12과_판다스\weather.csv', index_col=0, encoding='CP949')

print(f['평균기온'].max())
#평균기온으로 인덱싱후 max함수로 최곳값을 구해줌.