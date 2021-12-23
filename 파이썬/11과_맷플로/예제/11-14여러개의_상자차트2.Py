import numpy as np
import matplotlib.pyplot as plt

data = [1,2,3,4,5]
data2 = [2,3,4,5,6]


plt.boxplot(np.array([data,data2]))
plt.show()