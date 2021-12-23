import re
문장 = input('문장을 입력하세요') # 문장을 입력받는다

print('영문단어 : ',re.findall('\s[A-z]+',문장))
print('숫자 : ',re.findall('\S\d+',문장))
print('영문자+숫자',re.findall('[A-z]+[0-9]+',문장))

#영문단어
#숫자
#영문자 + 숫자
# Jian777 is vert famous Data scientis. He is only 26 years old but published 19 papers.

''' import string

N = input('문장을 입력하시오.')
src_str = string.ascii_lowercase + string.ascii_uppercase
boo = True;
num_arr =[]
str_arr = []
num_str_arr = []
for i in N.split(' '):
    if i.isdigit:
        num_arr.append(i)
    elif i.isalpha:
        str_arr.append(i)
    else:
        num_str_arr.append(i)
print('영문단어 : {}'.format(str_arr))
print('숫자 : {}'.format(num_arr))
print('영문자 + 숫자 : {}'.format(num_str_arr)) '''