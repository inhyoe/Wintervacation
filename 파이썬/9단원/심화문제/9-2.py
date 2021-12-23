import string

문자열 = input(' 문자열을 입력하세요 ')
대문자 = string.ascii_uppercase
소문자 = string.ascii_lowercase
숫자 = ['0','1','2','3','4','5','6','7','8','9']
포함된_대문자 = []
포함된_소문자 = []
포함된_숫자 = []
포함된_특수문자 = []

for i in 문자열:
    if i in 대문자:
        포함된_대문자.append(i)
    elif i in 소문자:
        포함된_소문자.append(i)
    elif i in 숫자:
        포함된_숫자.append(i)
    else :
        포함된_특수문자.append(i)
print(문자열)
print(포함된_대문자)
print(포함된_소문자)
    
print("{0}{1}{2}{3}".format(''.join(list(포함된_소문자)),
                      ''.join(list(포함된_대문자)),
                      ''.join(list(포함된_숫자)),
                      ''.join(list(포함된_특수문자))))