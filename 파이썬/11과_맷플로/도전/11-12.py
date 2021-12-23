import numpy as np
import matplotlib.pyplot as plt

n_bins = 15
x = np.random.randn(2000) # 표준 정규 분포
y = 10 + np.random.randn(2000)*2 # 평균 10 표준편차 2
z = -6 + np.random.randn(2000)*3

plt.hist(x, n_bins, histtype = 'bar', color = 'blue',alpha = 0.3)
plt.hist(y, n_bins, histtype = 'bar', color = 'red' ,alpha = 0.3)
plt.hist(z, n_bins, histtype = 'bar', color = 'green' ,alpha = 0.3)
# alpha 는 색의 불투명도를 나타낸다.


plt.show()