#https://www.youtube.com/watch?v=pY0WdM3j18Q 참고

# 문자클래스 []
# [abc] = [a-c]  // [0-5] = [012345]
# 'a'는 정규식과 일치하는 문자인 "가 있으므로 매치"
import re
txt1 = 'Life is short, you neeed python'
txt2 = 'The best moments of my life'
txt3 = 'My life MY Choice'
# 정규식 기호
# . 문자의 중간에 위치한다
re.search('A..A','ABBA') # True ..은 중간의 자릿수
print(re.search('A..A','ABBBBA')) # None
# ^ 문자의 처음에 위치한다  =  첫 단어로 검사하려는 단어가 있는지 검사
# ex ) 
re.search('^Life',txt1)
# $ 문자의 끝에 위치한다
re.search('life$',txt2)
# * 문자의 끝에 위치한다 = 두 문자중 하나의 문자라도 들어가 있다면 True
print(re.search('A..A','ABA'))
print(re.search('A..A','ABBA')) # 4글자이므로 조건에 충족함
print(re.search('A..A','ABBBA'))
print(re.search('A...A','ABBBA')) # 5글자이므로 조건에 충족함.
print('----------------------') # 글자 중간에 ..이 들아간다.

print(re.search('AB*','A'))  # A가 조건에 맞음   // 글자 끝부분에 * 가 들어간다.
print(re.search('AB*','AA')) # A가 조건에 맞음
print(re.search('AB*','J-HOPE')) # 조건에 맞지 않음
print(re.search('AB*','X-MAN')) # A가 조건에 맞음
print(re.search('AB*','CABBA')) # ABB가 조건에 맞음
print(re.search('AB*','CABBBBBA')) # ABBBBBB가 조건에 맞음


print('----------------------')
print(re.search('AB?','A')) # 임의의 문자가 0회 또는 1회 반복된 패턴 'A'가 조건에 맞음  // 글자 끝부분에 ?가 들어간다
print(re.search('AB?','AA'))# A가 조건에 맞음
print(re.search('AB?','J-HOPE')) # x
print(re.search('AB?','X-MAN')) # A가 조건에 맞음
print(re.search('AB?','CABBA')) # AB가 조건에 맞음
print(re.search('AB?','CABBBBBA')) # AB가 조건에 맞음

print('----------------------')
print(re.search('AB+','A')) # +직전의 패턴이 반복되는지 // 조건 x
print(re.search('AB+','AA'))# 조건 x
print(re.search('AB+','J-HOPE')) # x
print(re.search('AB+','X-MAN')) # 조건 x
print(re.search('AB+','CABBA')) # ABB가 조건에 맞음
print(re.search('AB+','CABBBBBA')) # ABBBBBB가 조건에 맞음
