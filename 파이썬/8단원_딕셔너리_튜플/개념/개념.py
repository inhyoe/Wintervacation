#딕셔러리와 리스트의 차이점
#딕셔너리는 값과 키가 있다.
#딕셔너리 생성 방법
#변수 = {}

#메서드
변수 = {}
변수['홍길동'] = '010-6631-3964'
print('2')
변수['강감찬'] = '010-2144-3224'

변수['김김김'] = '010-2312-1231'
print('1')
print(변수.keys()) # 변수의 키를 나타낸다
print('2')
print(변수.values()) # 각각의 변수의 값을 나타낸다
print('3')
print(변수.items()) # 변수의 키와 값을 나타낸다
변수['홍길동'] = '010-92391-9312'  # 딕셔너리의 값을 바꾼다
print('4')
print(sorted(변수)) # sorted - > 딕셔너리를 정렬하여 키를 반환한다
print('5')
sorted_변수 = sorted(변수.items())
print(sorted_변수)
print('6')
print(변수)
print('7')
sorted_phone = sorted(변수.items(), key = lambda x: x[0]) # 키를 가지고 정렬함
print(sorted_phone)
print('7')
#del 함수
del 변수['강감찬']
print(변수)
변수['강감찬'] = '010-1232-2311'
print(변수)
sorted_phonebook2 = sorted(변수.items, key = lambda x:x[1]) # 값으로 정렬
