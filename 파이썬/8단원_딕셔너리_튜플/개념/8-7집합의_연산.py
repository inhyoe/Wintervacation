A = {1,2,3}
B = {1,2,3}
print(A == B) # 연산이 가능하다.
B = {1,2,3,4,5}
print( A<B) # 크기도 비교 가능.


print('-------------------------------------------')
# 메소드 사용법.
a_set = { 1,2,3,4,5,5,6}
print(len(a_set)) #길이
print(max(a_set)) # 최댓값
print(min(a_set)) # 최솟값
print(sorted(a_set)) #중복값 삭제 후 정렬
print(sum(a_set)) # 중복 원소는 한번만 사용 가능하다.
a_set = {1,2,3,4}
print(all(a_set)) # 0값이 있다면 false 없다면 true
print(any(a_set)) # 0이 있는가를 검사한다. # ??????????????????????????????????????????

# 집합의 연산 8-8
print('------------------------------------------')
a = {1,2,3}
b = {3,4,5}
print(a|b) # 합집합
print(a.union(b)) # 합집합 메소드

print(a&b) # 교집합
print(a.intersection(b)) # 교집합 메소드

print(a-b) # 차집합
print(a.difference(b))  # 차집합 메소드

print((a|b) -( a&b))
print(a ^ b) # 같다.(대칭 차집합)
print(a.symmetric_difference(b)) #메소드