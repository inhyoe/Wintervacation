a = input('문자열을 입력하세요')
for i in (range(len(a)+1)):
    print(a[:i])
for k in reversed(range(len(a))):
    print(a[:k])
# reversed 함수의 경우 range가 출력되는 순서를 반대로 바꾸어줌.
# 추가로 range(start,stop,step)의 경우 출력이 range(start,stop,step)이다. 