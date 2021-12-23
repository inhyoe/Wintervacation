import matplotlib.pyplot as plt
import math
""" x = [x for x in range(350) ]
y = [math.sin(x) for x in range(350)]
 """
 
 
x = []
y = []
for angle in range(360):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))
plt.title('SINE WAVE')
plt.plot(x,y,'r-')
plt.show()