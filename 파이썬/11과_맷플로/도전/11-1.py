# 난수를 가지는 그래프를 그리기.
# 난수를 가지려면 x축은 1~ 1000까지 일정하게 가야한다
# y축은 난수가 생성된 값이다
# 1000개의 난수를 생성한 후 y값에 대입해야함.
# 그렇다면

import matplotlib.pyplot as plt
import numpy as np
x = range(1000)

y = []
for i in range(1000):
    y.append(np.random.uniform(-3,3))
plt.plot(x , y , marker = 'o')

plt.axis([-3,1200,-3,3])
plt.show()