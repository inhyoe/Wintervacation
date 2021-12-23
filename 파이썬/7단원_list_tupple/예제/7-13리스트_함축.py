s = []
for x in [1,2,3,4,5]:
    s.append(x**2) #이때 append는 리스트를 추가하는 것
print(s)
# 매우 번거롭다.
# 이를 개선하기 위해 리스트 함축을 사용한다.

print([x *x for x in range(10)]) # 리스트 함축 예시
st = 'hello world'
print([x.upper() for x in st]) # 대괄호를 넣었으므로 리스트식이고 st에있는 문자열을 하나씩 대입하여 x라는 리스트에 넣은다음 upper()을 해줌
    #  조건식        대입리스트 대입 값.
# 문자열중에서 첫문자만 따와 모두 대문자로 변환한 리스트 만들기

a = ['welcome','to','the','python','world']
print([x[0].upper() for x in a]) # 이때 리스트로 만들 변수(x와) 리스트에 대입할 변수(x)는 같아야한다.


