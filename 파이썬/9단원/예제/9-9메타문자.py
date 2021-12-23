import re
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

