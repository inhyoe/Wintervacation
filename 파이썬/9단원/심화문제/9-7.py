# 카이사르 암호를 재구성 해봅시다.
import string
입력값 = input('문장을 입력해 주세요')
칸수 = int(input('이동시킬 칸 수를 적으세요'))
소문자 = string.ascii_lowercase
대문자 = string.ascii_uppercase
카이사르_소문자 = 소문자[칸수:]+소문자[:칸수]
카이사르_대문자 = 대문자[칸수:]+대문자[:칸수]

def 카이사르_소(ch):
    value = 소문자.index(ch)
    return 카이사르_소문자[value]

def 카이사르_대(ch):
    value = 대문자.index(ch)
    return 카이사르_대문자[value]

print(카이사르_대('A'))
#여기서는 카이사르 암호가 만들어 져야함.

for i in 입력값:
    """ print(i,',',end ='') """
    if i in 소문자:
        print(카이사르_소(i),end = '')
    elif i in 대문자:
        print(카이사르_대(i), end = '')
    else:
        print(i, end='')
print()