# arange() 함수
# np.arange([start],stop,[end])
# numpy 배열을 자동으로 생성해주는 함수이다.
# range와 다른점은 range는 넘파이 배열을 자동으로 생성해 주지는 않음.
import numpy as np
print(np.arange(5))
print('---- 예제 ------')
# range함수와 같은 결과를 얻고 싶을 때는
print(np.array(range(5)))

# 함수설명
# linspace() - numpy.linspace(start,stop,[num (기본값은 50)])
# start~ stop수까지 num의 갯수만큼 사잇값을 출력한다
print(np.linspace(0,10)) # 기본값
print(np.linspace(0,10,100)) # num값 임의  지정.

print('------10 , 14 예제 소스코드 --------')

y = np.arange(12) # 0~11까지의 넘파이 배열이 생성된다.
print(y)
print(y.reshape(3, 4)) # 2차원 배열 3가지를 4개로 묶는다

print(y.reshape(6,2)) # 2차원 배열 6개로 2개로 묶는다

y.reshape(6,2)

print(y.flatten()) # 2차원 배열을 1차원으로 묶어준다.
print(np.random.rand(5,3)) # 5개의 행 생성후 3가지 원소를 넣는다
print(np.random.randint(1,7,size = 10)) # 1~6까지의 원소를10개의 넘파이 배열에 삽입.
print(np.random.randint(1,11,size = (4,7))) # 4가지 행을 생성 후 7가지 원소로 채운다

print('--------평균과 중앙값(정규분포)-----------')
# 평균과 중앙값 계산하기
# 10명의 키를 난수로 설정한 후 평균은 175이고 표준편차는 10인 정규분포를 따른다
m = 175
sigma = 10
heights = m + sigma * np.random.randn(10)
print(heights)