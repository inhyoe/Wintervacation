import numpy as np

ages = np.array([18,19,25,30,28])
y = ages > 20
print(y) # 부울형 인덱싱 (boolean)
print(ages[ages>20]) # 논리적인 인덱싱