import matplotlib.pyplot as plt
import numpy as np

xData = np.arange(20,50)
yData = xData +2*np.random.randn(30)

plt.scatter(xData, yData)
plt.title('Real Age vs Physical Age')
plt.xlabel('Real Age')
plt.ylabel('Physical Age')

plt.show()
#https://nittaku.tistory.com/443 정규분포 관련 np.random.~~()모듈 정리;