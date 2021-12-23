# 리스트 함축 표현에서 조건식을 붙이기.

print([x for x in range(10) if x % 2 ==0])

print([x*x for x in range(10) if x % 2 ==0])

# 입력값도 넣을 수 있다

print([int(x) for x in input('정수를 여러개 입력하세요 (구분자 띄어쓰기)').split()])
# 이때 구분자는 .split()으로 구별한다 (빈칸은 띄어쓰기)

print([int(x) for x in input('정수를 여러개 입력하세요 : ').split() if x.isdigit()])
# isdight() 함수는 문자인지 숫자인지 구별함.

#숫자를 합치는 것도 가능
print([(x,y) for x in [1,2,3] for y in [3,1,4]]) # 이것은 튜플형으로 묶었다.  -튜플은 수정불가능
print([[x,y] for x in [1,2,3] for y in [3,1,4]]) # 이것은 리스트형으로 묶었다.

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]) # 이것은 튜플형으로 묶었다. 추가적으로 x ==y가 아닌경우만.
