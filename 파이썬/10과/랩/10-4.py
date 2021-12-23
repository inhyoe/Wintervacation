import numpy as np

x= np.array([[1.83, 1.76, 1.69, 1.86,1.77,1.73],
             [86.0,74.0,59.0,95.0,80.0,68.0]])
y = x[0:2,1:3] # 1.76, 1.69
z = x[0:2][1:3] # 전체 선택 [0:2] 후에 1행 선택 [1:3]
print('x shape : ' , x.shape) # 1.76,1.77
print('y shape : ' , y.shape)
print('z shape : ' , z.shape)
print('z value : ' , z)
print( y)
print('BMI data' , x[0] / x[1]**2 )