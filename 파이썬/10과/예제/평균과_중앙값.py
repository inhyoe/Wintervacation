import numpy as np

m = 175
sigma = 10
height = m + sigma*np.random.randn(100)
# 100 명의 키를 난수로하는 정규분포,

np.mean(height) # (height + height ... )/100
np.median(height) # 리스트의 중앙에 있는 항목 출력
