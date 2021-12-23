import matplotlib.pyplot as plt
import numpy as np
x = [x for x in np.arange(0,2.25,0.25)]
y = [x **2 for x in np.arange(0,2.25,0.25)]
z = [x **3 for x in np.arange(0,2.25,0.25)]
k = [2**x for x in np.arange(0,2.25,0.25)]

plt.plot(x,x, label='liner')
plt.plot(x,y, label='quadratic')
plt.plot(x,z, label='qublic')
plt.plot(x,k, label='power')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('My Plot')
plt.legend()
plt.show()