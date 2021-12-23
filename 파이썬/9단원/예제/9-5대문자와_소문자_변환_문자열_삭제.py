import re


s = 'Hello, world'
print(s.lower())
print(s.upper())  # 대 소문자

# ----------------------------------

s = '   hello world     '
print(s.strip())  # 양쪽의 공백문자 모두 제거
print(s.lstrip()) # 왼쪽의 공백문자만 제거
print(s.rstrip()) # 오른쪽의 공백문자만 제거
# 변수명.strip(제거할 문장).capitalize() (제거할 문장)을 제거하고
# 첫글자를 대문자로 변경한다.

# -----------------------------------

s = 'www.booksr.co.kr.12312313'
print(s.find('.kr'))# 문자열을 찾아서 그 인덱스를 반환
print(s.find('x')) # 찾지 못하는 경우는 -1을 반환한다.
print(s.count('.')) # . 이 몇번 나타나는지 알려줌.
print(re.findall('\d+',s)) # findall함수는 re.findall('문자열',변수) 변수안에 문자열을 그대로 출력해준다.
