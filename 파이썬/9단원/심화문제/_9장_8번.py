import re

PUT = input("문장을 입력하시오 : ")

English = re.findall('\s[A-Za-z]+', PUT)
Number = re.findall(' \d+', PUT)
EnglishNumber = re.findall('^.[A-Za-z]+\d+', PUT)

print("영문 단어: ",end ='')
for i in English:
    print(i,end='')
print()
print("숫자 : ",end ='')
for i in Number:
    print(i,end='')
print()
print("영문자+숫자 : ",end= '')
for i in EnglishNumber:
    print(i,end ='')