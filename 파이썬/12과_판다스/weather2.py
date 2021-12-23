import csv
f = open('/Users/mac/Desktop/코딩2/파이썬/12과_판다스/weather.csv')
data = csv.reader(f)
header = next(data)
max_wind = 0.0

for row in data:
    if row[3] == '':
        wind = 0
    else:
        wind = float(row[3])
    if max_wind < wind:
        max_wind = wind

print('지난 10년간 울릉도의 최대 풍속은 ', max_wind, 'm/s')