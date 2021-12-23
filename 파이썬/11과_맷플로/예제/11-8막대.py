from matplotlib import pyplot as plt
import numpy as np

plt.bar # 막대차트그리기x_range = range(len(years))

years = [1965,1975,1985,1995,2005,2015]
ko = [130,640,2450,1160,17790,27250]
jp = [890,5120,11500,42130,40590,38780]
ch = [100,250,290,540,1760,7940]
x_range = range(len(years))

plt.bar(x_range , ko, width= 0.3)
plt.bar(x_range , jp,width= 0.3)
plt.bar(x_range ,ch,width= 0.3)
plt.show()