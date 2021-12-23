import random
import string
src_str = string.ascii_uppercase
src_str2 = string.ascii_lowercase
num = random.randint
password = int(input('몇자리를 원하시나요?'))
# 문제 해결 방법
# 패스워드에 랜덤한 숫자 및 랜덤한 대 소문자도 나와야 한다.
# 이럴 경우에는 
for i in range(password):
    