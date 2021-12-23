import numpy as np

# np.arange([start],stop,[step]) = start 부터 * 생략시 0 */ stop-1 까지 step만큼  
print(np.arange(5)) # 0~4까지
print(np.arange(1,6)) # 1~ 5까지
print(range(5))      # 아래와 결과값이 다름.
                     # 기본적으로 range(5)형은 0~4까지의 숫자를 출력하는 것이고
                     # arange(5)형은 0~4까지 넘파이 배열을 만들어 출력하는 것이다.
print(list(range(5)))