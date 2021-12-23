# sort() 메소드
numbers = [9,8,7,6,5,4,3,13,34,53,32,52]
numbers.sort()
print(numbers) # 크기순으로 정렬해준다

# 문자열의 sort()메소드

bts = ['a','r','c','q','p']
bts.sort()
print(bts)
# reversed = True 메소드
numbers.sort(reverse=True)
print(numbers) # 역순으로 정렬해준다.
print(sorted(numbers)) # numbers를 정렬하므로 변함이 없음
numbers.sort(reverse=True)
print(sorted(numbers)) # 증명.
print(sorted("FADEWAY"))