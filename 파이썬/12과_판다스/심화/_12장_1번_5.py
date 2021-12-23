import pandas as pd
f = pd.read_csv('C:\Users\kk\Desktop\파이썬 자습\코딩\파이썬\12과_판다스\weather.csv', index_col=0, encoding='CP949')

print(f[f['평균기온'] >30])
#f[조건식]으로 조건에 해당하는 행 출력