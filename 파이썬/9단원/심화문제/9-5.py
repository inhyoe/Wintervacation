import re

s = 'Korea is awesome! I REALLY LOVE KOREA'

print(len(re.findall('[kK][oO][rR][eE][aA]',s))) # 문자열 추출
print(type(re.findall('[kK][oO][rR][eE][aA]',s)))
