import numpy as np
import matplotlib.pyplot as plt

x1 =np.random.randn(1000)*6+25
y1 =np.random.randn(1000)*6+25
#1
x2 = np.random.randn(1000)*6+25
y2 = np.random.randn(1000)*3+25
#2
x3 =np.random.randn(1000)*6+25
y3_1 = np.random.randn(1000)
y3 = y3_1*6+25+y3_1
#3
plt.subplot(1,3,1)
plt.scatter(x1,y1,alpha = 0.4)
plt.subplot(1,3,2)
plt.scatter(x2,y2,alpha = 0.4)
plt.subplot(1,3,3)
plt.scatter(x3,y3,alpha = 0.4)
plt.show()
