import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(10,10)*2

plt.boxplot(x)
plt.show()