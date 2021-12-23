import numpy as np
x1 = [i for i in range(100)]
x2 = [i + np.random.randint(1, 10) for i in range(100)]
x3 = [i + np.random.randint(1,50) for i in range(100) ]
x4 = [np.random.randint(1,100) for i in range(100)]


# x1 = [ 1 ~99]
# x2 = [(1~99) + 1~9까지의 난수 더하기]
# x3 = [(1~99) + 1~49까지의 난수 더하기]
# x4 = [1~99까지 난수 100개 생성 ]

print(np.corrcoef([x1,x2,x3,x4]))