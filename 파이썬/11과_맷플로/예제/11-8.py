import matplotlib.pyplot as plt
import numpy as np

years = [ 1960,1970, 1980, 1990, 2000, 2010]
ko = [130,650,2450,11600,17790,27250]
jp = [890,5120,11500,42130,40560,38780]
ch = [100,200,290,540,1760,7940]

x_range = np.arange(len(years))
plt.bar(x_range+ 0.0, ko, width = 0.25,label = 'kroea')
plt.bar(x_range+ 0.3, jp, width = 0.25,label = 'jp')
plt.bar(x_range+ 0.6, ch, width = 0.25,label = 'ch')
plt.show()