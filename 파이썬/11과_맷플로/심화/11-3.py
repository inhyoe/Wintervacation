import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0,50,60)
np_x = (np.array(x)).reshape(2,30)

print(np_x[::][:1])
print(np_x[::][1:])

print(np_x)
for x in range(30):
    plt.scatter(np_x[:][:1],np_x[:][1:])
plt.show()
''' 
plt.scatter(np_x,np_x)
plt.show() '''

 