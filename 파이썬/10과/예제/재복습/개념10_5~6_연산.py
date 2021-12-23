import numpy as np
# 사용법 np.array(변수 혹은 리스트)
salary = np.array([220,250,230])
salary = salary * 2
print(salary)
# 각각의 원소의 곱을 출력한다

salary = [220,250,240] 
salary = salary * 2
print(salary)
# 각각의 원소를 2번 출력한다.

salary = np.array([220, 250, 230])
salary = salary * 2.1
print(salary)
# 실수를 출력한다.

scores = np.array([88, 72, 93, 94, 89, 78, 99])
print(scores[2])
print(scores[1:4]) # 인덱스 슬라이싱.

ages = np.array([18,19,20,21,22,24])
print(ages> 20)
# 값을 출력하는 것이 아닌 False True를 출력함.

# 이때 원소들의 집합을 출력하고 싶으면
print(ages[ages > 20])
print(10,'-',8)
y = [[1,2,3],[4,5,6],[7,8,9]] # 2차원 리스트형 배열
# 1 2 3
# 4 5 6
# 7 8 9
print(y) 
np_array = np.array(y)    # 2차원 넘파이 배열
print(np_array)
print([y[0][2]])
print(type(np_array[0][2])) # 출력은 정수로 되지만 타입은 넘파이형임
# 1 2 3 <-
# 4 5 6
# 7 8 9
np_array[0,0] = 12
print(np_array) # 원소를 바꿈.
np_array[0,0] = 1.234
print(np_array)

print('------------------------------------')
print('10 - 10')

np_array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(np_array[0:2, 2:4]) #0번째 ~ 1번째 행까지 선택 후 2~ 3번째 원소 출력
print(np_array[1,1:3]) # 
np_array = np.array([[(0,0),(0,1),(0,2),(0,3)]
                    ,[(1,0),(1,1),(1,2),(1,3)]
                    ,[(2,0),(2,1),(2,2),(2,3)]
                    ,[(3,0),(3,1),(3,2),(3,3)]]) # 2차원 배열의 원소 4개
print(np_array[::2][::2]
      ,np_array[::2,::2])
# [][]형과 , [,]의 차이점은 [][]은 [첫][둘] 행만을 슬라이싱 하는 경우이고
# [start:stop:step,start:stop:step]은 start~stop까지 step만큼 건너뛴 행의
#                                  원소가 start~stop까지 step만큼 건너뛴 원소의 값이다.
#                                  한마디로 행 ,원소 슬라이싱이다.

print('10 - 11 ')
print('-----------------------------------')
# 이러한 넘파이 배열에서도 또한 연산이 가능하다
y = [[1,2,3],[4,5,6],[7,8,9]]
np_array = np.array(y)
print(np_array > 5 ) # 이것 또한 False, true를 출력한다.(부울)
print(np_array[np_array > 5]) # 원소들을 출력하고 싶으면

# 복잡한 연산을 수행하기
print(np_array[:,2] >5) 