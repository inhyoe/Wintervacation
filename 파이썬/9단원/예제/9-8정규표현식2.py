#규칙을 이용하여 문자를 추출하는 정규식과 메타 문자
import re
txt1 = 'Life is short, you neeed python'
txt2 = 'The best moments of my life'
txt3 = 'My life MY Choice'
print(re.search('^Life',txt1))
print(re.search('^Life',txt2))
print(re.search('^Life',txt3))
# ^ = 첫 문장에 Life가 있는지 검사함.
print(re.search('life$',txt1))
print(re.search('life$',txt2))
# $ = 끝문장에 life가 있는지 검사함.
print(re.search('[Ll]ife',txt2))
# Ll에서 대소문자 구별을 하지 않고 검사함.

# \d = 숫자
# \w =  문자와 숫자
# \s = 공백문자
# \S = 공백제외문자
# *  = 앞문자가 0번이상 반복
# + =  앞문자가 1번이상 반복
# . = 모든문자

#반복
# +
#ex )
