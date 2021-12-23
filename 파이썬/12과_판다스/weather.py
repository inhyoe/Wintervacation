import csv
<<<<<<< HEAD
import pandas
f = open('C:\Users\kk\Desktop\파이썬 자습\코딩\파이썬\12과_판다스\weather2.csv')
=======
f = open('/Users/mac/Desktop/코딩2/파이썬/12과_판다스/weather.csv')
>>>>>>> f4ae1a5d41c3502e6d64ffff7b9f16f006f66f56
data = csv.reader(f)
header = next(data)
for row in data:
    print(row)
f.close()