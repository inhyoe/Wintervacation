import matplotlib.pyplot as plt
import numpy as np

''' <<<<<<< HEAD '''

xData = np.random.randn(3000)
yData = np.random.randn(3000)
plt.scatter(xData,yData,alpha=0.5)
plt.title('Random Position')
plt.xlabel('x')
plt.ylabel('y')
''' ======= '''
""" xData = np.arange(20,50)
yData = xData + 2* np.random.randn(30)

plt.scatter(xData,yData)
plt.title('Real Age vs Physical Age')
plt.xlabel('Real Age')
plt.ylabel('Physical Age')
 """


xData = np.random.randn(3000)
yData = np.random.randn(3000)

plt.scatter(xData,yData,alpha = 0.3)
''' >>>>>>> c94c3223edf4a1514fb0bc0bd1091781f1527496 '''
plt.show()