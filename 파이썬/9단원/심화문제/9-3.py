import string

문자열 = input('문자열을 입력하시오 : ')

소문자 = string.ascii_lowercase
대문자 = string.ascii_uppercase
숫자 = ['0','1','2','3','4','5','6','7','8','9']
소문자갯수 = 0
대문자개수 = 0
숫자개수 = 0
특문개수 = 0
for i in 문자열:
    if i in 소문자:
        소문자갯수 += 1
    elif i in 대문자:
        대문자개수 += 1
    elif i in 숫자:
        숫자개수 += 1
    else:
        특문개수 += 1

print('대문자 = ' , 대문자개수)
print('소문자 = ' , 소문자갯수)
print('숫자 = ' , 숫자개수)
print('특수문자 = ' , 특문개수)
