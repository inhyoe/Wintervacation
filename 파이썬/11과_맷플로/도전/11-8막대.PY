import matplotlib.pyplot as plt
import numpy as np

years = [1965,1975,1985,1995,2005,2015]
ko = [130,640,2450,1160,17790,27250]
jp = [890,5120,1150,4230,4053,38870]
ch = [100,250,290,540,1760,7940]
x_range = np.arange(len(years))

plt.bar(x_range+0.0,ko,width = 0.3)
plt.bar(x_range+0.35,jp,width = 0.3)
plt.bar(x_range+0.8,ch,width = 0.3)
plt.xticks(x_range,years)
plt.show()