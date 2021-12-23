# 집합 리스트

numbers = { 2,4,1}
print(numbers) # 크기순으로만 나열해줌

numbers = { 1,2,5,4,2,1,1}
numbers = set()
print(numbers) # 중복을 제거해줌

# 8-6번
numbers = { 2,4,1}
if 1 in numbers: # 집합 안에 1이 있는지
    print('o')
    
numbers = { 1,2,4}
for x in numbers:   # 집합은 순서가 없기 때문에 인데스를 가지고 접근 x
    print(x, end='') # 이렇게 순서대로 호출은 가능.
    
# 집합의 항목에 접근하는 연산.

numbers = { 1, 2, 3}
numbers.add(4) # 집합에 추가하는 방법
print()
print(numbers)

numbers.remove(4) # 집합의 원소를 삭제하는 방법
print(numbers)