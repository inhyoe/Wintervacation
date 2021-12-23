input_value = int(input('n을 입력하세요 : '))
a = 0 # 첫번째 줄의 값
b = 0 # 짝수번째 줄의 값.
c = 0 # 각 값의 초기값.
print(input_value)
for i in range((input_value)):
    if i % 2 == 0: # 짝수번째 줄의 값
        for k in range((input_value)): # 줄의 값 내용 출력
            c = c +1
            a = c
            print('{0:3}'.format(a),end='')
            b = a + input_value + 1 
    else: # 홀수번째 줄의 값
        for k in range(input_value): #줄의 값 내용 출력
            
            b = b - 1
            print('{0:3}'.format(b),end='')
            c = a+input_value 
    print()
        
        

            
            
# 1  2  3  4  5   a = a+1
# 10  9  8  7  6  b = a+a - 1        5  입력시
# 11 12 13 14 15  a = a+a + 1   
# 20 19 18 17 16  b = a+a+a+a-1
# 21 22 23 24 25  a = a+a+a+a+1

# 6 입력시
# 1 2 3 4  5  6
# 7 8 9 10 11 12

