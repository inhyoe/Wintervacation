import re
txt = 'Life is too short, you need python, My Life for iara'
txt2 = ' The best moments of my Life.'
print(re.search('Life', txt),1) # 0~4번째까지 Life가 있다고 출력 뒤의 Life는 출력하지 않음
print(re.search('life', txt2),2) # 대 - 소문자를 구별함.
match = re.search('Life',txt,)
print(match.group()) # 매치된 문자열을 반환.
print(match.start()) # 변수의 시작인덱스를 나타냄
print(match.end()) # 변수의 끝인덱스를 나타냄
print(match.span()) #일치하는 구간을 슬라이싱하기위한 인덱스를 나타낸다.

print(re.search('Life|life',txt2)) # life 또는 Life를 찾으라는 의미 
print(re.search('[Ll]ife',txt2)) # 위 식을 축약함. 


#- --------------------

text = 'Please call me 010-1234-5678'

#group() 기능을 테스트 하는 코드

regex = re.compile('(\d{3})-(\d{4}-\d{4})')
                    # 그룹1번  - ( 그룹 2번 )

match_obj = regex.search(text)
print(match_obj.group())
print(match_obj.group(1))
print(match_obj.group(2)) # 그룹 2번

